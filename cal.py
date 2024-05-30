# Calc.py

def main():
    # Getting values for calculation
    num1 = float("6")
    num2 = float("3")
    
    # Calling add function from add.py
    import add
    result_add = add.add(num1, num2)
    print("Result of addition:", result_add)
    
    # Calling sub function from sub.py
    import sub
    result_sub = sub.sub(num1, num2)
    print("Result of subtraction:", result_sub)

if __name__ == "__main__":
    main()