import data
import session_ops
import analytics
import limit_checker


def generate_report():
    print("\n========== GAMING REPORT ==========")

    if len(data.sessions) == 0:
        print("No gaming data available!")
        return

    total = 0

    for session in data.sessions:
        total = total + session[2]

    average = total / len(data.sessions)

    print("Number of sessions:", len(data.sessions))
    print("Total gaming time:", total, "hours")
    print("Average session time:", average, "hours")

    print("\nSessions:")

    for session in data.sessions:
        print(session[0], "-", session[1], "-", session[2], "hours")

    print("===================================")


# MAIN MENU
while True:
    print("\n================================")
    print("       GAMING TIME ANALYZER")
    print("================================")
    print("1. Add Gaming Session")
    print("2. View Gaming Sessions")
    print("3. Analyze Gaming Time")
    print("4. Analyze Games")
    print("5. Check Gaming Limit")
    print("6. Generate Report")
    print("7. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        session_ops.add_session()

    elif choice == "2":
        session_ops.view_sessions()

    elif choice == "3":
        analytics.analyze_time()

    elif choice == "4":
        analytics.analyze_games()

    elif choice == "5":
        limit_checker.check_limit()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        print("Thank you for using Gaming Time Analyzer!")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")