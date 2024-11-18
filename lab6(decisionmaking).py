from datetime import datetime

def show_instructions():
    print("\nDecision Making Instructions:")
    print("- Enter time (e.g., '6 AM', '12 PM').")
    print("- Enter 'weekday' or 'weekend'.")
    print("- Enter weather conditions (e.g., 'sunny').")
    print("- Type 'done' to finish decision input.")
    print("- Type 'r' to show instructions again.\n")

def change_time_to_24_hour(in_time):
    try:
        return int(datetime.strptime(in_time, "%I %p").strftime("%H"))
    except ValueError:
        print("Invalid time format. Use '6 AM', '12 PM', etc.")
        return None

def check_decision(decision, time):
    if 6 <= time < 8 and "weekday" in decision:
        return "Go to work"
    if 12 <= time < 13:
        return "Lunch"
    if 21 <= time < 22:
        return "Go to bed"
    if "weekend" in decision and "sunny" in decision:
        return "Go for a walk"
    return "Invalid input"

def main():
    decision = []
    time_value_full = None
    show_instructions()
    
    while True:
        decision_input = input("Enter the details: ").strip()
        
        # Handle time input
        if "AM" in decision_input.upper() or "PM" in decision_input.upper():
            time_value_full = change_time_to_24_hour(decision_input)
            if time_value_full is None:
                continue  # Invalid time input, ask again
        
        # Handle 'done' and 'r' commands
        elif decision_input.lower() == "r":
            show_instructions()
        elif decision_input.lower() == "done":
            if time_value_full is None:
                print("Time is required before making a decision.")
                continue
            result = check_decision(decision=decision, time=time_value_full)
            print(result)
            break
        
        # Handle other decision inputs
        else:
            decision.append(decision_input.lower())

main()
