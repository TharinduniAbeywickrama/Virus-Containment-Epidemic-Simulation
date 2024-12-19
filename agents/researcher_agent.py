from agents.human_agent import HumanAgent
from mesa import Agent
import random

class ResearcherAgent(Agent):
    """ A researcher agent that updates containment strategies and develops vaccines. """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.research_level = random.randint(1, 10)
        
    def step(self):
        self.analyze_infection_trends()
        self.update_containment_strategy()

    def analyze_infection_trends(self):
        infected_count = sum(1 for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "infected")
        if infected_count > 50:
            self.research_level += 1

    def update_containment_strategy(self):
        if self.research_level > 5:
            print(f"Researcher {self.unique_id}: Developing a new vaccine strategy!")
