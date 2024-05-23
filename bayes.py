def bayes_theorem(P_A, P_B_given_A, P_B):
    return (P_B_given_A * P_A) / P_B

# Example probabilities
P_A = 0.3  # Probability of event A
P_B_given_A = 0.4  # Probability of event B given A
P_B = 0.5  # Probability of event B

# Calculate P(A|B) using Bayes' Theorem
P_A_given_B = bayes_theorem(P_A, P_B_given_A, P_B)

print("Probability of A given B using Bayes' Theorem:", P_A_given_B)


# Example probabilities
P_A = 0.3  # Probability of event A
P_B = 0.5  # Probability of event B

# Calculate the joint probability of A and B
P_A_and_B = P_A * P_B

print("Joint Probability of A and B:", P_A_and_B)


# Example probabilities
P_A = 0.3  # Probability of event A
P_B = 0.5  # Probability of event B
P_A_and_B = 0.15  # Joint probability of A and B

# Calculate P(A|B)
P_A_given_B = P_A_and_B / P_B

print("Conditional Probability of A given B:", P_A_given_B)
