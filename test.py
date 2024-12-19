#Dynamic Line Plot
import matplotlib.pyplot as plt
from model import EpidemicModel  # Import your EpidemicModel class

# Parameters for the simulation
width = 20
height = 20
num_humans = 100
num_health_workers = 3
num_researchers = 1
num_policy_makers = 1
num_virus_agents = 10

# Create the model instance
model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

# Run the model for a set number of steps (200 steps in this case)
for i in range(100):
    model.step()

    # Collect agent data after each step
    agent_data = model.get_agent_data()

    # Clear the previous plot and plot the updated data as a line plot
    ax.clear()

    # Get the counts of health statuses (Infected, Recovered, Susceptible)
    health_counts = agent_data['Health Status'].value_counts()

    # Plotting the trends of each health status
    for status in health_counts.index:
        status_counts = agent_data[agent_data['Health Status'] == status].groupby('Step').size()
        ax.plot(status_counts.index, status_counts.values, label=status)

    ax.set_xlabel('Step')
    ax.set_ylabel('Number of Agents')
    ax.set_title(f'Health Status Distribution Over Time')
    ax.legend()  # Add a legend to differentiate between statuses

    # Pause to update the plot
    plt.pause(0.1)

# Turn off interactive mode after finishing the simulation
plt.ioff()
plt.show()
