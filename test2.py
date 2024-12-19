#Grid
import time  # Import the time module for adding delay
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import EpidemicModel
from agents.human_agent import HumanAgent

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

fig, ax = plt.subplots(figsize=(8, 8))
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
    width = 20
    height = 20
    num_humans = params["num_humans"].get()
    num_health_workers = params["num_health_workers"].get()
    num_researchers = params["num_researchers"].get()
    num_policy_makers = params["num_policy_makers"].get()
    num_virus_agents = params["num_virus_agents"].get()

    # Initialize the Epidemic Model
    model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)

    for step in range(100):  # Run for 100 steps
        model.step()

        # Retrieve positions and health statuses of Human Agents
        x_positions = []
        y_positions = []
        colors = []

        for agent in model.schedule.agents:
            if isinstance(agent, HumanAgent):
                x, y = agent.pos
                x_positions.append(x)
                y_positions.append(y)
                colors.append(status_colors[agent.health_status])  # Map health status to color

        # Clear and update the grid visualization
        ax.clear()
        ax.scatter(x_positions, y_positions, c=colors, s=50, alpha=0.8)
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_xlabel("X Position")
        ax.set_ylabel("Y Position")
        ax.set_title(f"Human Agent Movement and Health Status (Step {step + 1})")

        # Add a legend for health status colors
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', label='Susceptible', markerfacecolor='green', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Infected', markerfacecolor='red', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Recovered', markerfacecolor='blue', markersize=10),
        ]
        ax.legend(handles=legend_elements, loc='upper right')

        # Update the canvas
        canvas.draw()
        root.update_idletasks()  # Update the GUI

        # Slow down the simulation by adding a delay
        time.sleep(0.5)  # Adjust the delay (in seconds) as needed to slow down the simulation

# Connect the start button to the start_simulation function
start_button.config(command=start_simulation)

# Run the Tkinter event loop
root.mainloop()
