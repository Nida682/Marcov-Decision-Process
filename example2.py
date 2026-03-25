import random

# States (user behavior)
states = ["Browsing", "Interested", "Buying"]

# Actions (recommendation)
actions = ["show_product"]

# Transition probabilities
transitions = {
    "Browsing": {"Browsing": 0.5, "Interested": 0.4, "Buying": 0.1},
    "Interested": {"Browsing": 0.2, "Interested": 0.5, "Buying": 0.3},
    "Buying": {"Browsing": 0.3, "Buying": 0.7}
}

# Rewards
rewards = {
    "Browsing": 1,
    "Interested": 3,
    "Buying": 10
}

# Start state
state = "Browsing"

for step in range(5):
    print("User State:", state)

    # Choose next state based on probability
    rand = random.random()
    total = 0

    for next_state, prob in transitions[state].items():
        total += prob
        if rand <= total:
            state = next_state
            break

    print("Reward:", rewards[state])
