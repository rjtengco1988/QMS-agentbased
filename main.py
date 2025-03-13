import numpy as np # import numpy
import matplotlib.pyplot as plt # import matplotlib

population = 10000 # number of population
days = 100 # days of simulation
infection_prob = 0.5 #
recovery_time = 5 #infection take 5 days to recover

people = np.zeros(population) # initialize population 0 = susceptible, 1 = infected, 2 = recovered
people[np.random.randint(0, population)] = 1  # Start with one infected
history = [] # list store history of infection

for day in range(days): # Loop through each day in the simulation
    new_people = people.copy() # Create a copy to update changes without affecting the current state
    for i in range(population): # Iterate through each individual
        if people[i] == 1:
            if np.random.rand() < (1/recovery_time): # Random chance of recovery (1/recovery_time probability)
                new_people[i] = 2  # Recovered
            else:
                for _ in range(2): # Each infected person attempts to infect two others
                    other = np.random.randint(0, population) # Randomly select another individual
                    if people[other] == 0 and np.random.rand() < infection_prob: # If the selected person is susceptible
                        new_people[other] = 1  # New infection
    people = new_people.copy()
    history.append((sum(people == 0), sum(people == 1), sum(people == 2))) # Store counts of susceptible, infected, and recovered

history = np.array(history) # Convert history list to a NumPy array
plt.plot(history[:,0], label="Susceptible") # Plot susceptible count over time
plt.plot(history[:,1], label="Infected", color="red") # Plot infected count over time
plt.plot(history[:,2], label="Recovered", color="green") # Plot recovered count over time
plt.xlabel("Days") # Label x-axis
plt.ylabel("Population Count") # Label y-axis
plt.title("Epidemic Spread Simulation") # Title of the plot
plt.legend() # Display legend
plt.show() # Show the plot