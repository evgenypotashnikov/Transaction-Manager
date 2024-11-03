<p align="center">
      <img src="https://i.ibb.co/HKFSw6T/1.png" alt="Project Logo" width="726">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Engine-Python_3.12.3-purple" alt="Python Version">
   <img src="https://img.shields.io/badge/Version-v1.0 (Alpha)-blue" alt="Version">
   <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

## About
Transaction Manager is a simple command application for managing financial transactions. It allows you to create new transactions, view the balance, income and expenses, and search for transactions by various criteria such as date, category and amount. The application provides a user-friendly interface for entering data and displaying results, which makes it a useful tool for personal financial management.

## Documentation
## Launching the application
After downloading the repository, run the **`main.py`** file using the command **`python main.py`**.

### Method
- **`create_new_transaction`** - The user can create a new transaction by specifying the date, category, amount, and description.
- **`balance`** - The user can view the current balance, which is calculated as the difference between income and expenses.
- **`income`** - The user can view the total amount of income.
- **`expense`** - The user can view the total amount of expenses.
- **`show_all_transaction`** - The user can view a list of all transactions.
- **`search_transaction`** - The user can search for transactions by date, category, or amount.

### Utility Functions
- **`initialization`** - Initializes a directory and file for storing transactions. It creates the directory if it does not exist, opens the file in append mode, and if the file is empty, writes a header with the field names from **`Transaction.fields`** to it.
- **`read`** - reads data from a CSV file by opening it for reading and returning a list of rows from the file using **`csv.DictReader`**.
- **`write`** - writes a new transaction to a CSV file by opening the file in append mode and writing the new transaction data to the file using **`csv.writer`**.

## Developers

- [Evgeny Potashnikov](https://github.com/evgenypotashnikov)

## License
Project GoTo-Apps.TransactionManager is distributed under the MIT license.

