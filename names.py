import random
import string
import time
import json

def gen_username():
    name = generate_full_name().split(" ")[0].lower()
    username = name + ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(4,6)))
    print(username)
    return username

def gen_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=12))
    print(password)
    return password

def generate_full_name():
    first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Judy",
    "Kyle", "Lily", "Mason", "Nina", "Oliver", "Penny", "Quinn", "Riley", "Sam", "Tina",
    "Ulysses", "Violet", "Walter", "Xander", "Yara", "Zane", "Aiden", "Bella", "Cameron",
    "Daisy", "Ethan", "Fiona", "Gabe", "Hazel", "Isaac", "Jasmine", "Kai", "Luna", "Miles",
    "Nora", "Oscar", "Piper", "Quentin", "Raven", "Sawyer", "Toby", "Ursula", "Vance",
    "Wendy", "Xavier", "Yvonne", "Zach", "Ava", "Ben", "Cara", "Dylan", "Ella", "Finn",
    "Gina", "Henry", "Ivy", "Jack", "Kara", "Leo", "Mia", "Noah", "Olivia", "Parker",
    "Quincy", "Rory", "Sadie", "Troy", "Uma", "Victor", "Willa", "Xena", "Yuri", "Zara"
]
    last_names = [
    "Adam", "Bridget", "Caleb", "Dakota", "Eli", "Faye", "Gage", "Harmony", "Ivy", "Jax",
    "Kira", "Liam", "Maya", "Nico", "Olive", "Pax", "Quinn", "Remi", "Sage", "Talia",
    "Ulysses", "Vera", "Wade", "Xander", "Yara", "Zane", "Aiden", "Bella", "Cameron",
    "Daisy", "Ethan", "Fiona", "Gabe", "Hazel", "Isaac", "Jasmine", "Kai", "Luna", "Miles",
    "Nora", "Oscar", "Piper", "Quentin", "Raven", "Sawyer", "Toby", "Ursula", "Vance",
    "Wendy", "Xavier", "Yvonne", "Zach", "Ava", "Ben", "Cara", "Dylan", "Ella", "Finn",
    "Gina", "Henry", "Ivy", "Jack", "Kara", "Leo", "Mia", "Noah", "Olivia", "Parker",
    "Quincy", "Rory", "Sadie", "Troy", "Uma", "Victor", "Willa", "Xena", "Yuri", "Zara"
]
    return random.choice(first_names) + " " + random.choice(last_names)


# print(gen_username())