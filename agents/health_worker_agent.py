from agents.human_agent import HumanAgent
from mesa import Agent
import random

class HealthWorkerAgent(Agent):
    """ A health worker agent responsible for testing and treating humans. """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.capacity = random.randint(5, 10)  # Can treat 5-10 people per day
        
    def step(self):
        self.test_and_treat()

    def test_and_treat(self):
        infected_humans = [agent for agent in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
                           if isinstance(agent, HumanAgent) and agent.health_status == "infected"]
        for human in infected_humans:
            if self.capacity > 0:
                human.health_status = "recovered"
                self.capacity -= 1
