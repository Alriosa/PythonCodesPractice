#Double conditional

print("Enterprise status")
print("Enter the earnings")
enterprise_earnings = int(input())

print("number of employee")
number_employee = int(input())

if enterprise_earnings < 10 and number_employee >10:
    print("The things are going bad")
elif enterprise_earnings > 10 and number_employee ==10:
    print("Perfect!")
else:
    print("Could be better...")
