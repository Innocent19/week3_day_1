print("Enter Your Year of Birth:")
date_of_birth = input()
age = 2018-int(date_of_birth)
try:
 if age<=18:
    print ("You are a minor")
 elif 18<age<=36:
        print("You are a youth")
 else: 
     print("You are an elder") 
except(NameError,TypeError):
    print("An error occured")
finally:
    print("End of program")    
    
