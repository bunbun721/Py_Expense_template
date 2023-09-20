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
    {
        "type":"checkbox",
        "name":"split",
        "message":"New Expense - People Involved: ",
        "choices": [ {"name":x, "checked":True} for x in get_spender_choices()]
    }
]

def new_expense(*args):
    infos = prompt(expense_questions)

    with open("expense_report.csv", "a", newline="") as f:
        reader = csv.writer(f)
        amount = infos.get("amount")
        label = infos.get("label")
        spender = infos.get("spender")
        split = infos.get("split")
        for user in split:
            print("Adding " + user + " to expense report")

        reader.writerow([amount,label,spender, split])

    print("Expense Added !")
    return True


