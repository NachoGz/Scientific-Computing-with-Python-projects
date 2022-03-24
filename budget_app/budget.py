class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
    # methods
    # accepts an amount and description
    def deposit(self, amount, description=''):  
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    # checks balance and returns a true or false
    def check_funds(self, amount):
        return self.balance >= amount

    # similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            self.balance -= amount
            return True
        else:
            return False
    
    # returns the current balance of the budget category based on the deposits and withdrawals that have occurred
    def get_balance(self):
        return self.balance
    
    # add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]"
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            withdraw_description = f'Transfer to {destination.category}'
            self.withdraw(amount, withdraw_description)

            deposit_description = f'Transfer from {self.category}'
            destination.deposit(amount, deposit_description)
            return True
        else:
            return False
    def show(self):
        return self.ledger
   
    def __str__(self):
        table = ''
        len_cat = len(self.category)
        ast = (30 - len_cat)//2

        row = '*'*ast + self.category + '*'*ast + '\n'
        ledger = self.ledger
        r_limit = 7 + len_cat
        for item in ledger:
            # print(item)
            # "{:.2f}".format(a_float)
            row += f'{item["description"][:23]:<23}{"{:.2f}".format(item["amount"])[:7]:>7}\n'
        row += f'Total: {self.balance}'
        table += row 

        return table


def create_spend_chart(categories):
    expen = 0
    mon = []
    for category in categories:
        catexpen = 0
        for j in category.ledger:
            if j["amount"] < 0:
                expen += j["amount"]
                catexpen += j["amount"]
        # total = expen + category.balance
        # perc = (expen * 100) / total
        # nearest_multiple = 10 * round(perc/10)

        mon.append(catexpen)
        # percent.append(nearest_multiple)
    print(expen)
    percent = []
    for i in mon:
        # percent.append(round((i / expen * 100) / 10) * 10)
        percent.append((round((i * 100) / expen)/10) * 10)
    graph = "Percentage spent by category\n"
    num = 100

    while num >= 0:
        graph += str(num).rjust(3) + "| "
        for i in percent:
            if i >= num:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n" 
        num -= 10
    graph += "    "
    num = len(categories)
    graph += "-" * (num * 3 +1)
    graph += "\n"
    graph += "     "
    high = 0

    for category in categories:
        if len(category.category) > high:
            high = len(category.category)
    for category in categories:
        while len(category.category) != high:
            category.category += " "
    for i in range(high):
        for category in categories:
            graph += category.category[i] + "  "
        graph += "\n" + "     "
    graph = graph.rstrip() + '  '
    # print(graph)

    return graph
    

    