print("=== Tips counter ===")

try:
    bill = float(input("Write bill amount: "))
    tip_percent = float(input("Write Tips %: "))
except ValueError:
    print("Only numbers, sorry, try again")
    exit()

tip = bill * tip_percent/100
total = bill + tip

tip = round (tip, 5)
total = round (total, 5)

print("Tips:", tip)
print("total to pay", total)