
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
while True:
    gallons = float(input("Enter the quantity of gasoline in American gallons (negative value to quit): "))

    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is approximately {liters:.2f} liters.")