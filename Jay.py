import re
from Weather import get_weather
from Numbers import *
from Time import *
from Translator import translate
from Leagues import *
from Cooking import cooking
from Gardening import gardening
from Paint import *

print("Hi, I'm Jay. I'm here to assist you in any way you want.")

while True:
    command = input("What would you like me to do? ").lower()
    
    if any(keyword in command for keyword in ["weather", "forecast", "temperature", "rain", "sunny", "cloudy"]):
        match = re.search(r"(?:in|of|at|location(?: of)?)\s+(.+)", command)
        if match:
            location = re.sub(r"[^a-zA-Z\s]", "", match.group(1).strip())
        else:
            location = input("In what city? ").strip()
        
        get_weather(location)

    elif "square" in command and ("draw" in command or "make" in command or "create" in command):
        draw_square()
    
    elif "triangle" in command:
        draw_triangle()
    
    elif "circle" in command:
        draw_circle()

    elif "pentagon" in command:
        draw_pentagon()

    elif "hexagon" in command:
        draw_hexagon()
    
    elif "octagon" in command:
        draw_octagon()
    
    elif "star" in command:
        draw_star()

    elif "paint" in command or "draw" in command or "drawing" in command:
        paint()
        print("Nice drawing :)")
    
    elif "random" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        get_random(numbers[0], numbers[1])
    
    elif "multiplied" in command or "times" in command or "*" in command or "multiply" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        multiply(numbers[0], numbers[1])
    
    elif "divided" in command or "/" in command or "divide" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        divide(numbers[0], numbers[1])
    
    elif "plus" in command or "add" in command or "+" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        add(numbers[0], numbers[1])
    
    elif "minus" in command or "subtract" in command or "-" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        subtract(numbers[0], numbers[1])

    elif "power" in command or "^" in command:
        number = re.findall(r'\d+', command)
        number = [int(num) for num in number]
        num1 = number[0]
        num2 = number[1]
        power(num1, num2)

    elif "square root" in command or "sqrt" in command or "root" in command or "square rooted" in command:
        num = re.findall(r'\d+', command)
        num = [int(num) for num in num]
        num = num[0]
        square_root(num)

    elif "squared" in command or "square" in command:
        number = re.findall(r'\d+', command)
        num = [int(num) for num in number]
        num = num[0]
        print(f"{num} squared is {int(num) ** 2}")
    
    elif "cubed" in command or "cube" in command:
        number = re.findall(r'\d+', command)
        num = [int(num) for num in number]
        num = num[0]
        print(f"{num} cubed is {int(num) ** 3}")
    
    elif "factorial" in command:
        num = re.findall(r'\d+', command)
        factorial(num)

    elif "timer" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        
        if "seconds" in command:
            hours = 0
            minutes = 0
            seconds = numbers[0]
        
        if "hours" in command:
            hours = numbers[0]
            minutes = 0
            seconds = 0
        
        if "minutes" in command:
            hours = 0
            minutes = numbers[0]
            seconds = 0
        
        timer(hours, minutes, seconds)
    
    elif "time" in command:
        get_time()
    
    elif "date" in command:
        get_date()
    
    elif "alarm" in command:
        numbers = re.findall(r'\d+', command)
        numbers = [int(num) for num in numbers]
        hours = numbers[0]
        minutes = numbers[1]
        alarm(hours, minutes)

    elif "premier" in command and ("scores" in command or "results" in command):
        premier_results()
    
    elif "premier" in command and ("table" in command or "standings" in command):
        premier_table()

    elif "champions" in command and ("scores" in command or "results" in command):
        champions_results()

    elif "champions" in command and ("table" in command or "standings" in command):
        champions_table()

    elif "serie" in command and ("a" in command or "serie a" in command) and ("scores" in command or "results" in command):
        serie_results()

    elif "serie" in command and ("a" in command or "serie a" in command) and ("table" in command or "standings" in command):
        serie_table()
    
    elif "la liga" in command and ("scores" in command or "results" in command):
        la_liga_results()

    elif "la liga" in command and ("table" in command or "standings" in command):
        la_liga_table()
    
    elif "bundesliga" in command and ("scores" in command or "results" in command):
        bundesliga_results()

    elif "bundesliga" in command and ("table" in command or "standings" in command):
        bundesliga_table()
    
    elif "ligue" in command and ("1" in command or "ligue 1" in command) and ("scores" in command or "results" in command):
        ligue_results()

    elif "ligue" in command and ("1" in command or "ligue 1" in command) and ("table" in command or "standings" in command):
        ligue_table()

    elif "recipe" in command or "cooking" in command or "cook" in command or "make" in command or "recipes" in command:
        match = re.search(r"(?:for|of|in|at|recipe(?: for)?)\s+(.+)", command)
        if match:
            item = re.sub(r"[^a-zA-Z\s]", "", match.group(1).strip())
            cooking(item)
        else:
            item = input("What recipe would you like? ").strip()
            cooking(item)

    elif "plant" in command or "gardening" in command or "garden" in command or "plants" in command:
        match = re.search(r"(?:for|of|in|at|type|plant(?: for)?)\s+(.+)", command)
        if match:
            item = re.sub(r"[^a-zA-Z\s]", "", match.group(1).strip())
        else:
            item = input("What plant would you like? ").strip()
        
        try:
            gardening(item)
        except IndexError:
            print("No plant found. Try another search term.")
        except Exception as e:
            print(f"An error occurred while fetching plant information: {e}")

    elif "nuclear" in command:
        print("Please don't use nuclear weapons. It's not a good idea. Also, this probably means you are not Simona so get out of her computer.")
    
    elif "bomb" in command or "bombs" in command:
        print("Please don't use bombs. It's not a good idea. They are really not too good. Also, this probably means you are not Simona so get out of her computer.")

    elif "translate" in command or "translated" in command or "into" in command or "in" in command:
        pattern1 = r"translate\s(.+?)\s(?:into|in)\s(\w+)"
        pattern2 = r"translate\s(?:into|in)\s(\w+)\s(.+)"
        pattern3 = r"(.+?)\s(?:in)\s(\w+)"
        
        match1 = re.search(pattern1, command)
        match2 = re.search(pattern2, command)
        match3 = re.search(pattern3, command)
        
        if match1:
            text = match1.group(1).strip()
            language = match1.group(2).strip()
        
        elif match2:
            language = match2.group(1).strip()
            text = match2.group(2).strip()
        
        elif match3:
            text = match3.group(1).strip()
            language = match3.group(2).strip()
        
        else:
            print("Sorry, I couldn't understand the translation request.")
            continue
        
        translate(text, language)

    elif "exit" in command or "quit" in command or "stop" in command or "bye" in command or "goodbye" in command:
        print("See you soon!")
        break

    else:
        print("I'm sorry Simona, I unfortunately can't do that or I don't understand that yet.")