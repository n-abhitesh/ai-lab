import numpy as np

num_states = 10
num_actions = 2
gamma = 0.6

V = np.zeros(num_states)

def policy_evaluation(policy):
    for state in range(num_states):
        action = policy[state]
        next_state = (state + action) % num_states
        reward = np.random.rand()
        V[state] = reward + gamma * V[next_state]

def policy_improvement():
    policy = np.zeros(num_states, dtype=int)
    for state in range(num_states):
        q_values = np.zeros(num_actions)
        for action in range(num_actions):
            next_state = (state + action) % num_states
            reward = np.random.rand()
            q_values[action] = reward + gamma * V[next_state]
        policy[state] = np.argmax(q_values)
    return policy

policy = np.zeros(num_states, dtype=int)
for _ in range(100):  
    policy_evaluation(policy)
    policy = policy_improvement()

print("Final policy:", policy)
print("Value function:", V)
