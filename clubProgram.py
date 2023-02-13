gender = "male"
age = 17
if age >= 0 and age <= 17 :
   print("Too young")
elif age >= 18 and gender == "male":
    print("Can go in! But does not receive a free drink")
elif age >= 18 and gender == "female":
    print("Can go in! receives a free drink, its ladies night")
else:
    print("Invalid input")


def club_checkin(age = 17 , gender = "male"):
    if age >= 0 and age <= 17:
        return "Too young"
    elif age >= 18 and gender == "male":
        return "Can go in! But does not receive a free drink"
    elif age >= 18 and gender == "female":
        return "Can go in! receives a free drink, its ladies night"
    else:
        return "Invalid input"
age = int(input("Enter your age "))
gender = input("Enter gender(male,female)")
# age = 18
# gender = "male"

print(club_checkin(age, gender))
