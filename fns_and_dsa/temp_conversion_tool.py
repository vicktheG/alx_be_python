CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    global temp
    converted_temp = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {converted_temp}°C")


def convert_to_fahrenheit(celcius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    global temp
    converted_temp = (temp + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celcius}°C is {converted_temp}°F")


temp = int(input("Enter the temperature to convert: "))

# print("Invalid temperature. Please enter a numeric value.")

temperature_unit = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): "
).upper()
if temperature_unit == "F":
    convert_to_celsius(temp)
elif temperature_unit == "C":
    convert_to_fahrenheit(temp)
else:
    print("Enter either F/C")
