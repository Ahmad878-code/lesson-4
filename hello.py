print("Enter the number of Days :")

num = int(input())

year = int(num/365)
months = int((num % 365)/30)
days = (num % 365) % 30
print("Total number of year(s) :")
print(year)
print("Total number of month(s) :")
print(months)
print("Total number of day(s) :")
print(days)
          