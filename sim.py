import numpy as np
import seaborn as sns

"""
Simulating an economics game discussed
by Jordan Peterson and Joe Rogan in the
JRE podcast. The premise of the game is
that if you have 100 agents, and they
randomly get paired up. And they flip a coin. 
Depending on the coin flip, if heads agent A
gives some non zero amount of money to agent B
and vice versa. They all start with some money.

The prediction is that, given enough iterations
of this exchange game, a pareto distribution
or more generally a power law distribution
will be observed on the amount of wealth 
the agents have.

This is a probability exercise
to demonstrate that even with equal initial 
conditions, massive inequality of outcomes
is not only possible, but probably inevitible
due to total random luck.
"""

# Declare array of length 100 of arbitray
# starting money, 10 for now
agents = np.full(shape = (50,2),
                 fill_value = 10)

# Place holder third column
agents = np.insert(agents, 2, np.ones((50,)), axis = 1)  

# Simulate the game long term
for _ in range(5000):
    #create a new array with heads (1)
    # or tails (0), with 50% probability
    heads_or_tails = np.random.choice([0,1],
                                      50,
                                      p = [0.5,0.5])
    
    # Make the agent pairs switch cash depending
    # on heads or tails
    agents[:,2] = heads_or_tails
    
    #Randomize the pairs
    np.random.shuffle(agents[:,:2])  
    
    # If heads increase col 0 by 5 
    # and decrease col 1 by 5
    agents[agents[:, 2] == 1, 0] += 5
    agents[agents[:, 2] == 1, 1] -= 5
    
    #If tails increase col 1 by 5
    # and decrease col 0 by 5
    agents[agents[:, 2] == 0, 1] += 5
    agents[agents[:, 2] == 0, 0] -= 5
    
    
# Final money the individuals are left with
final_wealth = agents[:,:2].ravel()
final_wealth = np.sort(final_wealth)

#Plot the final distribution
sns.lineplot(x = np.arange(100), y = final_wealth)


















