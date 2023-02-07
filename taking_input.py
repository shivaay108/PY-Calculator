# here we do the input process of the code
import calculation
def user_inputandcalculation():
    first_input = float(input("Enter num1 : "))
    operator_input = (input("Enter operator : "))
    second_input = float(input("Enter num2 : "))
    
    if(operator_input == "+"):
        result = float(calculation.add(first_input, second_input))
        print("result : " , result)
    elif (operator_input == "-"):
        result = float(calculation.subtract(first_input,second_input))
        print("result : "  , result)
    elif(operator_input == '*'):
        result = float(calculation.multiply(first_input, second_input))
        print("result : " , result)
    elif(operator_input == "/"):
        result  = float(calculation.divide(first_input,second_input))
        print("result : " , result)
    else:
        print("this is not a vaild operator")

# then we ask them what they want to do with these inputs