from bank import bank_logic
import pytest

obj_bank = bank_logic.Bank()
obj_account = bank_logic.Account(0)
obj_bank.create('ABC')
obj_bank.create('XYZ')
account_number1 = obj_bank.get_all_customers()[0]['account_number']
account_number2 = obj_bank.get_all_customers()[1]['account_number']


def test_create():
    assert obj_account.get_balance(obj_bank.customers[0]['account_number']) == 0
    test_balance_limit()

def test_get_all_customers():
    assert type(obj_bank.get_all_customers()) == list
    assert type(obj_bank.get_all_customers()[0]) == dict

def test_deposit():
    assert obj_account.deposit(account_number1, 200) == "Minimum deposit amount is 500"
    assert obj_account.deposit(account_number1, 52000) == "Maximum deposit amount is 50000"
    assert obj_account.deposit(account_number1, 10000) == 10000 # test if balance is 10000 after deposit
    test_balance_limit()

def test_withdraw():
    assert obj_account.withdraw(account_number1,11000) == "Withdrawal Unsuccessful: Insufficient funds" 
    assert obj_account.withdraw(account_number1,500) == "Minimum withdrawal amount is 1000"

    # NOTE : To run the below test case, deposit amount greater than 26000
    # -- assert obj_account.withdraw(account_number1,25500) == "Maximum withdrawal amount is 25000"--

    assert obj_account.withdraw(account_number1,1000) == 9000 # test if balance is 9000 after valid withdrawal
    test_balance_limit()

def test_balance():
    assert obj_account.get_balance(account_number1) == 9000
    test_balance_limit()

def test_balance_limit():
    assert obj_account.get_balance(account_number1) < 100000 and obj_account.get_balance(account_number1) >= 0

def test_deposit_limit():
    assert obj_account.deposit(account_number1, 200) == "Minimum deposit amount is 500"
    assert obj_account.deposit(account_number1, 75000) == "Maximum deposit amount is 50000"
    test_balance_limit()

def test_withdrawal_limit():
    assert obj_account.withdraw(account_number1, 200) == "Minimum withdrawal amount is 1000"

    # NOTE : To run the below test case, deposit amount greater than 26000
    # assert obj_account.withdraw(account_number1, 75000) == "Maximum withdrawal amount is 25000"

    test_balance_limit()

def test_transfer():
    assert obj_bank.transfer(account_number1,account_number2, 1000) == "Transfer Successful"
    assert obj_bank.transfer(account_number1,account_number2, 500) == "Transfer Unsuccessful"
    assert obj_bank.transfer(account_number1,account_number2, 12000) == "Transfer Unsuccessful"
    # NOTE : To run the below test case, deposit amount greater than 26000
    # assert obj_bank.transfer(account_number1,account_number2, 26000) == "Transfer Unsuccessful"
    assert obj_bank.transfer(account_number1,account_number2, 200) == "Transfer Unsuccessful"
    # assert obj_bank.transfer(account_number1,account_number2, 52000) == "Transfer Unsuccessful"


