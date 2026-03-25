import random

# States
states = ["A", "B", "Goal"]

# Actions
actions = ["move"]

# Transition probabilities
transitions = {
    "A": {"A": 0.2, "B": 0.6, "Goal": 0.2},
    "B": {"A": 0.3, "B": 0.3, "Goal": 0.4},
    "Goal": {"Goal": 1.0}
}

# Rewards
rewards = {
    "A": -1,
    "B": -1,
    "Goal": 10
}

# Start state
state = "A"

for step in range(5):
    print("State:", state)

    # Choose next state based on probability
    rand = random.random()
    total = 0

    for next_state, prob in transitions[state].items():
        total += prob
        if rand <= total:
            state = next_state
            break

    print("Reward:", rewards[state])
