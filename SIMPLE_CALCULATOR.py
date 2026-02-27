#step=1 function to create arithmetic operations
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2


def multiply(num1,num2):
    return num1*num2


def div(num1,num2):
    return num1/num2


def floor_div(num1,num2):
    return num1//num2


def avg(num1,num2):
    return (num1+num2)/2

#step=2 user input
print("please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Floor_Div\n" \
      "6. Mean\n" 
      )

select=int(input("Select the Operation From 1 to 6: "))

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

##step=3 print the result using if- else
if select == 1:
     print(n1, "+", n2, "=", \
           add(n1,n2))
elif select == 2:
     print(n1, "-", n2, "=", \
           sub(n1,n2))

elif select == 3:
     print(n1, "*", n2, "=", \
           multiply(n1,n2))
     
elif select == 4:
     print(n1, "/", n2, "=", \
           div(n1,n2))   
     
elif select == 5:
     print(n1, "//", n2, "=", \
           floor_div(n1,n2))

elif select == 6:
     print("(", n1, "+", n2, ")","/", "2", "=", \
           avg(n1,n2))
     
else:
    print("invalid operation! pls select again...")




