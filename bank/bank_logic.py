# from dotenv import load_dotenv
# import os
from random import randint

#in case we use a database
# load_dotenv()
# username = os.getenv("username").lower()
# password = os.getenv("password")

# mongo_uri = "mongodb+srv://%s:%s@cluster0.8e22h.mongodb.net/bank?retryWrites=true&w=majority" %(username, password)
# print(mongo_uri)

class Bank:
    '''
    Class for Bank operations - create, get customer details annd transfer;
    Customer details are stored in a list of dictionaries
    '''

    #list of customer details
    customers = []

    def __init__(self):
        pass

    def create(self,name):
        '''
        Create an account for the customer; Returns account number of the customer
        '''
        Account(0)

        #initialise a dictionary for each individual customer
        self.account_dict = {'full_name': Customer(name).name, 'account_number': randint(1000,1099), 'balance': 0 , 'number_of_deposits' : 0, 'number_of_withdrawals' : 0}
        self.customers.append(self.account_dict)
        print("Your account has been created with the following details - " + str(self.account_dict) )
        return self.account_dict['account_number']

    def get_customer(self, acc_number):
        '''Get customer details when account number is provided
        '''
        return [i for i in self.customers if i['account_number'] == acc_number]

    def get_all_customers(self):
        '''
        Return list of all customers as a list
        '''
        return self.customers

    def transfer(self, src, dst, amount):
        '''
        Transfer money from src to dst accounts; All constraints on deposit and withdrawal limis are valid
        '''
        status = False

        # Check if accounts are in the bank db
        if self.get_customer(src) and self.get_customer(dst):
            # if amount exceeds balance
            if amount > self.get_customer(src)[0]['balance']:
                print("Transfer Sunsuccessful : Insufficient funds")
            else:
                #withdrawal limits for src
                if amount < 1000 :
                    print("Minimum withdrawal amount is 1000 for account " + str(src))
                elif amount > 25000:
                    print("Maximum withdrawal amount is 25000 for account " + str(src))
                else:
                    # deposit limits for dst
                    if amount < 500 :
                        print("Minimum deposit amount is 500 for account " + str(dst))
                    elif amount > 50000:
                        print("Maximum deposit amount is 50000 for account " + str(dst))
                    else:
                        # implement transfer
                        self.get_customer(src)[0].update({'balance': self.get_customer(src)[0]['balance'] - amount})
                        # customer_details[0].update({'balance': customer_details[0]['balance'] + amount})
                        self.get_customer(dst)[0].update({'balance': self.get_customer(dst)[0]['balance'] + amount})
                        status = True
        else:
            print("Either one or both account numbers are not valid. Please check them again.")
        if status == True:
            return "Transfer Successful"
        else:
            return "Transfer Unsuccessful"


class Customer:
    '''
    Customer class
    '''
    def __init__(self, name):
        self.name = name

    def get_account(self):
        '''
        Get account number of the customer
        '''
        return self.account_number

class Account:
    '''
    Account class ; Implement deposit, withdrawal, set_balance and get_balance methods
    '''
    def __init__(self, balance:float):
        self.balance = balance

    def set_balance(self, balance):
        '''
        Set balance manually if required. 
        Caution: Not to be used unnecessarily
        '''
        self.balance = balance
        return self.balance
    
    def get_balance(self,account_number):
        ''' Get account balance'''
        return self.balance

    # Counter function to count the number of function calls; Use as a decorator
    # def counter(func):
    #     def wrap(*args,**kwargs):
    #         wrap.calls +=1
    #         if wrap.calls > 3:
    #             print("Maximum attempts exceeded")
    #         else:
    #             print("You have " + str(3 - wrap.calls) + " attempts to {}".format(func.__name__))
    #         return func(*args,**kwargs)
    #     wrap.calls = 0
    #     return wrap
        
    def deposit(self, account_number, amount):
        ''' Deposit money to the account, while keeping the constraints'''

        print("Deposit in progress...")
        if amount< 500 :
            return "Minimum deposit amount is 500"
        elif amount > 50000:
            return "Maximum deposit amount is 50000"
        else:
            customer_details = Bank().get_customer(account_number)
            print(customer_details)
            if self.balance > 100000 :
                print("Deposit Unsuccessful: Maximum allowed balance is 1,00,000")
            else:
                if customer_details[0]['number_of_deposits'] >= 3:
                    print("Maximum deposit attempts exceeded. Please try again later.")
                else:
                    self.balance += amount
                    if len(customer_details) != 0:
                        customer_details[0].update({'balance': self.balance})
                        customer_details[0]['number_of_deposits'] +=1
                        print("Deposit successful. Your balance :" + str(self.balance))
                    else:
                        print("Account number is invalid")
            print(customer_details)
            return customer_details[0]['balance']

    def withdraw(self, account_number, amount):
        ''' Withdraw money from the account, while keeping the constraints'''

        print("Withdrawal in progress...")
        if amount > self.balance:
            return "Withdrawal Unsuccessful: Insufficient funds"
        else:
            if amount < 1000 :
                return "Minimum withdrawal amount is 1000"
            elif amount > 25000:
                return "Maximum withdrawal amount is 25000"
            else:
                customer_details = Bank().get_customer(account_number)
                if customer_details[0]['number_of_deposits'] > 3:
                    print("Maximum deposit attempts exceeded. Please try again later.")
                else:
                    self.balance -= amount
                    if self.balance < 0 :
                        print("Withdrawal Unsuccessful: Minimum balance should be 0")
                    else:
                        print(customer_details)
                        if len(customer_details) != 0:
                            customer_details[0].update({'balance': customer_details[0]['balance'] - amount})
                            print("Withdrawal successful. Your balance :"+ str(customer_details[0]['balance']))
                            customer_details[0]['number_of_withdrawals'] +=1
                        else:
                            return "Account number is invalid"
                print(customer_details)
                return customer_details[0]['balance']

# Following lines have been commented so as to prevent clashes with unit testing (tests.py)
# Uncomment the below lines of code to run as a stand alone python program

# myobj = Bank()
# print(myobj.create("ABC"))
# print(myobj.create("XYZ"))
# print(myobj.get_all_customers())

# acc1 = myobj.get_all_customers()[0]['account_number']
# acc2 = myobj.get_all_customers()[1]['account_number']
# account_obj1 = Account(myobj.get_all_customers()[0]['balance'])
# account_obj2 = Account(myobj.get_all_customers()[1]['balance'])

# Account1
# print(account_obj1.deposit(acc1,30000))
# print(account_obj1.deposit(acc1,3000))
# print(account_obj1.deposit(acc1,3000))
# print(account_obj1.deposit(acc1,3000))
# print(account_obj1.withdraw(acc1, 52000))

# # Account2
# print(account_obj2.deposit(acc2,30000))
# print(account_obj2.withdraw(acc2, 3000))

# print(myobj.transfer(acc1,acc2,70000))

# print(myobj.get_all_customers())