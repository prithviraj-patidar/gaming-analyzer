import data


def analyze_time():
    print("\n--- Gaming Time Analysis ---")

    if len(data.sessions) == 0:
        print("No data available!")
        return

    total = 0

    for session in data.sessions:
        total = total + session[2]

    average = total / len(data.sessions)

    print("Total gaming time:", total, "hours")
    print("Average session time:", average, "hours")


def analyze_games():
    print("\n--- Game Analysis ---")

    if len(data.sessions) == 0:
        print("No data available!")
        return

    game_times = {}

    for session in data.sessions:
        game = session[1]
        hours = session[2]

        if game in game_times:
            game_times[game] = game_times[game] + hours
        else:
            game_times[game] = hours

    print("\nGaming time by game:")

    for game in game_times:
        print(game, ":", game_times[game], "hours")

    # FIND MOST PLAYED GAME
    most_game = ""
    most_time = 0

    for game in game_times:
        if game_times[game] > most_time:
            most_time = game_times[game]
            most_game = game

    print("\nMost played game:", most_game)
    print("Time played:", most_time, "hours")