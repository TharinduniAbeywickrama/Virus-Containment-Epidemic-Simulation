#Dynamic Bar plot
from model import EpidemicModel
import matplotlib.pyplot as plt

# Parameters
width = 20
height = 20
num_humans = 100
num_health_workers = 10
num_researchers = 5
num_policy_makers = 10
num_virus_agents = 1

# Create model instance
model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

# Run the model for a set number of steps
for i in range(200):
    model.step()

    # Collect agent data after each step
    agent_data = model.get_agent_data()

    # Clear the previous plot and plot the updated data
    ax.clear()
    ax.plot(agent_data['Health Status'].value_counts())  # This will give you counts of health status over time
    ax.set_xlabel('Health Status')
    ax.set_ylabel('Number of Agents')
    ax.set_title(f'Health Status Distribution at Step {i+1}')
    plt.pause(0.1)  # Pause for a brief moment to update the plot

# Turn off interactive mode
plt.ioff()
plt.show()
