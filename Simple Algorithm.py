#!/usr/bin/env python
# coding: utf-8

""" Dynamic Lot-Size Algorithm
Author: Jack Wilson

The following algorithm follows the first step-by-step procedure
listed in Figure 2 of https://doi.org/10.1287/mnsc.24.16.1710.

Notes: 
    -   This program is designed for fixed K and h values.
    -   Production must take place in period 1.
    -   This completes 2^T partial and complete production plans
        but DOES NOT REGARD FEASABILITY.
"""

# imports
from IPython.display import display
import pandas as pd

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
    P = Subproblem(None)

    g_opt = 1e99
    act_lst = [P]

    # goto step 2
    term_check()


# step 2 - termination check
def term_check():
    """Check if the active list is empty, else pop the last
    subproblem and continue.
    """

    while len(act_lst) > 0:
        # goto step 3
        decomp(act_lst.pop())

    # the list is empty, report the best result
    print(f'STOP, P{"".join(str(i) for i in best.sigma)} is the optimal solution at ${g_opt}.')
    print('WARNING: The solution may be infeasible.')


# step 3 - decomposition loop
def decomp(P):
    """For 2 <= t <= sigma1 - 1, add all subproblems to the 
    active list.

    Notes
    -----
    Sigma1 is represented by the horizon T or the lowest number
    of sigma minus one.
    """

    # find the next sigma value
    sigma1 = P.sigma[0] if P.sigma else T + 1

    # retrieve the previous/new sigma values
    sigma = P.sigma if P.sigma else []

    # add all of the subproblems
    for t in range(2, sigma1):
        act_lst.append(Subproblem([t] + sigma))
    
    # goto step 4
    complete(sigma)

# step 4 - complete schedule
def complete(sigma):
    global g_opt, best

    # create the final subproblem for sigma
    P = Subproblem([1] + sigma)

    # update the optimal solution if better
    if P.g < g_opt:
        g_opt = P.g
        best = P

    
if __name__ == '__main__':
    # define input variables
    d_j = [100, 79, 230, 105, 3, 10, 99, 126, 40]
    C_j = [120, 200, 200, 400, 300, 50, 120, 50 ,30]

    K = 450
    h = 2

    # run the program
    main()

