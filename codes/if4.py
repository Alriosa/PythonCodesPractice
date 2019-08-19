#Double conditional

print("Enterprise status")
print("Enter the earnings")
enterprise_earnings = int(input())

print("number of employee")
number_employee = int(input())

print("we got gov sup?")
gov_sup = bool(input())

if enterprise_earnings < 10 and number_employee >10:
    print("The things are going bad")
elif enterprise_earnings > 10 and number_employee ==10:
    print("Perfect!")
elif enterprise_earnings <10 and number_employee <10 or gov_sup ==True:
    print("We got this!")
else:
    print("Could be better...")
