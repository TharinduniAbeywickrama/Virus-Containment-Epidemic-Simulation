# import streamlit as st
# from model import EpidemicModel
# import matplotlib.pyplot as plt

# # Sidebar for parameter input
# st.sidebar.header("Simulation Parameters")
# width = st.sidebar.slider("Grid Width", 10, 50, 20)
# height = st.sidebar.slider("Grid Height", 10, 50, 20)
# num_humans = st.sidebar.slider("Number of Humans", 10, 200, 100)
# num_health_workers = st.sidebar.slider("Number of Health Workers", 1, 20, 5)
# num_researchers = st.sidebar.slider("Number of Researchers", 1, 10, 2)
# num_policy_makers = st.sidebar.slider("Number of Policy Makers", 1, 10, 2)
# num_virus_agents = st.sidebar.slider("Number of Virus Agents", 1, 5, 1)
# steps = st.sidebar.slider("Number of Steps", 10, 500, 100)

# # Button to start simulation
# if st.sidebar.button("Run Simulation"):
#     # Run the simulation with parameters from the UI
#     model = EpidemicModel(width, height, num_humans, num_health_workers, num_researchers, num_policy_makers, num_virus_agents)
    
#     # Store results after each step
#     for _ in range(steps):
#         model.step()
    
#     # Collect simulation data
#     agent_data = model.get_agent_data()
    
#     # Visualization
#     st.write("Simulation Results")
#     health_counts = agent_data['Health Status'].value_counts()
#     st.line_chart(health_counts)
