# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


#You have 12410 days, 1768 weeks, and 408 months left.
age = int(age)
left_years =  90 - age
left_weeks =  left_years * 52
left_months  = left_years * 12
left_days = left_years * 365

print("You have " + str(left_days) + " days," + str(left_weeks) + " weeks, and " + str(left_months) + " months left.")