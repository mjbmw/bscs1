print("State your Information")

name = input("Whats your name?")
age = int(input("What's your age?"))
student = input("Are you student? (yes/no): ").lower()

if age < 13:
    price = 100

elif 13 <= age <= 17 and student == "yes":
    price = 120

elif 18 <= age <=59:
    if student == "yes":
        price = 150
    else:
        price = 200

elif age >=60:
    price = 80

else:
    price = 0

print("Ticket Information")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Student: {student}")
print(f"Ticket Price: P{price}")


 
      

