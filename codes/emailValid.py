valid_email = False

print("Enter your email")
email = input()

for i in email:

    if(i=="@" and i=="."):
        valid_email = True

if valid_email == True:
    print("Valid Email")
else:
    print("Invalid Email")
