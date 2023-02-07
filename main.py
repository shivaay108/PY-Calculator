import display
import taking_input

display.banner()
 
print("Operators :")
operators = ["+" , "-" , "*" , "/"]
count = 1
for i in operators:
    print(count ,") "  , i)
    count = count + 1

taking_input.user_inputandcalculation()

