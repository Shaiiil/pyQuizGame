print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's Play: ")
score = 0

answer = input("1. Which keyword is used to define a function in Python? \n  func \n  function \n  def \n  define\n ")
if answer == "def":
    print("Congrats You Got it Right!\nThe def keyword is used in Python to define a function. It is followed by the function name and parentheses, e.g., def my_function():.\n")
    score += 1
else: 
    print("Uh Oh, It seems like you got it Wrong! The Correct answer was def\nThe def keyword is used in Python to define a function. It is followed by the function name and parentheses, e.g., def my_function():.\n")


answer = input("2. What is the index of the first element in a Python list? \n  0 \n  1 \n  -1 \n ")
if answer == "0":
    print("Congrats You Got it Right!\nPython uses zero-based indexing, meaning that the index of the first element in a list is 0, not 1.\n")
    score += 1
else: 
    print("Uh Oh, It seems like you got it Wrong! The Correct answer was 0\nPython uses zero-based indexing, meaning that the index of the first element in a list is 0, not 1.\n")


answer = input("3. Which of the following is a valid Python variable name? \n  2nd_variable \n  variable-name \n  variable_2 \n  variable@2\n ")
if answer == "variable_2":
    print("Congrats You Got it Right!\nIn Python, variable names can contain letters, numbers, and underscores, but they cannot start with a number or contain special characters.\n")
    score += 1
else: 
    print("Uh Oh, It seems like you got it Wrong! The Correct answer was variable_2\nIn Python, variable names can contain letters, numbers, and underscores, but they cannot start with a number or contain special characters.")


answer = input("4. Which Python library is used for data analysis? \n  matplotlib \n  numpy \n  pandas \n  requests\n ")
if answer == "pandas":
    print("Congrats You Got it Right!\nTThe pandas library is widely used for data manipulation and analysis in Python, providing data structures like Series and DataFrames.\n")
    score += 1
else: 
    print("Uh Oh, It seems like you got it Wrong! The Correct answer was pandas\nThe pandas library is widely used for data manipulation and analysis in Python, providing data structures like Series and DataFrames.\n")

print("Thanks for finishing the Quiz Game!!")
print("Your total score was "+ str(score) + " out of 4")
  