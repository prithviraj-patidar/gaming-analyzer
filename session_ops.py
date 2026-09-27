import data


def add_session():
    print("\n--- Add Gaming Session ---")

    date = input("Enter date (DD-MM-YYYY): ")
    game = input("Enter game name: ")
    hours = float(input("Enter gaming time in hours: "))

    if hours < 0:
        print("Gaming time cannot be negative!")
        return

    session = [date, game, hours]
    data.sessions.append(session)

    print("Gaming session added successfully!")


def view_sessions():
    print("\n--- Gaming Sessions ---")

    if len(data.sessions) == 0:
        print("No gaming sessions found!")
        return

    for i in range(len(data.sessions)):
        print(i + 1, ".", data.sessions[i][0],
              "-", data.sessions[i][1],
              "-", data.sessions[i][2], "hours")