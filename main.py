# Data Types in Python
from pyscript import display, document

# String variable or #str
name = "Elise Lim"   

# Integer variable or #int
age = 15   

# Float variable or #float
height_cm = 160.02   

# List variable or #list
countries_to_visit = ["Maldives", "Italy", "Canada"]   

# Boolean variable or #bool
student_type = False  

# Dictionary variable or #dict
personal_info = {
    "color": "Pink",
    "car_brand": "N/A",
    "shoe_size": 7,
    "best_friend": "Misha"
}  

# Set variable or #set
favorite_fruits = {"Mango", "Banana", "Dragonfruit", "Grapes", "Strawberry"}   

# Tuple variable or #tuple
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")   

# Display 
document.getElementById('result').innerHTML = f"""
<h4>Hello! My name is <i>{name}</i>.</h4> 
<ul>
  <li>Age: {age} years old</li>
  <li>Height: {height_cm} cm</li>
  <li>Countries I want to visit: {countries_to_visit}</li>
  <li>Am I a new student? {student_type}</li>
  <li>Personal Info: {personal_info}</li>
  <li>Favorite Fruits: {favorite_fruits}</li>
  <li>Days of the Week: {days_of_week}</li>
</ul>
"""
