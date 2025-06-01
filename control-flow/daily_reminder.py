task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Make sure to complete it today!")

    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Try to complete it today or tomorrow."
            )

    case "low":
        if time_bound == "yes":
            print (f"\nReminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time." )

    case _:
        print("\nInvalid priority level. Please restart and enter 'high', 'medium', or 'low'.")
        print(f"Your task '{task}' has been noted but cannot be properly prioritized.")
