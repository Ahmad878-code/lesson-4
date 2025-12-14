# Take marks as input from users
print("Enter marks obtained in 4 subjects :")
math = int(input("Math: "))
physics = int(input("physics: "))
chemistry = int(input("Chemistry: "))
computer = int(input("Computer: "))

# Lets calculate the percentage of marks
sum= math + physics + chemistry + computer
print("sum of math,physics,chemistry and computer")
percentage = (sum/400) * 100

print(end="percentage marks = ")
print(percentage)