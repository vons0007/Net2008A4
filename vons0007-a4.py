print("test")
class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
class main:
    def run(self):
        calc = calculator()
        print("what operation would you like to perform? ")
        operation = input("Enter +, -, *, /, or ^ for power: ")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if operation == '+':
            result = calc.add(a, b)
        elif operation == '-':
            result = calc.subtract(a, b)
        elif operation == '*':
            result = calc.multiply(a, b)
        elif operation == '/':
            result = calc.divide(a, b)
        elif operation == '^':
            result = calc.power(a, b)
        else:
            print("Invalid operation.")
            return
        print(f"The result is: {result}")
        
if __name__ == "__main__":
    app = main()
    app.run()