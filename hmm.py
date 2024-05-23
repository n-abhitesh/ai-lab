states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
transition_probability = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}
emission_probability = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

def forward_algorithm(observed_sequence):
    fwd = [{}]

    # Initialize base cases (t == 0)
    for state in states:
        fwd[0][state] = start_probability[state] * emission_probability[state][observed_sequence[0]]
    
    # Compute forward probabilities for t > 0
    for t in range(1, len(observed_sequence)):
        fwd.append({})
        for state in states:
            fwd[t][state] = sum(fwd[t-1][prev_state] * transition_probability[prev_state][state] * emission_probability[state][observed_sequence[t]] for prev_state in states)
    
    return fwd

observed_sequence = ['walk', 'shop', 'clean']
fwd_probs = forward_algorithm(observed_sequence)

# Print the forward probabilities
for t, probs in enumerate(fwd_probs):
    print(f"Time step {t}: {probs}")
