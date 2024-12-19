from agents.human_agent import HumanAgent
from mesa import Agent
import random

class VirusAgent(Agent):
    """ A virus agent responsible for spreading and evolving. """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.infectivity_rate = random.uniform(0.1, 0.3)
        self.mutation_probability = 0.05
        
    def step(self):
        self.spread_infection()
        self.mutate_if_necessary()

    def spread_infection(self):
        susceptible_humans = [agent for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "susceptible"]
        for human in susceptible_humans:
            if random.random() < self.infectivity_rate:   # A single infected agent spreads the virus
                human.health_status = "infected"
    
    def mutate_if_necessary(self):
        if random.random() < self.mutation_probability:
            self.infectivity_rate = random.uniform(0.2, 0.5)
            self.mutation_probability = random.uniform(0.05, 0.1)
