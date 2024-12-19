from agents.human_agent import HumanAgent
from mesa import Agent
import random

class PolicyMakerAgent(Agent):
    """ A policy maker agent who sets containment policies such as lockdowns. """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.policy_effectiveness = random.uniform(0.5, 1.0)
        self.economic_balance = random.uniform(0.2, 0.8)
    
    def step(self):
        self.enforce_policy()

    def enforce_policy(self):
        infected_count = sum(1 for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "infected")
        if infected_count > 50:
            self.policy_effectiveness = min(self.policy_effectiveness + 0.1, 1.0)
            print(f"Policy Maker {self.unique_id}: Implementing stronger lockdown!")
        else:
            self.policy_effectiveness = max(self.policy_effectiveness - 0.1, 0.5)
