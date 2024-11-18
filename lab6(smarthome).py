def weather(automater,temperature):   
        if "dark" in automater and "yes" in automater:
            return "Turn on the lights"
        if temperature is not None and temperature < 18:
            return "Turn on the heater"
        if  temperature is not None and  temperature > 25:
            return "Turn on the air conditioner"   
        if "armed" in automater and "opened" in automater:
            return "It might be pleasant day"
        return "Not clear criteria"
    
def showinstructions():
    print("Available Conditions")
    print("Is it dark outside? (dark or not dark)")
    print("Is someone at home? (yes or not)")
    print("temperature below 18")
    print("Is the security armed or not armed")
    print("temperature above 25")
    print("Is the door opened or closed\n")
    print("Enter your Criterias (type 'done' when finished):")
    print("To Show instructions again type 'r':")
    
def main():
    automater =[]
    temperature = None
    showinstructions()
    while True:
        automate = input("Criterias: ")    
        try:
            temp_value = int(automate)
            temperature = temp_value 
        except ValueError:
            if automate != "r":    
                automater.append(automate)
        if automate == "r":
            showinstructions()
        if automate == "done":
            print(weather(automater,temperature))
            break
main()
