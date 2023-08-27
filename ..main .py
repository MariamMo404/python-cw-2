my_name=input("what is your name")
my_age=input("how old are you")
print(f"my name is{my_name} and i an {my_age}yers old")
first_number=input("add first number")
second_number=input("addnsecond number")
operation=input("what is your operation-+/*")
if operation == '+': 
    print(first_number + second_number)
elif operation == "-" :
        print(first_number- second_number)
elif operation == "*" :       
      print(first_number*second_number)
elif operation == "/" :      
      print(first_number/second_number)
else :
      print(" the operation is not valid" )  
bus_capcity=(20)
people_inbus=int("how many people in the bus")
waiting=int("how many people are waiting")
empty_seats=(bus_capcity-people_inbus)
if empty_seats>=waiting:
 print("join")
else:
     print("sorry the us is full")
