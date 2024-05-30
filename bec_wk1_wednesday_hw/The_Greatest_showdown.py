# Task 1: Identify the Greatest
user_input1 = int(input("Enter a number: "))
user_input2 = int(input("Enter another number: "))
user_input3 = int(input("Enter one more number: "))

if user_input1 > user_input2 and user_input1 > user_input3:
    print(user_input1)
elif user_input2 > user_input1 and user_input2 > user_input3:
    print(user_input2)
else:
    print(user_input3)