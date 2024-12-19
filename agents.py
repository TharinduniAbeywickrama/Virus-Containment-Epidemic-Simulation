# from mesa import Agent
# import random

# # Human Agent Class
# class HumanAgent(Agent):
#     """ A human agent with health status, immunity, and behavior. """
    
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         self.health_status = "susceptible"  # can be 'susceptible', 'infected', 'recovered'
#         self.immunity_level = 0  # 0 to 100 (percentage immunity)
#         self.mobility_rate = random.uniform(0.5, 1.5)  # Random mobility rate
#         self.compliance_level = random.uniform(0.0, 1.0)  # Mask-wearing behavior
        
#     def step(self):
#         """ Human behavior: moves and interacts with others. """
#         if self.health_status == "susceptible":
#             self.move()
#             self.interact_with_others()
        
#         elif self.health_status == "infected":
#             self.spread_infection()
        
#         elif self.health_status == "recovered":
#             self.move()
        
#     def move(self):
#         """ Move randomly or socially based on compliance level. """
#         x, y = self.pos
#         if random.random() < self.compliance_level:
#             # Move randomly (e.g., social distancing)
#             new_pos = (x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1]))
#         else:
#             # Move more freely
#             new_pos = (x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1]))
#         self.model.grid.move_agent(self, new_pos)
        
#     def interact_with_others(self):
#         """ Interact with other humans to potentially get infected. """
#         nearby_agents = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
#         for agent in nearby_agents:
#             if isinstance(agent, HumanAgent) and agent.health_status == "infected":
#                 if random.random() < 0.1:  # 10% chance to be infected
#                     self.health_status = "infected"
                    
#     def spread_infection(self):
#         """ Infected human spreads virus to others. """
#         nearby_agents = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
#         for agent in nearby_agents:
#             if isinstance(agent, HumanAgent) and agent.health_status == "susceptible":
#                 if random.random() < 0.2:  # 20% chance to infect others
#                     agent.health_status = "infected"

# # Health Worker Agent Class
# class HealthWorkerAgent(Agent):
#     """ A health worker agent responsible for testing and treating humans. """
    
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         self.capacity = random.randint(5, 10)  # Can treat 5-10 people per day
        
#     def step(self):
#         """ Health worker's actions for the day: testing and treating. """
#         self.test_and_treat()

#     def test_and_treat(self):
#         """ Health worker tests and treats nearby humans. """
#         infected_humans = [agent for agent in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False) if isinstance(agent, HumanAgent) and agent.health_status == "infected"]
#         for human in infected_humans:
#             if self.capacity > 0:
#                 human.health_status = "recovered"
#                 self.capacity -= 1  # Use up capacity per treatment

# # Researcher Agent Class
# class ResearcherAgent(Agent):
#     """ A researcher agent that updates containment strategies and develops vaccines. """
    
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         self.research_level = random.randint(1, 10)  # Research capability
        
#     def step(self):
#         """ Researcher agent's actions: update research based on infection trends. """
#         self.analyze_infection_trends()
#         self.update_containment_strategy()

#     def analyze_infection_trends(self):
#         """ Analyze current infection trends and develop a vaccine. """
#         infected_count = sum(1 for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "infected")
#         if infected_count > 50:  # If infection rate is high, focus on vaccine development
#             self.research_level += 1

#     def update_containment_strategy(self):
#         """ Update the containment strategy based on current research. """
#         if self.research_level > 5:
#             print(f"Researcher {self.unique_id}: Developing a new vaccine strategy!")

# # Policy Maker Agent Class
# class PolicyMakerAgent(Agent):
#     """ A policy maker agent who sets containment policies such as lockdowns. """
    
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         self.policy_effectiveness = random.uniform(0.5, 1.0)  # 50% to 100% effective
#         self.economic_balance = random.uniform(0.2, 0.8)  # Trade-off between economics and health
    
#     def step(self):
#         """ Policy maker enacts lockdown or adjusts policies. """
#         self.enforce_policy()

#     def enforce_policy(self):
#         """ Enforce lockdowns or restrictions based on the infection rate. """
#         infected_count = sum(1 for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "infected")
#         if infected_count > 50:
#             self.policy_effectiveness = min(self.policy_effectiveness + 0.1, 1.0)
#             print(f"Policy Maker {self.unique_id}: Implementing stronger lockdown!")
#         else:
#             self.policy_effectiveness = max(self.policy_effectiveness - 0.1, 0.5)

# # Virus Agent Class
# class VirusAgent(Agent):
#     """ A virus agent responsible for spreading and evolving. """
    
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)
#         self.infectivity_rate = random.uniform(0.1, 0.3)  # 10%-30% chance of infection
#         self.mutation_probability = 0.05  # 5% chance of mutation
#         self.adaptability = random.uniform(0.5, 1.0)  # Virus adaptability to interventions
        
#     def step(self):
#         """ Virus behavior: spread infection and mutate. """
#         self.spread_infection()
#         self.mutate_if_necessary()

#     def spread_infection(self):
#         """ Virus spreads to nearby susceptible humans. """
#         susceptible_humans = [agent for agent in self.model.schedule.agents if isinstance(agent, HumanAgent) and agent.health_status == "susceptible"]
#         for human in susceptible_humans:
#             if random.random() < self.infectivity_rate:
#                 human.health_status = "infected"
    
#     def mutate_if_necessary(self):
#         """ Virus may mutate and adapt to policies. """
#         if random.random() < self.mutation_probability:
#             self.infectivity_rate = random.uniform(0.2, 0.5)  # Mutation increases infectivity
#             self.mutation_probability = random.uniform(0.05, 0.1)  # Mutation chance may increase

