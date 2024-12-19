import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import EpidemicModel
from agents.human_agent import HumanAgent
from agents.health_worker_agent import HealthWorkerAgent
from agents.researcher_agent import ResearcherAgent
from agents.policy_maker_agent import PolicyMakerAgent

# Initialize the main application window
root = tk.Tk()
root.title("Multi-Agent Epidemic Simulation")

# Input Parameters Section
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(input_frame, text="Simulation Parameters", font=("Arial", 14)).pack()

# Create input fields for parameters
params = {
    "num_humans": tk.IntVar(value=100),
    "num_health_workers": tk.IntVar(value=10),
    "num_researchers": tk.IntVar(value=5),
    "num_policy_makers": tk.IntVar(value=10),
    "num_virus_agents": tk.IntVar(value=1)
}

for param, var in params.items():
    frame = tk.Frame(input_frame)
    frame.pack(fill=tk.X, pady=5)
    tk.Label(frame, text=param.replace("_", " ").capitalize() + ":", width=20, anchor="w").pack(side=tk.LEFT)
    tk.Entry(frame, textvariable=var).pack(side=tk.LEFT, padx=5)

# Add a start button
start_button = tk.Button(input_frame, text="Start Simulation", font=("Arial", 12))
start_button.pack(pady=20)

# Visualization Section
viz_frame = tk.Frame(root)
viz_frame.pack(side=tk.RIGHT, padx=20, pady=20)

fig, axs = plt.subplots(3, 1, figsize=(8, 18))
plt.subplots_adjust(hspace=0.8)  # Adjust spacing between subplots
canvas = FigureCanvasTkAgg(fig, master=viz_frame)
canvas.get_tk_widget().pack()

# Define color mapping for health statuses
status_colors = {
    "susceptible": "green",  # Healthy agents
    "infected": "red",       # Infected agents
    "recovered": "blue"      # Recovered agents
}

def start_simulation():
    # Get parameter values from the UI
    width, height = 20, 20
    num_humans = params["num_humans"].get()
    num_health_workers = params["num_health_workers"].get()
    num_researchers = params["num_researchers"].get()
    num_policy_makers = params["num_policy_makers"].get()
    num_virus_agents = params["num_virus_agents"].get()

    # Initialize the Epidemic Model
    model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)

    # Prepare lists to track metrics
    steps, infected_counts, recovered_counts, susceptible_counts = [], [], [], []
    treated_counts, strategies_updated, policies_enforced = [], [], []

    # Run the model for a set number of steps
    for step in range(100):
        model.step()
        steps.append(step + 1)

        # Metrics for each agent type
        infected_this_step, recovered_this_step, susceptible_this_step = 0, 0, 0
        treated_this_step, strategies_this_step, policies_this_step = 0, 0, 0

        x_positions, y_positions, colors = [], [], []

        for agent in model.schedule.agents:
            if isinstance(agent, HumanAgent):
                x, y = agent.pos
                x_positions.append(x)
                y_positions.append(y)
                colors.append(status_colors[agent.health_status])
                if agent.health_status == "infected":
                    infected_this_step += 1
                elif agent.health_status == "recovered":
                    recovered_this_step += 1
                else:
                    susceptible_this_step += 1
            elif isinstance(agent, HealthWorkerAgent):
                treated_this_step += agent.capacity
            elif isinstance(agent, ResearcherAgent):
                strategies_this_step += agent.research_level
            elif isinstance(agent, PolicyMakerAgent):
                policies_this_step += agent.policy_effectiveness

        # Append metrics
        infected_counts.append(infected_this_step)
        recovered_counts.append(recovered_this_step)
        susceptible_counts.append(susceptible_this_step)
        treated_counts.append(treated_this_step)
        strategies_updated.append(strategies_this_step)
        policies_enforced.append(policies_this_step)

        # Update scatter plot
        axs[0].clear()
        axs[0].scatter(x_positions, y_positions, c=colors, s=50, alpha=0.8)
        axs[0].set_xlabel("X Position")
        axs[0].set_ylabel("Y Position")
        axs[0].set_title(f"Human Agent Movement and Health Status)\n"
                         f"Infected: {infected_this_step}, Recovered: {recovered_this_step}, Susceptible: {susceptible_this_step}")
        axs[0].set_xlim(0, width)
        axs[0].set_ylim(0, height)
        axs[0].legend(handles=[
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Infected'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Susceptible'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Recovered')
        ], title="Health Status", loc="upper right")

        # Update line plot for agent actions
        axs[1].clear()
        axs[1].plot(steps, treated_counts, label="Infected Treated", color="blue")
        axs[1].plot(steps, strategies_updated, label="Strategies Updated", color="green")
        axs[1].plot(steps, policies_enforced, label="Policies Enforced", color="orange")
        axs[1].set_title("Actions by Agents")
        axs[1].legend()

        # Update health status line plot
        axs[2].clear()
        axs[2].plot(steps, infected_counts, label="Infected", color="red")
        axs[2].plot(steps, recovered_counts, label="Recovered", color="blue")
        axs[2].plot(steps, susceptible_counts, label="Susceptible", color="green")
        axs[2].set_title("Health Status Over Time")
        axs[2].legend()

        # Update the canvas
        canvas.draw()
        root.update_idletasks()

# Connect the start button to the start_simulation function
start_button.config(command=start_simulation)

# Run the Tkinter event loop
root.mainloop()

