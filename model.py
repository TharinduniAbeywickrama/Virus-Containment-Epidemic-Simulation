#The Initial One
# from mesa import Agent, Model
# from mesa.time import RandomActivation
# from mesa.space import MultiGrid
# from mesa.datacollection import DataCollector
# from agents import HumanAgent, HealthWorkerAgent, ResearcherAgent, PolicyMakerAgent, VirusAgent
# import random


# class EpidemicModel(Model):
#     """Model for simulating epidemic spread with multiple agent types."""

#     def __init__(self, width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents):
#         """Initialize the model, creating the grid, agents, and scheduler."""
        
#         self.num_agents = num_humans + num_health_workers + num_researchers + num_policy_makers + num_virus_agents
#         self.grid = MultiGrid(width, height, True)  # Set up a grid with periodic boundary
#         self.schedule = RandomActivation(self)  # Randomly activate agents each step
        
#         # Create human agents
#         for i in range(num_humans):
#             a = HumanAgent(i, self)
#             self.schedule.add(a)
#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#         # Create health worker agents
#         for i in range(num_health_workers):
#             a = HealthWorkerAgent(i + num_humans, self)
#             self.schedule.add(a)
#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#         # Create researcher agents
#         for i in range(num_researchers):
#             a = ResearcherAgent(i + num_humans + num_health_workers, self)
#             self.schedule.add(a)
#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#         # Create policy maker agents
#         for i in range(num_policy_makers):
#             a = PolicyMakerAgent(i + num_humans + num_health_workers + num_researchers, self)
#             self.schedule.add(a)
#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#         # Create virus agents
#         for i in range(num_virus_agents):
#             a = VirusAgent(i + num_humans + num_health_workers + num_researchers + num_policy_makers, self)
#             self.schedule.add(a)
#             x = self.random.randrange(self.grid.width)
#             y = self.random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#         # Data collector for tracking the model's state
#         self.datacollector = DataCollector(
#             agent_reporters={
#                 "Health Status": lambda a: getattr(a, "health_status", None),  # Safely collect health_status if it exists
#                 "Type": lambda a: type(a).__name__,  # Collect agent type for tracking
#             }
#         )

#     def step(self):
#         """Advance the model by one step."""
#         self.datacollector.collect(self)  # Collect data for the step
        
#         # Perform the agent actions for this step
#         self.schedule.step()

#     def get_agent_data(self):
#         """Retrieve data collected about agents (e.g., health status)."""
#         return self.datacollector.get_agent_vars_dataframe()
#The Initial One

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from agents.human_agent import HumanAgent
from agents.health_worker_agent import HealthWorkerAgent
from agents.researcher_agent import ResearcherAgent
from agents.policy_maker_agent import PolicyMakerAgent
from agents.virus_agent import VirusAgent
import random

class EpidemicModel(Model):
    """Model for simulating epidemic spread with multiple agent types."""

    def __init__(self, width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents):
        self.num_agents = num_humans + num_health_workers + num_researchers + num_policy_makers + num_virus_agents
        self.grid = MultiGrid(width, height, True)  # Set up a grid with periodic boundary
        self.schedule = RandomActivation(self)  # Randomly activate agents each step

        # Initialize current_id for agent creation
        self.current_id = 0
        
        # Create agents
        self.create_agents(HumanAgent, num_humans)
        self.create_agents(HealthWorkerAgent, num_health_workers)
        self.create_agents(ResearcherAgent, num_researchers)
        self.create_agents(PolicyMakerAgent, num_policy_makers)
        self.create_agents(VirusAgent, num_virus_agents)

        # Data collector for tracking the model's state
        self.datacollector = DataCollector(
            model_reporters={
                "Infected": lambda m: self.count_health_status("infected"),
                "Recovered": lambda m: self.count_health_status("recovered"),
                "Susceptible": lambda m: self.count_health_status("susceptible"),
            },
            agent_reporters={
                "Health Status": lambda a: getattr(a, "health_status", None),
                "Type": lambda a: type(a).__name__,
            }
        )

    def create_agents(self, agent_class, num_agents):
        for i in range(num_agents):
            agent = agent_class(self.next_id(), self)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def next_id(self):
        """Generate the next unique ID for an agent."""
        self.current_id += 1
        return self.current_id

    def count_health_status(self, status):
        """Count the number of agents with a specific health status."""
        return sum(1 for agent in self.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == status)

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)  # Collect data for the step
        self.schedule.step()

    def get_agent_data(self):
        """Retrieve data collected about agents (e.g., health status)."""
        return self.datacollector.get_agent_vars_dataframe()

    def get_model_data(self):
        """Retrieve data collected at the model level (e.g., counts of infected)."""
        return self.datacollector.get_model_vars_dataframe()




