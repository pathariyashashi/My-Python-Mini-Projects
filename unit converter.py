# UNIT CONVERTER PROJECT

def length_converter():
    print("\nLength Converter")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")

    choice = input("Choose option: ")

    if choice == "1":
        km = float(input("Enter kilometer: "))
        meter = km * 1000
        print("Result:", meter, "meters")

    elif choice == "2":
        meter = float(input("Enter meter: "))
        km = meter / 1000
        print("Result:", km, "kilometers")

    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")

    choice = input("Choose option: ")

    if choice == "1":
        kg = float(input("Enter kilogram: "))
        gram = kg * 1000
        print("Result:", gram, "grams")

    elif choice == "2":
        gram = float(input("Enter gram: "))
        kg = gram / 1000
        print("Result:", kg, "kilograms")

    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Result:", f, "Fahrenheit")

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Result:", c, "Celsius")

    else:
        print("Invalid choice")


# Main Menu
while True:

    print("\n===== UNIT CONVERTER =====")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        length_converter()

    elif option == "2":
        weight_converter()

    elif option == "3":
        temperature_converter()

    elif option == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Option")