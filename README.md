# CompPhysProjectThree
## Self-Avoiding Random Walk
One application of a random walk process is to model the average length of a polymer chain made up of N
monomers (a monomer is a molecule such as CH2). To more accurately model such a process it is necessary to
use a self-avoiding walk (SAW). A SAW is not completely random in that the walker is restricted from stepping
on a grid space that the walker has previously been on.
### (a) Write a program that models a SAW in two-dimensions.
Start with an initial step upwards. Generate a random number 1, 2, or 3 corresponding to a step to the left, a step straight ahead, and a step to the right. For each step these directions are relative to the walkers last step. If the step leads to a self-intersection (i.e., a step onto a point the walker has already been on), the walk must be terminated and a new walk begun back at the origin. To record whether a site has previously been stepped on, represent the lattice as a two-dimensional array. Set the array initially equal to zero except for the starting point and the one above it for the initial step up. Set these equal to one. When the walker takes a step, check if the array has a value of 0 or 1. If 0, set that sight equal to 1 and continue the walk. If 1, the walk terminates. Record the fraction of successful walks as a function of the number of steps, f(N).
### (b) What is the qualitative dependence of f(N) on N?
What is the maximum value of N you can reasonably consider? For the values of N that you can reasonably consider, calculate the mean square end-to-end distance, R^2(N) and plot it as a function of N.
### (c) Modify your program to add a weighting procedure.
Weighting procedure developed by Rosenbluth and Rosenbluth that does not throw out as many walks. Before the Nth step the three possible grid points the walker can step to are summed and the total is sN which can be 0, 1, 2, or 3, corresponding to all three steps allowed, two of the three steps allowed, only one of the three steps allowed, and no allowed steps.

sn = 0 → W (N) = W (N − 1)

sn = 1 → W (N) = 2/3 W (N − 1) Take one of the two possible steps.

sn = 2 → W (N) = 1/3 W (N − 1) Take the one possible step.

sn = 3 → W (N) = 0 Terminate the walk. (1)

Calculate the weighted mean of R^2(N) where the sum is over all of the trials. Calculate R^2(N) = N^(2v) (a power law fit) and find your estimate for v.
R^2(N) = sum(Wi(N)Ri^2(N)) / sum(Wi(N))
### (d) Make a movie of your results
