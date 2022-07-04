import sys
import time
import datetime
import statistics

sys.path.append("C:/Documents/codecool/python/secure-erp-python-sjafernik")
from model.sales import sales
from view import terminal as view

TODAY = datetime.date.today()

def list_transactions():
    transactions_list = []
    with open(sales.DATAFILE) as f:
        transactions_raw = f.read().splitlines()
    for line in transactions_raw:
        transactions_list.append(line.split(";"))
    view.print_table(sales.HEADERS, transactions_list)


def add_transaction():
    new_transaction = view.get_inputs(["Customer", "Product", "Price", "Date"])
    new_transaction.insert(0, sales.util.generate_id())
    new_transaction_str = ";".join(new_transaction)

    with open(sales.DATAFILE) as f:
        transaction_lines = f.read().splitlines()

    transaction_lines_updated = []
    for item in transaction_lines:
        transaction_lines_updated.append(item)
    transaction_lines_updated.append(new_transaction_str)

    with open(sales.DATAFILE, "w") as f:
        for item in transaction_lines_updated:
            f.write(item + "\n")
    
    print(f"{new_transaction[1]} added")


def update_transaction():
    list_transactions()
    transaction_to_delete = view.get_input("Which transaction would you like to modify? (enter the ID)\n")
    new_transaction = view.get_inputs(["Customer", "Product", "Price", "Date"])
    new_transaction.insert(0, sales.util.generate_id())
    new_transaction_str = ";".join(new_transaction)

    with open(sales.DATAFILE) as f:
        transactions_lines = f.read().splitlines()

    transactions_lines_updated = []
    for item in transactions_lines:
        if item.split(";")[0] != transaction_to_delete:
            transaction_to_delete.append(item)
    transactions_lines_updated.append(new_transaction_str)

    with open(sales.DATAFILE, "w") as f:
        for item in transactions_lines_updated:
            f.write(item + "\n")
    
    print(f"{new_transaction[1]} modified")



def delete_transaction():
    list_transactions()
    transaction_to_delete = view.get_input("Which transaction would you like to delete? (enter the ID)\n")

    with open(sales.DATAFILE) as f:
        transaction_lines = f.read().splitlines()

    transaction_lines_updated = []
    for item in transaction_lines:
        if item.split(";")[0] != transaction_to_delete:
            transaction_lines_updated.append(item)

    with open(sales.DATAFILE, "w") as f:
        for item in transaction_lines_updated:
            f.write(item + "\n")
    
    print(f"{transaction_to_delete} deleted")


def get_biggest_revenue_transaction():
    biggest_revenue_transaction = []
    result = [[], []]
    temp = []

    with open(sales.DATAFILE) as f:
        transactions_lines = f.read().splitlines()
    for index, item in enumerate(transactions_lines):
        if biggest_revenue_transaction == []:
            biggest_revenue_transaction.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") == time.strptime(biggest_revenue_transaction[0].split(";")[2], "%Y-%m-%d"):
            biggest_revenue_transaction.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") < time.strptime(biggest_revenue_transaction[0].split(";")[2], "%Y-%m-%d"):
            biggest_revenue_transaction = []
            biggest_revenue_transaction.append(item)
    for transaction in biggest_revenue_transaction:
        for item in transaction.split(";"):
            temp.append(item)
        result.append(temp)
        temp = []

def get_biggest_revenue_product():
    biggest_revenue_product = []
    result = [[], []]
    temp = []

    with open(sales.DATAFILE) as f:
        transactions_lines = f.read().splitlines()
    for index, item in enumerate(transactions_lines):
        if biggest_revenue_product == []:
            biggest_revenue_product.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") == time.strptime(biggest_revenue_product[0].split(";")[2], "%Y-%m-%d"):
            biggest_revenue_product.append(item)
        elif time.strptime(item.split(";")[2], "%Y-%m-%d") < time.strptime(biggest_revenue_product[0].split(";")[2], "%Y-%m-%d"):
            biggest_revenue_product = []
            biggest_revenue_product.append(item)
    for product in biggest_revenue_product:
        for item in transaction.split(";"):
            temp.append(item)
        result.append(temp)
        temp = []


def count_transactions_between():
    products = view.get_input("Choose product: ")
    result = 0
    with open(sales.DATAFILE) as f:
        transactions_lines = f.read().splitlines()
    for item in transactions_lines:
        if item.split(";")[3].lower() == products.lower():
            result += 1
    view.print_general_results(result, f"Transaction beetwen {products}: ")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
