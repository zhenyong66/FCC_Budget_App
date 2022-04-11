class Category:    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = None):
        if description == None:
            description = ""
        amount = round(amount, 2)
        dp = {"amount": amount,
              "description": description}
        self.ledger.append(dp)             
    
    def check_funds(self, amount):
        balance = self.ledger[0]["amount"]
        if amount <= balance:
            return True
        elif amount > balance:
            return False
        
    def withdraw(self, amount, description = None):
        if description == None:
            description = ""
        if self.check_funds(amount) is True:
            amount = -1*amount
            wd = {"amount": amount,    
                  "description": description}
            self.ledger.append(wd)
            return True
        elif self.check_funds(amount) is False:
            return False
    
    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i["amount"]
        return total
        
    def transfer(self, amount, category):
        wd_description = "Transfer to " + str(category.name)
        dp_description = "Transfer from " + str(self.name)
        if self.check_funds(amount) is True:
            wd_amount = -1*amount
            wd = {"amount": wd_amount,
                  "description": wd_description}
            self.ledger.append(wd)
            dp = {"amount": amount,
                  "description": dp_description}
            category.ledger.append(dp)
            return True
        elif self.check_funds(amount) is False:
            return False
    
    def __repr__(self):
        #create title line
        title_line = ""
        asterik_1 = ""
        asterik_2 = ""
        temp = int((30 - len(self.name)) / 2)
        for i in range(temp):
            asterik_1 += "*"
        for j in range(30 - temp - len(self.name)):
            asterik_2 += "*"
        output = title_line + asterik_1 + self.name + asterik_2 + "\n"
        # create lists of items
        for k in self.ledger:
            # description
            if len(k["description"]) > 23:
                desc = str(k["description"][:23])
            elif len(k["description"]) <= 23:
                desc = str(k["description"])
            # amount
            amt = "%.2f" % float(k["amount"])
            whitespace = ""
            temp2 = 30 - len(desc) - len(amt)
            for l in range(temp2):
                whitespace += " "
            itm  = desc + whitespace + amt + "\n"
            output += itm
        # total amount
        output += "Total: " + str(self.get_balance())
        return output
            
# function (outside of class)
def create_spend_chart(categories):
    cat_name = []
    wd = []
    spent_percent = []
    for i in categories:
        # get names
        cat_name.append(i.name)    
        # get total withdrawals
        for j in range(len(i.ledger)):
            itm = i.ledger[j]
            amt = itm["amount"]
            temp = 0
            if amt < 0:
                temp += amt
        wd.append(float(temp))
    tol_wd = sum(wd)
    # get spent percents
    spent_percent = []
    for i in wd:
        temp = int(i / tol_wd * 10)
        spent_percent.append(temp)
    
    # first line
    chart = "Percentage spent by category\n" \

    # bar
    bars = []
    max_bar_length = 11
    for i in spent_percent:
        bar = ""
        o = ""
        bar_space = ""
        for j in range(max_bar_length - i - 1):
            bar_space += " "
        for k in range(i + 1):
            o += "o"
        bar += bar_space + o
        bars.append(bar)
    
    temp = []
    x = 100
    for i in range(max_bar_length):
        temp2 = ""
        for j in bars:
            temp2 += j[i] + "  "
        temp.append(temp2)
        
        if x == 100:
            chart += str(x) + "| " + temp[i] + "\n"
        elif x > 0 and x < 100:
            chart += " " + str(x) + "| " + temp[i] + "\n"
        elif x == 0:
            chart += "  " + str(x) + "| " + temp[i] + "\n"
        x -= 10
   
    # dash line
    dashes = "-"
    for i in range(len(categories)):
        dashes += "---"
    chart += "    " + dashes + "\n"
    
    # category names
    max_name_length = 0
    for i in cat_name:
        if len(i) > max_name_length:
            max_name_length = len(i)
    for i in range(len(cat_name)):
        if len(cat_name[i]) < max_name_length:
            for j in range(max_name_length - len(cat_name[i])):
                cat_name[i] += " "
            cat_name[i] = cat_name[i]
    temp = []
    for i in range(max_name_length):
        temp2 = ""
        for j in cat_name:
            temp2 += j[i] + "  "
        temp.append(temp2)  
        chart += "     " + temp[i]
        if i != max(0, max_name_length - 1):
            chart += "\n"
    
    return chart

# testing     
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)
# print(auto)

# categories = [food, clothing, auto]
# print(create_spend_chart(categories))

# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# actual = create_spend_chart([business, food, entertainment])
# expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(actual)
# print(expected)