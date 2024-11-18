def traffic(controls):
    if "red" in controls:
        return "Cars must Stop"
    if "green" in controls:
        return "Cars must go"
    if "yellow" in controls:
        return "Cars must slow down and prepare to stop"
    if "yes" in controls:
        return "The light will turn red after a short delay"
    return "Invalid Input"
def showinstructions():
    print("Traffic Light Control")
    print("Enter the color of  traffic light")
    print("is the pedestrian button pressed?")
    print("Enter the decision (type 'done when finished): ")
    print("To show instructions again type 'r': ")

def main():
    controls = []
    # button = None
    showinstructions()
    while True:
        control=input("Controls: ")
        if control != "r":
            controls.append(control.lower())
        if control == "r":
            showinstructions()
        if control == "done":
            print(traffic(controls=controls))
            break
main()
