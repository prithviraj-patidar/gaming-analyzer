import data


def check_limit():
    print("\n--- Gaming Limit Checker ---")

    if len(data.sessions) == 0:
        print("No data available!")
        return

    limit = float(input("Enter your gaming limit per session (hours): "))

    for session in data.sessions:
        if session[2] > limit:
            print(session[0], "-", session[1],
                  ": Limit exceeded!")
        else:
            print(session[0], "-", session[1],
                  ": Within limit.")