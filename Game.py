import random

def paly_ball():
    return random.choice([0,1,2,3,4,6])

def cricket_game():
    overs, target, scoreboard = 5, 0,{"Team A": 0, "Team B": 0}

    def display_scoreboard():
        print("\nCurrent Scoreboard:\nTeam A:",scoreboard["Team A"],"\n Team B:",scoreboard["Team B"])

    print("Welcome to Simple Cricket Game")

    for team in("Team A", "Team B"):
        print(f"\n{team}'s Batting:")
        target = scoreboard["Team A"] + 1 if team == "Team B" else 0

        for over in range(overs):
            print(f"\nOver {over+1}:")

            for ball in range(6):
                input("Press Enter to bowl:")
                run_scored = paly_ball()
                print(f"Ball {ball + 1}: {run_scored} runs scored")
                scoreboard[team] += run_scored
                display_scoreboard()

                if team == "Team B" and scoreboard[team] > target:
                    print(f"{team} wins by {scoreboard[team] - target} runs")
                    return

    print(f"\nMatch Drawn!!\nFinal Scoreboard:\nTeam A:",scoreboard["Team A"],"\n Team B:",scoreboard["Team B"])

if __name__ == "__main__":
    cricket_game()