#with scatter plot
import matplotlib.pyplot as plt
from model import EpidemicModel
from agents.human_agent import HumanAgent
from agents.health_worker_agent import HealthWorkerAgent
from agents.researcher_agent import ResearcherAgent
from agents.policy_maker_agent import PolicyMakerAgent

# Parameters for the simulation
width = 20
height = 20
num_humans = 100
num_health_workers = 10
num_researchers = 5
num_policy_makers = 10
num_virus_agents = 1

# Create the model instance
model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)

# Initialize the plot with three subplots (scatter plot, line plot, and health status line plot)
plt.ion()  # Turn on interactive mode
fig, axs = plt.subplots(3, 1, figsize=(8, 18))  # Create a 3-row layout for plots

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.8)  # Increase the vertical space between the plots

# Define color mapping for health statuses
status_colors = {
    "susceptible": "green",  # Healthy agents
    "infected": "red",       # Infected agents
    "recovered": "blue"      # Recovered agents
}

# Prepare lists to track additional data
steps = []
treated_counts = []  # Number of infected agents treated by Health Workers
strategies_updated = []  # Number of updates made by Researchers
policies_enforced = []  # Number of policies enforced by Policy Makers
infected_counts = []  # Number of infected agents over time
recovered_counts = []  # Number of recovered agents over time
susceptible_counts = []  # Number of susceptible agents over time

# Run the model for a set number of steps (e.g., 100 steps)
for step in range(100):
    model.step()  # Advance the model by one step
    steps.append(step + 1)

    # Retrieve positions and health statuses of Human Agents
    x_positions = []
    y_positions = []
    colors = []

    # Track metrics
    treated_this_step = 0
    strategies_this_step = 0
    policies_this_step = 0
    infected_this_step = 0
    recovered_this_step = 0
    susceptible_this_step = 0

    for agent in model.schedule.agents:
        if isinstance(agent, HumanAgent):
            x, y = agent.pos
            x_positions.append(x)
            y_positions.append(y)
            colors.append(status_colors[agent.health_status])  # Map health status to color
            # Count the number of agents in each health status
            if agent.health_status == "infected":
                infected_this_step += 1
            elif agent.health_status == "recovered":
                recovered_this_step += 1
            else:
                susceptible_this_step += 1
        elif isinstance(agent, HealthWorkerAgent):
            treated_this_step += agent.capacity  # Track the number of treatments available
        elif isinstance(agent, ResearcherAgent):
            strategies_this_step += agent.research_level  # Track research updates
        elif isinstance(agent, PolicyMakerAgent):
            policies_this_step += agent.policy_effectiveness  # Track policy actions

    # Append metrics to tracking lists
    treated_counts.append(treated_this_step)
    strategies_updated.append(strategies_this_step)
    policies_enforced.append(policies_this_step)
    infected_counts.append(infected_this_step)
    recovered_counts.append(recovered_this_step)
    susceptible_counts.append(susceptible_this_step)

    # Clear and update the scatter plot (top plot)
    axs[0].clear()
    scatter = axs[0].scatter(x_positions, y_positions, c=colors, s=50, alpha=0.8)

    axs[0].set_xlabel("X Position")
    axs[0].set_ylabel("Y Position")
    axs[0].set_title(f"Human Agent Movement and Health Status)\n"
                     f"Infected: {infected_this_step}, Recovered: {recovered_this_step}, Susceptible: {susceptible_this_step}")
    axs[0].set_xlim(0, width)
    axs[0].set_ylim(0, height)

    # Add a legend for the color mapping of health statuses
    axs[0].legend(handles=[
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Infected'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Susceptible'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Recovered')
    ], title="Health Status", loc="upper right")

    # Clear and update the line plot (middle plot)
    axs[1].clear()
    axs[1].plot(steps, treated_counts, label="Infected Treated", color="blue")
    axs[1].plot(steps, strategies_updated, label="Strategies Updated", color="green")
    axs[1].plot(steps, policies_enforced, label="Policies Enforced", color="orange")
    axs[1].set_xlabel("Steps")
    axs[1].set_ylabel("Actions")
    axs[1].set_title(f"Health Worker, Researcher, and Policy Maker Actions\n"
                     f"Infected Treated: {treated_this_step}, Strategies Updated: {strategies_this_step}, Policies Enforced: {policies_this_step}")
    axs[1].legend()

    # Clear and update the health status line plot (bottom plot)
    axs[2].clear()
    axs[2].plot(steps, infected_counts, label="Infected", color="red")
    axs[2].plot(steps, recovered_counts, label="Recovered", color="blue")
    axs[2].plot(steps, susceptible_counts, label="Susceptible", color="green")
    axs[2].set_xlabel("Steps")
    axs[2].set_ylabel("Number of Agents")
    axs[2].set_title(f"Health Status Counts Over Time\n"
                     f"Infected: {infected_this_step}, Recovered: {recovered_this_step}, Susceptible: {susceptible_this_step}")
    axs[2].legend()

    # Pause to update the plots dynamically
    plt.pause(0.1)

# Turn off interactive mode after finishing the simulation
plt.ioff()
plt.show()
