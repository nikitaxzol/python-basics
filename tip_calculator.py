print("=== Tips counter ===")

try:
    bill = float(input("Write bill amount: "))
    tip_percent = float(input("Write Tips %: "))
    staff_amount = float(input("Write number of workers:"))
except ValueError:
    print("Only numbers, sorry, try again")
    exit()

if bill <= 0 : 
    print("sorry it can't be less that 0, try again please")
    exit()
if tip_percent <= 0 : 
    print("sorry it can't be less that 0, try again please")
    exit()
if staff_amount <= 0 :
    print("sorry it can't be less that 0, try again please")

tip = bill * tip_percent/100
total = bill + tip
tip_per_person = tip / staff_amount


tip = round (tip, 5)
total = round (total, 5)
tip_per_person = round (tip_per_person, 1)

print("Tips:", tip)
print("total to pay:", total)
print("Tips amount for 1 worker:", tip_per_person)