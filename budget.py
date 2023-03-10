def getTotals(categories):
  total = 0
  breakdown = []
  for category in categories:
    total += category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded = list(map(lambda x: truncate(x / total), breakdown))
  return rounded


def truncate(n):
  multiplier = 10
  return int(n * multiplier) / multiplier


def create_spend_chart(categories):  #returns string in bar chart form
  res = "Percentage spent by category\n"
  i = 100
  totals = getTotals(categories)
  while i >= 0:
    cat_spaces = " "  #one space
    for total in totals:
      if total * 100 >= i:
        cat_spaces += "o  "  #will look like: _o__o_ ...
      else:
        cat_spaces += "   "  #3 spaces
    res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i -= 10

  dashes = "-" + "---" * len(categories)
  names = []
  x_axis = ""
  for category in categories:
    names.append(category.name)

  maxi = max(names, key=len)

  for x in range(len(maxi)):
    nameStr = '     '  #5 spaces
    for name in names:
      if x >= len(name):
        nameStr += "   "  #3 spaces
      else:
        nameStr += name[x] + "  "  #2 spaces

    if (x != len(maxi) - 1):
      nameStr += '\n'

    x_axis += nameStr

  res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
  return res


class Category:

  def __init__(self, name):
    self.name = name  #instantiation
    self.ledger = list()

  def __str__(self):
    title = f"{self.name:*^30}\n"  #name of category
    items = ""  #definition
    total = 0
    for item in self.ledger:  #print items and cost
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      #^item description with format in terms of how many characters to display
      total += item['amount']


#adding up all amounts of items to acquire total.
    output = title + items + "Total: " + str(total)  #final correct format
    return output

  def deposit(self, amount, description=""):  #empty desc by default
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)
        ):  #see if we have enough money in acc, if so, withdraw
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    total_cash = 0  #calculate total cash by adding all amounts
    for item in self.ledger:
      total_cash += item["amount"]

    return total_cash

  def transfer(self, amount, category):
    if (self.check_funds(amount)):  #ensure we have enough money in the acc
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if (
        self.get_balance() >= amount
    ):  #ensure we have more moeny in acc than what we're asking for the transaction
      return True
    return False

  def get_withdrawls(self):  #gets total amount spent
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total
