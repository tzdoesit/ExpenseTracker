
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def list_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]} | Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))

def filter_expense_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nWelcome to your expense tracker. \n\nMenu:')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Print total expenses')
        print('4. Filter expense by category')
        print('5. Exit')

        choice = input('\nPlease select an option: ')

        if choice == '1':
            print("You selected 'Add an expense'")
            amount = float(input('Please enter an amount: '))
            category = input('Please enter a category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            list_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Please enter a category you would like to filter: ')
            filtered_by_expenses = filter_expense_by_category(expenses, category)
            list_expenses(filtered_by_expenses)

        elif choice == '5':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()
