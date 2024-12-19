from mesa import Agent
import random

class HumanAgent(Agent):
    """ A human agent with health status, immunity, and behavior. """
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.health_status = "susceptible"  # can be 'susceptible', 'infected', 'recovered'
        self.immunity_level = 0  # 0 to 100 (percentage immunity)
        self.mobility_rate = random.uniform(0.5, 1.5)  # Random mobility rate
        self.compliance_level = random.uniform(0.0, 1.0)  # Mask-wearing behavior
        
    def step(self):
        if self.health_status == "susceptible":
            self.move()
            self.interact_with_others()
        elif self.health_status == "infected":
            self.spread_infection()
        elif self.health_status == "recovered":
            self.move()
        
    def move(self):
        x, y = self.pos
        new_pos = (x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1]))
        self.model.grid.move_agent(self, new_pos)
        
    def interact_with_others(self):
        nearby_agents = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        for agent in nearby_agents:
            if isinstance(agent, HumanAgent) and agent.health_status == "infected":
                if random.random() < 0.1:
                    self.health_status = "infected"
                    
    def spread_infection(self):
        nearby_agents = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        for agent in nearby_agents:
            if isinstance(agent, HumanAgent) and agent.health_status == "susceptible":
                if random.random() < 0.2:
                    agent.health_status = "infected"
