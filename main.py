dictionary = {"conditionals":"Allow your code to execute different actions depending on whether condition is true or false",
              "functions":"perform a specific task,allowing breaking down of code into smaller,reusable pieces",
              "loops":"repeats a block of code a certain number of times or until a specific condition is met"}
print(dictionary["conditionals"])
for key in dictionary:
    print(key)
    print(dictionary[key])