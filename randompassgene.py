import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "@#$_.!%*()-=+[]{}()?"
mix = lower + upper + numbers + symbols

print("\nRANDOM PASSWORD GENERATOR\n\n")

while True:
	try:
		length = int(input("Enter Desired Length For Password : "))
		if length <= 3 or length > 16:
			print("Error : Value Must be digit Between 4 to 16!")
		else:
			break
	except ValueError:
		print("Error : Value Must be digit Between 4 to 16!")

password = "".join(random.choices(mix,k = length))
print(f"\nPASSWORD : {password}")