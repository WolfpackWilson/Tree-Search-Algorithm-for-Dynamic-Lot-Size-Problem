# Tree Search Algorithm for Dynamic Lot Size Problem
This repository provides code for the tree search algorithms detailed in 
_An Algorithm for the Dynamic Lot-Size Problem With Time-Varying Production 
Capacity Constraints_ by Baker et al.

https://doi.org/10.1287/mnsc.24.16.1710

### Important Notes
-   This program is designed for fixed K and h values.
-   Production must take place in period 1.

### Example Problem
```
==================================================
Display the problem
--------------------------------------------------
K = $ 450.00
h = $ 2.00  
Period, j    1    2    3    4    5   6    7    8   9
D_j        100   79  230  105    3  10   99  126  40
c_j        120  200  200  400  300  50  120   50  30
==================================================
Step 1 - Initialization
--------------------------------------------------
Created subproblem P and added it to the AL.
Set sigma=None, g(P)=None, g*=1e+99
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P]
Removing P from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=9
Created subproblem P9.

3.1) Property 1: 10 > 688?
3.2) g(P)=450, d_sig=10
3.3) Property 2: 450 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P9. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=8
Created subproblem P8.

3.1) Property 1: 116 > 764?
3.2) g(P)=530, d_sig=116
3.3) Property 2: 530 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P8. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=7
Created subproblem P7.

3.1) Property 1: 145 > 743?
3.2) g(P)=862, d_sig=145
3.3) Property 2: 862 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P7. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P6.

3.1) Property 1: 225 > 703?
3.2) g(P)=1392, d_sig=225
3.3) Property 2: 1392 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P6. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P5.

3.1) Property 1: 0 > 406?
3.2) g(P)=1942, d_sig=0
3.3) Property 2: 1942 > 1e+99?
3.4) Check if the subproblem can be dominated.
P56 dominates P5: 1842 < 1942. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P4.

3.1) Property 1: 0 > 111?
3.2) g(P)=2498, d_sig=0
3.3) Property 2: 2498 > 1e+99?
3.4) Check if the subproblem can be dominated.
P45 dominates P4: 2392 < 2498. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P3.

3.1) Property 1: 413 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P7, P6]
Removing P6 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P56.

3.1) Property 1: 0 > 406?
3.2) g(P)=1842, d_sig=0
3.3) Property 2: 1842 > 1e+99?
3.4) Check if the subproblem can be dominated.
P57 dominates P56: 1332 < 1842. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P46.

3.1) Property 1: 0 > 111?
3.2) g(P)=1848, d_sig=0
3.3) Property 2: 1848 > 1e+99?
3.4) Check if the subproblem can be dominated.
P47 dominates P46: 1358 < 1848. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P36.

3.1) Property 1: 363 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P7]
Removing P7 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P67.

3.1) Property 1: 105 > 703?
3.2) g(P)=1312, d_sig=105
3.3) Property 2: 1312 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P67. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P57.

3.1) Property 1: 0 > 406?
3.2) g(P)=1332, d_sig=0
3.3) Property 2: 1332 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P57. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P47.

3.1) Property 1: 0 > 111?
3.2) g(P)=1358, d_sig=0
3.3) Property 2: 1358 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P47. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P37.

3.1) Property 1: 293 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P67, P57, P47]
Removing P47 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P347.

3.1) Property 1: 0 > 141?
3.2) g(P)=1808, d_sig=0
3.3) Property 2: 1808 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P347. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=2
Created subproblem P247.

3.1) Property 1: 0 > 20?
3.2) g(P)=2268, d_sig=0
3.3) Property 2: 2268 > 1e+99?
3.4) Check if the subproblem can be dominated.
P2347 dominates P247: 2258 < 2268. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P147.

3.1) Property 1: 152 > 0?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P67, P57, P347]
Removing P347 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=2
Created subproblem P2347.

3.1) Property 1: 0 > 20?
3.2) g(P)=2258, d_sig=0
3.3) Property 2: 2258 > 1e+99?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P2347. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P1347.

3.1) Property 1: 0 > 0?
3.2) g(P)=2416, d_sig=0
t = 1. Go to step 4.
==================================================
 Step 4 - Complete Schedule
--------------------------------------------------
P1347 is more optimal: 2416 < 1e+99
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P67, P57, P2347]
Removing P2347 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P12347.

3.1) Property 1: 0 > 0?
3.2) g(P)=2708, d_sig=0
t = 1. Go to step 4.
==================================================
 Step 4 - Complete Schedule
--------------------------------------------------
P12347 is not optimal: 2708 !< 2416
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P67, P57]
Removing P57 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P457.

3.1) Property 1: 0 > 111?
3.2) g(P)=1782, d_sig=0
3.3) Property 2: 1782 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P457: 1358 < 1782. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P357.

3.1) Property 1: 0 > 141?
3.2) g(P)=1992, d_sig=0
3.3) Property 2: 1992 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P157.

3.1) Property 1: 252 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P347 dominates P357: 1808 < 1992. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=2
Created subproblem P257.

3.1) Property 1: 72 > 20?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8, P67]
Removing P67 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P567.

3.1) Property 1: 0 > 406?
3.2) g(P)=1762, d_sig=0
3.3) Property 2: 1762 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P567: 1332 < 1762. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P467.

3.1) Property 1: 0 > 111?
3.2) g(P)=1768, d_sig=0
3.3) Property 2: 1768 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P467: 1358 < 1768. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P367.

3.1) Property 1: 243 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P8]
Removing P8 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=7
Created subproblem P78.

3.1) Property 1: 95 > 743?
3.2) g(P)=980, d_sig=95
3.3) Property 2: 980 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P78. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P68.

3.1) Property 1: 175 > 703?
3.2) g(P)=1178, d_sig=175
3.3) Property 2: 1178 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P68. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P58.

3.1) Property 1: 0 > 406?
3.2) g(P)=1396, d_sig=0
3.3) Property 2: 1396 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P58: 1332 < 1396. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P48.

3.1) Property 1: 0 > 111?
3.2) g(P)=1620, d_sig=0
3.3) Property 2: 1620 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P48: 1358 < 1620. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P38.

3.1) Property 1: 363 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P78, P68]
Removing P68 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P568.

3.1) Property 1: 0 > 406?
3.2) g(P)=1628, d_sig=0
3.3) Property 2: 1628 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P568: 1332 < 1628. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P468.

3.1) Property 1: 0 > 111?
3.2) g(P)=1634, d_sig=0
3.3) Property 2: 1634 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P468: 1358 < 1634. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P368.

3.1) Property 1: 313 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P78]
Removing P78 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P678.

3.1) Property 1: 55 > 703?
3.2) g(P)=1430, d_sig=55
3.3) Property 2: 1430 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P678. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P578.

3.1) Property 1: 0 > 406?
3.2) g(P)=1450, d_sig=0
3.3) Property 2: 1450 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P578: 1332 < 1450. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P478.

3.1) Property 1: 0 > 111?
3.2) g(P)=1476, d_sig=0
3.3) Property 2: 1476 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P478: 1358 < 1476. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P378.

3.1) Property 1: 243 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9, P678]
Removing P678 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P5678.

3.1) Property 1: 0 > 406?
3.2) g(P)=1880, d_sig=0
3.3) Property 2: 1880 > 1966?
3.4) Check if the subproblem can be dominated.
P56 dominates P5678: 1842 < 1880. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P4678.

3.1) Property 1: 0 > 111?
3.2) g(P)=1886, d_sig=0
3.3) Property 2: 1886 > 1966?
3.4) Check if the subproblem can be dominated.
P46 dominates P4678: 1848 < 1886. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P3678.

3.1) Property 1: 193 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P9]
Removing P9 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=8
Created subproblem P89.

3.1) Property 1: 86 > 764?
3.2) g(P)=900, d_sig=86
3.3) Property 2: 900 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P89. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=7
Created subproblem P79.

3.1) Property 1: 115 > 743?
3.2) g(P)=1152, d_sig=115
3.3) Property 2: 1152 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P79. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P69.

3.1) Property 1: 195 > 703?
3.2) g(P)=1602, d_sig=195
3.3) Property 2: 1602 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P69. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P59.

3.1) Property 1: 0 > 406?
3.2) g(P)=2072, d_sig=0
3.3) Property 2: 2072 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P19.

3.1) Property 1: 642 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P56 dominates P59: 1842 < 2072. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P49.

3.1) Property 1: 0 > 111?
3.2) g(P)=2548, d_sig=0
3.3) Property 2: 2548 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P19.

3.1) Property 1: 642 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P45 dominates P49: 2392 < 2548. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P39.

3.1) Property 1: 383 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P89, P79, P69]
Removing P69 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P569.

3.1) Property 1: 0 > 406?
3.2) g(P)=2052, d_sig=0
3.3) Property 2: 2052 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P169.

3.1) Property 1: 592 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P56 dominates P569: 1842 < 2052. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P469.

3.1) Property 1: 0 > 111?
3.2) g(P)=2058, d_sig=0
3.3) Property 2: 2058 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P169.

3.1) Property 1: 592 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P46 dominates P469: 1848 < 2058. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P369.

3.1) Property 1: 333 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P89, P79]
Removing P79 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P679.

3.1) Property 1: 75 > 703?
3.2) g(P)=1602, d_sig=75
3.3) Property 2: 1602 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P679. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P579.

3.1) Property 1: 0 > 406?
3.2) g(P)=1622, d_sig=0
3.3) Property 2: 1622 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P579: 1332 < 1622. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P479.

3.1) Property 1: 0 > 111?
3.2) g(P)=1648, d_sig=0
3.3) Property 2: 1648 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P479: 1358 < 1648. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P379.

3.1) Property 1: 263 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P89, P679]
Removing P679 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P5679.

3.1) Property 1: 0 > 406?
3.2) g(P)=2052, d_sig=0
3.3) Property 2: 2052 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P1679.

3.1) Property 1: 472 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P56 dominates P5679: 1842 < 2052. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P4679.

3.1) Property 1: 0 > 111?
3.2) g(P)=2058, d_sig=0
3.3) Property 2: 2058 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P1679.

3.1) Property 1: 472 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P46 dominates P4679: 1848 < 2058. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P3679.

3.1) Property 1: 213 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P89]
Removing P89 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=7
Created subproblem P789.

3.1) Property 1: 65 > 743?
3.2) g(P)=1350, d_sig=65
3.3) Property 2: 1350 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P789. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P689.

3.1) Property 1: 145 > 703?
3.2) g(P)=1548, d_sig=145
3.3) Property 2: 1548 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P689. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P589.

3.1) Property 1: 0 > 406?
3.2) g(P)=1766, d_sig=0
3.3) Property 2: 1766 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P589: 1332 < 1766. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P489.

3.1) Property 1: 0 > 111?
3.2) g(P)=1990, d_sig=0
3.3) Property 2: 1990 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P189.

3.1) Property 1: 592 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P46 dominates P489: 1848 < 1990. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P389.

3.1) Property 1: 333 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P789, P689]
Removing P689 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P5689.

3.1) Property 1: 0 > 406?
3.2) g(P)=1998, d_sig=0
3.3) Property 2: 1998 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P1689.

3.1) Property 1: 542 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P56 dominates P5689: 1842 < 1998. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P4689.

3.1) Property 1: 0 > 111?
3.2) g(P)=2004, d_sig=0
3.3) Property 2: 2004 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P1689.

3.1) Property 1: 542 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P46 dominates P4689: 1848 < 2004. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P3689.

3.1) Property 1: 283 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P789]
Removing P789 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=6
Created subproblem P6789.

3.1) Property 1: 25 > 703?
3.2) g(P)=1800, d_sig=25
3.3) Property 2: 1800 > 1966?
3.4) Check if the subproblem can be dominated.
3.5) Failed to eliminate P6789. Adding to the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P5789.

3.1) Property 1: 0 > 406?
3.2) g(P)=1820, d_sig=0
3.3) Property 2: 1820 > 1966?
3.4) Check if the subproblem can be dominated.
P57 dominates P5789: 1332 < 1820. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P4789.

3.1) Property 1: 0 > 111?
3.2) g(P)=1846, d_sig=0
3.3) Property 2: 1846 > 1966?
3.4) Check if the subproblem can be dominated.
P47 dominates P4789: 1358 < 1846. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P3789.

3.1) Property 1: 213 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: [P6789]
Removing P6789 from the AL.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=5
Created subproblem P56789.

3.1) Property 1: 0 > 406?
3.2) g(P)=2250, d_sig=0
3.3) Property 2: 2250 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P16789.

3.1) Property 1: 422 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P56 dominates P56789: 1842 < 2250. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=4
Created subproblem P46789.

3.1) Property 1: 0 > 111?
3.2) g(P)=2256, d_sig=0
3.3) Property 2: 2256 > 1966?
Subproblem not optimal. Go to step 3.1
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=1
Created subproblem P16789.

3.1) Property 1: 422 > 0?
Infeasible. Go back to step 2.
3.4) Check if the subproblem can be dominated.
P46 dominates P46789: 1848 < 2256. Go to step 3.1.
==================================================
Step 3 - Decomposition Loop
--------------------------------------------------
t=3
Created subproblem P36789.

3.1) Property 1: 163 > 141?
Infeasible. Go back to step 2.
==================================================
Step 2 - Termination Check
--------------------------------------------------
AL: []
STOP, the AL is empty.

The optimal solution is P1347 with cost $2416.
==================================================
```

