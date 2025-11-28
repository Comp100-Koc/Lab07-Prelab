# Lab 07: List and Dictionary Prelab

# Question 1: Custom Sorting of Nested Dictionaries
You are given a list of dictionaries. Each dictionary represents a person with fields like `name`, `age`, `salary`, and `address`. The address field is itself a dictionary containing `city` and `zip_code`.

## Requirements:
Write a function `custom_sort(people, primary, secondary)` that sorts the list of people based on the following rules:
- Sort by primary field in **ascending** order.
    - If two people have the same value for the primary field, sort them by the secondary field.
    - If the secondary field is also identical, sort them by `name`.
    - the fields that are in address will be input with a `.` like `adress.zip_code`
## Example Input:
```python
people = [
    {'name': 'Alice', 'age': 30, 'salary': 75000, 'address': {'city': 'New York', 'zip_code': 10001}},
    {'name': 'Bob', 'age': 25, 'salary': 62000, 'address': {'city': 'Boston', 'zip_code': 20001}},
    {'name': 'Charlie', 'age': 25, 'salary': 68000, 'address': {'city': 'Boston', 'zip_code': 15001}},
    {'name': 'David', 'age': 30, 'salary': 90000, 'address': {'city': 'New York', 'zip_code': 20002}}
]
primary = 'age'
secondary = 'address.zip_code'
```

## Example Output:
```python
[
    {'name': 'Charlie', 'age': 25, 'salary': 68000, 'address': {'city': 'Boston', 'zip_code': 15001}},
    {'name': 'Bob', 'age': 25, 'salary': 62000, 'address': {'city': 'Boston', 'zip_code': 20001}},
    {'name': 'Alice', 'age': 30, 'salary': 75000, 'address': {'city': 'New York', 'zip_code': 10001}},
    {'name': 'David', 'age': 30, 'salary': 90000, 'address': {'city': 'New York', 'zip_code': 20002}}
]
```
# Question 2: Compute Order Receipt
Write a function `compute_bill` that calculates the total price for a list of ordered items, updating the stock by decrementing the count of each item that is successfully billed. The function will only bill the items that are available in stock, and any items out of stock will be ignored.

## Implementation Method: 
Iterates through the order list, checks stock, computes total cost, and decrements stock. Returns total cost.

## Inputs: 
- The function takes an order list, which contains the items ordered by their names (e.g., `["ram", "ssd", "monitor"]`).
- The function relies on two dictionaries, stock and prices:
- stock: This dictionary holds the current stock level for each hardware item.

```python
stock = {
    "ram": 6,
    "ssd": 0,
    "monitor": 32,
    "power_supply": 15,
    "keyboard": 20
}
```

- prices: This dictionary stores the price for each hardware item.

```python
prices = {
    "ram": 55,
    "ssd": 90,
    "monitor": 220,
    "power_supply": 35,
    "keyboard": 25
}
```

- Sample Input: 
```python
order = ["ram", "ssd", "monitor"]
```

## Output:
- The function returns the total price of the items -`total (float)`- in the order that are available in stock.
- The stock dictionary is updated to reflect the reduced quantities of the items that were billed. 
- Note: stock dictionary is not an output of the function, it is updated as result of your function.
- Sample Output:
    - `compute_bill(order)` Output: `275`
    - Updated stock: `{"ram": 5, "ssd": 0, "monitor": 31, "power_supply": 15, "keyboard": 20}`

# Question 3: Monthly Balance Calculator
Write a function `generate_monthly_report` that is is designed to group a list of transactions by month, calculate the total credits and debits for each month, and compute the net balance for each month. It generates a report in the form of a dictionary with monthly breakdowns.

## Inputs:
The function takes a list of transactions. Each transaction is represented by a dictionary with the following fields:
- `id`: A unique identifier for the transaction.
- `type`: A string that indicates the type of transaction, either 'credit' or 'debit'.
- `amount`: A numerical value representing the amount involved in the transaction.
- `timestamp`: A string representing the date of the transaction in the format YYYY-MM-DD.
- Sample Input:
```python
transactions = [
    {'id': 1, 'type': 'credit', 'amount': 500, 'timestamp': '2024-01-05'},
    {'id': 2, 'type': 'debit', 'amount': 300, 'timestamp': '2024-01-10'},
    {'id': 3, 'type': 'credit', 'amount': 700, 'timestamp': '2024-01-15'},
    {'id': 4, 'type': 'credit', 'amount': 900, 'timestamp': '2024-02-01'},
    {'id': 5, 'type': 'debit', 'amount': 400, 'timestamp': '2024-02-05'}
]
```
## Output:
The function returns a dictionary where the keys are the months in YYYY-MM format, and the values are dictionaries with:
- `total_credit`: Total amount of credits for that month.
- `total_debit`: Total amount of debits for that month.
- `net_balance`: The difference between total_credit and total_debit (i.e., total_credit - total_debit).

After processing all transactions, the function returns a regular dictionary containing the summary for each month. The dictionary has the structure:
```python
{
    'YYYY-MM': {'total_credit': <total>, 'total_debit': <total>, 'net_balance': <balance>}
}
```
Sample Output:
```python
'2024-01': {'total_credit': 1200, 'total_debit': 300, 'net_balance': 900},
'2024-02': {'total_credit': 900, 'total_debit': 400, 'net_balance': 500}
...
```

