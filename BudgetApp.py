class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item["amount"]
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount: float, message: str = ""):
        self.ledger.append({"amount": amount, "description": message})

    def withdraw(self, amount: float, message: str = ""):
        self.ledger.append({"amount": -amount, "description": message})
        total = sum([item["amount"] for item in self.ledger])
        if total < amount:
            return False
        return True

    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount: float, category):
        if self.get_balance() < amount:
            return False
        self.withdraw(amount, f"Transfer to {category.category}")
        category.deposit(amount, f"Transfer from {self.category}")
        return True

    def check_funds(self, amount: float):
        return amount < self.get_balance()


def create_spend_chart(categories):
    total = 0
    spent_amounts = []

    # Calculate total spending and each category's spending
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent -= item["amount"]
        spent_amounts.append(spent)
        total += spent

    # Calculate percentage spent by each category
    percentages = [(spent / total * 100) // 10 * 10 for spent in spent_amounts]

    # Draw chart
    draw = 'Percentage spent by category\n'

    for i in range(100, -10, -10):
        draw += f"{str(i).rjust(3)}|"
        for percentage in percentages:
            if percentage >= i:
                draw += " o "
            else:
                draw += "   "
        draw += " \n"

    draw += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length_category_character = max(len(category.category) for category in categories)
    for i in range(max_length_category_character):
        draw += "    "
        for category in categories:
            if len(category.category) > i:
                draw += " " + category.category[i] + " "
            else:
                draw += "   "
        draw += " \n"

    return draw.strip("\n")


if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)
    nail = Category("Nail")
    nail.deposit(1000, "initial deposit")
    nail.withdraw(15)

    print(create_spend_chart([food, clothing, auto, nail]))
