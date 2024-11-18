def weather(forecasts, temperature):   
        if "cloudy" in forecasts and "no wind" in forecasts:
            return "It might rain"
        if temperature is not None and temperature < 0 and "clear" in forecasts:
            return "It might snow"
        if  temperature is not None and  temperature > 30 and  "no wind" in forecasts:
            return "It might be hot day"   
        if "clear" in forecasts and "wind" in forecasts:
            return "It might be pleasant day"
        return "Not clear criteria"
    
def showinstructions():
    print("Available Forecasts:")
    print("cloudy")
    print("no wind")
    print("temperature below 0")
    print("clear")
    print("temperature above 30")
    print("wind \n")
    print("Enter your forecast (type 'done' when finished):")
    print("To Show instructions again type 'r':")
    
def main():
    forecasts =[]
    temperature = None
    showinstructions()
    while True:
        forecast = input("Forecast: ")    
        try:
            temp_value = int(forecast)
            temperature = temp_value 
        except ValueError:
            if forecast != "r":    
                forecasts.append(forecast)
        if forecast == "r":
            showinstructions()
        if forecast == "done":
            print(weather(forecasts,temperature))
            break     
main()
