## About
- This python program is an implementation of a payment banking solution
- The following methods have been implemented - 
    - create account
    - deposit
    - withdraw
    - get_balance
    - transfer
- The following constraints/conditions have been considered while implementing -
    - Account balance cannot exceed ₹1,00,000
    - Account balance cannot be less than ₹0
    - The minimum deposit amount is ₹500 per transaction
    - The maximum deposit amount is ₹50,000 per transaction
    - The minimum withdrawal amount is ₹1,000 per transaction
    - The maximum withdrawal amount is ₹25,000 per transaction
    - No more than 3 deposits are allowed in a day
    - No more than 3 withdrawals are allowed in a day
    - Account number entered during deposit or withdrawal should be valid
    - Account has sufficient balance during withdrawals 

## Steps to run the program
- Install requirements using ```pip install -r requirements.txt```. It is recommended that you use a ```virtualenv```
- If you choose to run the program directly, make necessary changes/uncomment the lines at the bottom and run    ```python bank_logic.py``` on your terminal. The output is printed on the terminal.
- If you choose to do unit testing, go to ```/bank``` directory, run ```pytest -q tests.py```. Make necessary changes in the test file accordingly.