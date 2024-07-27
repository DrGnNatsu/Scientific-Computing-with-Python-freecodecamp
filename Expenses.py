def add_expense(expenses, amount, category):
    # Add the expense to the list of expenses
    # Append: Add an element to the end of the list
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    # lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression.
    # Syntax: lambda arguments : expression
    # map() function returns a map object(which is an iterator) of
    # the results after applying the given function to each item of a given iterable (list, tuple etc.)
    # Syntax: map(function, iterable)
    # sum() function returns the sum of all items in an iterable (list, tuple, etc.)
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    # filter() function constructs an iterator from elements of an iterable for which a function returns true.
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break


if __name__ == '__main__':
    main()
