#!/usr/bin/env python
# coding: utf-8

""" Dynamic Lot-Size Algorithm
Author: Jack Wilson

The following algorithm follows the first step-by-step procedure
listed in Figure 3 of https://doi.org/10.1287/mnsc.24.16.1710.

Notes: 
    -   This program is designed for fixed K and h values.
    -   Production must take place in period 1.
"""

# imports
from IPython.display import display
from itertools import combinations
import pandas as pd

DEBUG = True
LINE = '-' * 50
DLINE = '=' * 50

# define variables to be used
d_j, C_j, K, h = [None] * 4
T, j, g_opt, act_lst = [None] * 4
best = None


class Subproblem:
    def __init__(self, sigma: list):
        '''Calculates and contains the subproblem info.

        Parameters
        ----------
        sigma: list
            An ordered list of the subscript attached to the
            subproblem (includes period t)
        
        Notes
        -----
        The starting instance should be null.
            e.g. Null == None
            e.g. tsigma_89 == [t, 8, 9] where t: int < 8
        '''

        # period - list of each number
        self.sigma = sigma if sigma else None

        # total cost
        self.g = self.calc_g() if sigma else None

        # backshifted
        self.d_sig = self.calc_d_sig() if sigma else None

    def __repr__(self) -> str:
        sigma = ''.join(str(i) for i in self.sigma) if self.sigma else ''
        return f'P{sigma}'

    def calc_g(self):
        """Calculates the cost g."""

        g = 0
        streak = 1

        # iterate through each period to determine the overall cost
        for t in j:
            if t < self.sigma[0]:
                # ignore cases before the current period
                continue
            elif t in self.sigma:
                # if reordering this period
                streak = 1
                g += K
            else:
                # if holding inventory this period
                g += h * streak * d_j[t-1]
                streak += 1

        return g
        
    def calc_d_sig(self):
        """Calculate the backshift d_sigma
        
        Sum of the current and future demands subracted by the 
        available capacity on production periods.
        """

        c = sum(C_j[t-1] for t in self.sigma)
        d = sum(d_j[t-1] for t in j[self.sigma[0]-1:])
        return max(0, d - c)


def debug(*args):
    """Print string and write to file if DEBUG is enabled."""
    print(*args) if DEBUG else None
        

# setup
def main():
    """Begin by displaying the problem and setting some intial 
    variables.
    """

    global T, j

    # define the period and the respective range
    T = len(C_j)
    j = [i + 1 for i in range(T)]

    # display the problem
    debug(DLINE + '\nDisplay the problem\n' + LINE)
    print(f'K = $ {K:.2f}')
    print(f'h = $ {h:.2f}')

    display(pd.DataFrame({'Period, j': j, 'D_j': d_j, 'c_j': C_j}).set_index('Period, j').T)

    # goto step 1
    init()


# step 1 - initialization
def init():
    """Initialize the overall problem.
    
    Set P_sigma on the active list, where sigma is null,
    the cost is 0 and the optimal cost is infinite.
    """

    global g_opt, act_lst

    debug(DLINE + '\nStep 1 - Initialization\n' + LINE)
    P = Subproblem(None)

    g_opt = 1e99
    act_lst = [P]

    debug(f'Created subproblem {repr(P)} and added it to the AL.')
    debug(f'Set sigma=None, g(P)={P.g}, g*={g_opt}')

    # goto step 2
    term_check()


# step 2 - termination check
def term_check():
    """Check if the active list is empty, else pop the last
    subproblem and continue.
    """

    while len(act_lst) > 0:
        # goto step 3
        debug(DLINE + '\nStep 2 - Termination Check\n' + LINE)
        debug('AL:', act_lst)
        debug(f'Removing {act_lst[-1]} from the AL.')

        decomp(act_lst.pop())

    # the list is empty, report the best result
    if best:
        sln = ''.join(str(i) for i in best.sigma)
        print(DLINE + f'\nThe optimal solution is P{sln} with cost ${g_opt}')
    else:
        print('No solution was reached.')


# step 3 - decomposition loop
def decomp(P, t: int = None):
    """Add all subproblems to the active list if they do
    not get eliminated.

    Parameters
    ----------
    P: Subproblem
        The subproblem popped from the active list.
    t: int
        For the special cases of step 3.3, 3.4, 3.5.
    """

    # find the next t
    sigma1 = P.sigma[0] if P.sigma else T + 1
    t = t if t else sigma1 - 1

    # retrieve the previous/new sigma values
    sigma = P.sigma if P.sigma else []

    # create the subproblem
    P_t = Subproblem([t] + sigma)

    debug(DLINE + '\nStep 3 - Decomposition Loop\n' + LINE)
    debug(f't={t}')
    debug(f'Created subproblem {P_t}.\n')

    # step 3.1 - test feasibility with property 1
    rhs = sum(C_j[i-1] - d_j[i-1] for i in j[:t-1])
    debug(f'3.1) Property 1: {P_t.d_sig} > {rhs}?')

    if P_t.d_sig > rhs:
        debug('Infeasible. Go back to step 2.')
        return

    # step 3.2 - if t=1, go to step 4
    debug(f'3.2) g(P)={P_t.g}, d_sig={P_t.d_sig}')

    if t == 1:
        debug('t = 1. Go to step 4.')
        complete(sigma)
        return

    # step 3.3 - test optimality with property 2A and static K
    debug(f'3.3) Property 2: {P_t.g} > {g_opt - K}?')
    if P_t.g > g_opt - K:
        debug('Subproblem not optimal. Go to step 3.1')
        decomp(P, 1)

    # step 3.4 - test domination with property 3
    debug('3.4) Checking if the subproblem can be dominated.')

    # generate the completions of the partial plan to test
    range_ = range(t+1, T+1)
    plans = [
        [t] + list(subset)
        for len_ in range(1, len(range_)+1)
        for subset in combinations(range_, len_)
    ]

    # test for domination
    # in practice, d_sig == 0 for the completion
    for plan in plans:
        P_ = Subproblem(plan)
        if P_.d_sig == 0 and P_.g < P_t.g:
            debug(f'{P_} dominates {P_t}: {P_.g} < {P_t.g}. Go to step 3.1.')
            decomp(P, t-1)
            return
    
    # step 3.5 - append the subproblem to the active list
    debug(f'3.5) Failed to eliminate {P_t}. Adding to the AL.')
    act_lst.append(P_t)
    decomp(P, t-1)
    return


# step 4 - complete schedule
def complete(sigma):
    global g_opt, best
    debug(DLINE + '\n Step 4 - Complete Schedule\n' + LINE)

    # create the final subproblem for sigma
    P = Subproblem([1] + sigma)

    # update the optimal solution if better
    if P.g < g_opt:
        debug(f'{P} is more optimal: {P.g} < {g_opt}')
        g_opt = P.g
        best = P
        return

    debug(f'{P} is not optimal: {P.g} !< {g_opt}')

    
if __name__ == '__main__':
    # define input variables
    d_j = [100, 79, 230, 105, 3, 10, 99, 126, 40]
    C_j = [120, 200, 200, 400, 300, 50, 120, 50 ,30]

    K = 450
    h = 2

    # run the program
    main()

