print("Welcome to the Python Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
     operation = input("Enter your choice(1/2/3/4) or quit to no operation : ")
     if operation == 'quit':
          print("Exit from calculator")
          break
     if operation in ['1','2','3','4']:
          try:
               num_1 = float(input("Enter a number:"))
               num_2 = float(input("Enter another number:"))
          except ValueError:
               print("Invalid input. Please enter a number.")
               continue
          if operation == '1':
               print(f"{num_1} + {num_2} = {num_1 + num_2}")
          elif operation == '2':
               print(f"{num_1} - {num_2} = {num_1 - num_2}")
          elif operation == '3':
               print(f"{num_1} * {num_2} = {num_1 * num_2}")
          elif operation == '4':
               if num_2 ==0:
                    print("Error! Division by zero is not allowed.")
               else:
                    print(f"{num_1} / {num_2} = {num_1 / num_2}")
        
     else:
          print("Invalid choice. Please choose a valid operation.") 
          print("Thank you for using my calculator..")
          
