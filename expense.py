from PyInquirer import prompt

import csv

def get_spender_choices():
    with open("users.csv", "r") as f:
        reader = csv.reader(f)
        return [row[0] for row in reader]

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_spender_choices()
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)

    with open("expense_report.csv", "a", newline="") as f:
        reader = csv.writer(f)
        amount = infos.get("amount")
        label = infos.get("label")
        spender = infos.get("spender")
        reader.writerow([amount,label,spender])

    print("Expense Added !")
    return True


