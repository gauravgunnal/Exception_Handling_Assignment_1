'''Q1'''
'''In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's 
instructions. When an exception is encountered, the program execution is immediately halted, and the control is transferred to a special 
code block called an exception handler. The exception handler is responsible for handling the exception, which can involve displaying an 
error message, logging the error, or taking any other appropriate action.
Exceptions in Python can occur due to various reasons, such as errors in program logic, input/output issues, or unexpected conditions. 
Some common types of exceptions in Python include `TypeError`, `ValueError`, `FileNotFoundError`, and `ZeroDivisionError`. Python also 
provides a way to define custom exceptions by creating new classes that inherit from the built-in `Exception` class or any of its subclasses.
On the other hand, syntax errors are different from exceptions. Syntax errors occur when the Python interpreter encounters code that 
violates the language's syntax rules. These errors prevent the interpreter from parsing and understanding the code correctly. Syntax 
errors are usually caused by typos, missing parentheses, incorrect indentation, or using invalid language constructs.
When a syntax error is encountered, the Python interpreter displays a traceback that points to the specific line and character where the 
error occurred. Unlike exceptions, which can be caught and handled programmatically, syntax errors need to be fixed directly in the code 
before the program can be executed.
In summary, the main differences between exceptions and syntax errors in Python are:
1. Occurrence: Exceptions occur during the execution of a program, while syntax errors are detected during the parsing stage before the 
program is executed.
2. Handling: Exceptions can be caught and handled using try-except blocks, allowing the program to recover from the error and continue 
execution. Syntax errors need to be fixed in the code itself before the program can run.
3. Causes: Exceptions are often caused by runtime conditions, such as invalid input or unexpected events. Syntax errors are caused by 
violations of the language's syntax rules, such as misspelled keywords or incorrect indentation.
In both cases, error messages and traceback information can provide valuable insights into the nature of the error and help in 
troubleshooting and resolving issues in Python programs.'''

'''Q2'''
'''When an exception is not handled in Python, it leads to an abnormal termination of the program. The Python interpreter displays an 
error message, known as a traceback,which includes information about the type of exception that occurred, the line of code where the exception 
was raised, and the call stack at the time of the exception.
Let's consider an example to illustrate what happens when an exception is not handled:'''
def divide(a, b):
    result = a / b
    return result

num1 = 10
num2 = 0
result = divide(num1, num2)
print(result)
'''In this example, we have a function called divide that takes two numbers as parameters and returns their division. However, in the 
main part of the code, we call the divide function with num2 set to 0. This will raise a ZeroDivisionError exception since dividing a 
number by zero is not allowed.
When this code is executed, the Python interpreter encounters the ZeroDivisionError and looks for an exception handler to handle it. 
If no appropriate exception handler is found, the interpreter stops the program's execution and prints a traceback message, indicating the 
error:'''
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = 10
num2 = 0
result = divide(num1, num2)
print(result)
'''Now, if we run this modified code, instead of the program terminating, it will catch the ZeroDivisionError exception, 
print an error message, and continue executing the subsequent code:'''
Error: Division by zero is not allowed.
None
'''In this case, the program continues to execute after handling the exception, and the value of result is None since the division 
operation failed. Handling exceptions allows you to control how the program responds to errors and enables you to take appropriate
 actions to handle exceptional conditions.'''

'''Q3'''
'''In Python, the try-except statement is used to catch and handle exceptions. The try block contains the code where an exception 
might occur, and the except block specifies the code to be executed if a specific exception is raised. The except block can be used to 
catch and handle multiple types of exceptions.
Here's an example to demonstrate the usage of try-except statement:'''
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = 10
num2 = 0
result = divide(num1, num2)
print(result)

'''Q4'''
'''a. Try and Else:
The try-except-else statement in Python allows you to specify a block of code to be executed if no exceptions occur within the try block. 
The else block is optional and will only execute if no exceptions are raised. It is useful for separating the code that may raise an exception 
from the code that should only execute if the exception does not occur.
Here's an example that demonstrates the use of try-except-else:'''
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The division result is: {result}")

divide(10, 2)
divide(10, 0)
'''b. Finally:
The finally block is used in combination with try-except to specify a block of code that should be executed regardless of whether an exception 
occurs or not. The finally block is optional and will execute after the try and except blocks, even if an exception is raised or not.
Here's an example that demonstrates the use of try-except-finally:'''
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Division operation completed.")

divide(10, 2)
divide(10, 0)
'''c. Raise:
The raise statement in Python is used to explicitly raise an exception. It allows you to raise a specific exception manually at a 
desired location in your code. You can use the raise statement to generate custom exceptions or re-raise exceptions caught in an except block.'''
'''Q5'''
'''Custom exceptions in Python are user-defined exception classes that are created by inheriting from the built-in Exception class or 
its subclasses. They are designed to represent specific types of errors or exceptional conditions that are not covered by the existing 
built-in exceptions.
Custom exceptions are useful for the following reasons:
Specific Error Handling: By creating custom exceptions, you can define distinct exception types that represent specific error scenarios in 
your code. This allows you to handle those exceptions differently, providing more targeted error handling and making your code more expressive
 and maintainable. Custom exceptions can carry additional information about the error context, allowing for more informative error messages or 
 specific actions to be taken based on the exception type.
Code Organization: Custom exceptions help in organizing and categorizing different types of errors in your codebase. By creating a hierarchy 
of exception classes, you can establish a clear structure that reflects the nature of the exceptions and their relationships. This makes it 
easier to understand and navigate the codebase when dealing with multiple exception types.
Code Reusability: Once you define custom exceptions, they can be reused across different parts of your codebase. This promotes code reuse 
and reduces duplication, as you can raise and handle the same custom exception in different parts of your program. It also allows for 
consistent error handling throughout your application.
Here's an example that illustrates the creation and usage of a custom exception in Python:'''
class InvalidEmailError(Exception):
    pass

def send_email(email_address, message):
    if "@" not in email_address:
        raise InvalidEmailError("Invalid email address provided.")
    # Code to send the email...

# Example usage
email = "example.com"
try:
    send_email(email, "Hello, world!")
except InvalidEmailError as e:
    print(str(e))
'''By using a custom exception in this example, we have created a specialized exception type that represents the specific error 
condition of an invalid email address. This allows us to handle this specific type of exception differently than other types of 
exceptions, providing more targeted and meaningful error handling in our code.'''

'''Q5'''
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"InvalidInputError: {self.message}"

def divide(a, b):
    if b == 0:
        raise InvalidInputError("Cannot divide by zero.")

try:
    num1 = 10
    num2 = 0
    divide(num1, num2)
except InvalidInputError as e:
    print(str(e))
