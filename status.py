from PyInquirer import prompt

import csv

def balance():
    balance_per_user = {}
    print("Balance:")
    with open('expense_report.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            payer = line[2]
            payer = payer.strip()
            users = line[3]
            users = users.replace("[","")
            users = users.replace("]","")
            users = users.replace("'","")
            users = users.split(",")

            if payer not in balance_per_user:
                balance_per_user[payer] = 0
            for user in users:
                user = user.strip()
                if payer == user:
                    balance_per_user[user] += float(line[0])
                    continue
                    
                elif user not in balance_per_user:
                    balance_per_user[user] = 0
                balance_per_user[user] -= float(line[0]) / len(users)

    for user in balance_per_user:
        print(f"{user}: {balance_per_user[user]}")


            


def display_status(*args):
    balance()
    return True


