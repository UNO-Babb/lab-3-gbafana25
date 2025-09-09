#TempConvert.py
#Name: Gareth Moodley
#Date: 9-9-2025
#Assignment: Convert Fahrenheit to Celsius


def main():
  #Prompt the user for a Fahrenheit temperature
  
  tempF = int(input("Input a temperature in Fahrenheit: "))

  #Convert that temperature to celsius, rounding to 1 decimal percision

  tempC = ((tempF - 32) * 5) / 9
  tempC = round(tempC, 1)
  #Output converted temperature.

  print(tempF, "is", tempC, "degrees celsius.")

if __name__ == '__main__':
  main()
