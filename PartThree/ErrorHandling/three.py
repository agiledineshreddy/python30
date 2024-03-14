a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))

print("Good Morning")
try:
    print(a/b)  # riskly code
except:
    print(a/1)  # handling code

finally:
    print("Clean-up code")

print("Good Afternoon")
print("Good Night")
