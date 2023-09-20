from PyInquirer import prompt

import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
    {
        "type":"input",
        "name":"email",
        "message":"New User - Email: ",
    },
]

def add_user():
    infos = prompt(user_questions)

    with open("users.csv", "a", newline="") as f:
        reader = csv.writer(f)
        name = infos.get("name")
        email = infos.get("email")
        reader.writerow([name,email])

    return