# Write your code here.

#Task 1: Hello
def hello():
    return "Hello!"
hello()

#Task 2: Greet with a Formatted String
def greet(name):
    return("Hello, " + name + "!")

greet("Mariya")

#Task 3: Calculator

def calc(a,b,operation="multiply"):
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == 'multiply':
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):           
            return "You can't multiply those values!"
        return a*b
    elif operation == "divide":
        try:
            return a / b
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "modulo":
        try: 
            return a%b
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "int_divide":
        try:
            return a // b
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "power":
        return a ** b

# def calc(a, b, operation="multiply"):
#     try:
#         match operation:
#             case "add":
#                 return a + b
#             case "subtract":
#                 return a - b
#             case "multiply":
#                 if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):           
#                     return "You can't multiply those values!"
#                 return a * b
#             case "divide":
#                 return a / b
#             case "modulo":
#                 return a % b
#             case "int_divide":
#                 return a // b
#             case "power":
#                 return a ** b
#             case _:
#                 return "Error: Unsupported operation"
#     except ZeroDivisionError:
#         return "You can't divide by 0!"


print(calc(7,4,))
print(calc(7,4, "add"))
print(calc(7,4, "subtract"))
print(calc(7,4, 'multiply'))
print(calc("a","b", 'multiply'))
print(calc(7,4, "divide"))
print(calc(7,0, "divide"))
print(calc(7,4, "modulo"))
print(calc(7,0, "modulo"))
print(calc(7,4, "int_divide"))
print(calc(7,0, "int_divide"))
print(calc(7,4, "power"))


#Task 4: Data Type Conversion

def data_type_conversion(value, type):
    try: 
        if type == 'int':
            return int(value)
        elif type == 'float':
            return float(value)
        elif type == 'str':
            return str(value)
        else:
            return "Invalid type!"
    except ValueError:
        return ("You can't convert " + value + " into a " + type + ".")

print(data_type_conversion("7", "int"))
print(data_type_conversion("hello", "int"))

#Task 5: Grading System, Using *arg

def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "E"
    except:
        return "Invalid data was provided."

print(grade(65,45,77,82,97))
print(grade("hello"))

#Task 6: Use a For Loop with a Range

def repeat(string, count):
    result = ''
    for _ in range(count):
        result += string
    return result

print(repeat("Hello!", 4))

#Task 7: Student Scores, Using **kwargs
def student_scores(parameter, **kwargs):
    if parameter == "best":
        return max(kwargs, key=kwargs.get)
    elif parameter == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid parameter"

print(student_scores("best", Kate=95, Tom=64, Anna=73))
print(student_scores("mean", Kate=95, Tom=64, Anna=73)) 

#Task 8: Titleize, with String and List Operations

def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    return " ".join(
        word.capitalize() if i == 0 or i == len(words) - 1 or word.lower() not in little_words else word.lower()
        for i, word in enumerate(words)
    )

print(titleize("i like to code and learn something new"))  

#Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("musicology", "os"))

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels="aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[:2] == "qu":
            pig_latin_words.append(word[2:] + "quay")
        elif word[0] in vowels:
            pig_latin_words.append(word + "ay")
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1
            if index > 1 and word[index - 1] == 'q' and word[index] == "u":
                index += 1
            pig_latin_words.append(word[index:] + word[:index] + "ay")

    return " ".join(pig_latin_words)
print(pig_latin("i like to code and learn something new"))
