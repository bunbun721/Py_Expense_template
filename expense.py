from PyInquirer import prompt

import csv

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)

    with open("expense_report.csv", "w", newline="") as f:
        reader = csv.writer(f)
        amount = infos.get("amount")
        label = infos.get("label")
        spender = infos.get("spender")
        reader.writerow([amount,label,spender])

    print("Expense Added !")
    return True


