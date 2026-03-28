import random

def run_simulation(trials=10000):
    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):
        doors = ["car", "goat", "goat"]
        random.shuffle(doors)

        player_choice = random.randrange(3)

        monty_valid = [
            i for i in range(3)
            if i != player_choice and doors[i] != "car"
        ]
        monty_choice = random.choice(monty_valid)

        switch_choice = [
            i for i in range(3)
            if i != player_choice and i != monty_choice
        ][0]

        if doors[player_choice] == "car":
            stay_wins += 1

        if doors[switch_choice] == "car":
            switch_wins += 1

    return stay_wins / trials, switch_wins / trials


if __name__ == "__main__":
    trials = 100000
    stay, switch = run_simulation(trials)

    print(f"Trials: {trials}")
    print(f"Stay Probability   : {stay:.4f}")
    print(f"Switch Probability : {switch:.4f}")