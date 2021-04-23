# Registeration - Email, First name , Last name, Password


database = {
    2930892176: ['Tolulope', 'Soile', 'tolupraize@gmail.com', 'teebee', 0],
    5245930334: ['Temilade', 'Williams', 'tolexy4rill@yahoo.com', 'xyz', 0]
}

import re
import datetime as dt
import random


def init():
    print('Thank You For CHOOSING Zuri!')
    print('Do you have an account with us?')
    haveaccount = (input('Enter "1" to "Log In" or "2" to "Sign Up/ Create an Account with Zuri" \n'))
    while True:
        try:
            int(haveaccount)
            if haveaccount == str(1):
                login()
            elif haveaccount == str(2):
                register()
            else:
                print('Invalid Option. Try again')
                init()
        except ValueError:
            print('Select a valid option')
            init()
            return False


def check(email):
    is_email_valid = re.search('^\w+@\w+.\w+$', email)
    if is_email_valid:
        return True
    else:
        print('Please make sure that you have "@" and "." in your email and the length of your mail is at least 6 characters long.')
        register()
        return False
        login()


def register():
    print('Kindly enter your details to create an account with Zuri!')
    email = input('Enter your email address here \n')
    check(email)
    first_name = input('Enter your First Name \n')
    last_name = input('Enter your Last Name \n')
    password = input('Kindly enter a password \n')
    accountnumber = accountnumbergenerator()

    database[accountnumber] = [first_name, last_name, email, password, 0]
    print(f'Dear {last_name} {first_name}, Your account has been created successfully. Thank you!')
    print(' == ==== ====== ========')
    print('Your account number is: %d' % accountnumber)
    print(' == ==== ====== ========')
    print('Make sure you keep your details safe')
    print(' == ==== ====== ========')

    login()


def login():
    print('Kindly Enter Your Details to Log Into Your Account')
    useracctnumber = input('Pls Enter Your 10 Digit Account Number \n')
    is_valid_account_number = account_number_validation(useracctnumber)
    if is_valid_account_number:
        password = input('Enter your Password \n')

        for accountnumber, userDetails in database.items():
            if accountnumber == int(useracctnumber):
                if userDetails[3] == password:
                    bankoperation(userDetails)
        print('Invalid account number or Password')
        login()
    else:
        init()


def account_number_validation(accountnumber):
    if accountnumber:

        if len(str(accountnumber)) == 10:
            try:
                int(accountnumber)
                return True

            except ValueError:
                print('Invalid Account number. Account number should be an integer')
                return False
        else:
            print('Account number cant be more or less than 10 digits and should contain only numbers')

    else:
        print('account number is required')
        return False
    # check if acct no is not empty and 10 digits and  if the acct number is an inter


def bankoperation(user):
    print("Welcome! %s %s" % (user[0], user[1]))

    current_datetime = dt.datetime.now()
    print(current_datetime)

    selectedOption = input('What would you like to do? Enter 1 to Deposit, 2 to Withdraw, 3 to lay a Complaint \n')
    while True:
        try:
            int(selectedOption)
            if selectedOption == str(1):
                deposit(user)
            elif selectedOption == str(2):
                withdrawal(user)
            elif selectedOption == str(3):
                complaint(user)
            elif selectedOption == str(4):
                cancel()
            else:
                print('Invalid Selection! Please Try Again')
                bankoperation(user)
        except ValueError:
            print('Select a valid option')
            bankoperation()
            return False


def deposit(user):
    print('How much will you like to deposit?\n')
    depositmax = 100000
    while True:
        try:
            deposithere = int(input('Amount must be in multiples of NGN 100 \n'))
            if deposithere <= depositmax:
                print('Your deposit of %s Naira was successful' % deposithere)
                print(' == ==== ====== ========')
                balance = user[4]
                currentbalance = deposithere + balance
                print('Your current balance is %d' % currentbalance)
                option()
            elif deposithere:
                print('You cant deposit more than 100000 at once NGN')
                deposit(user)
            else:
                print('invalid! Try again')
                deposithere = input('Amount must be in multiples of NGN 100 \n')

        except ValueError:
            print(' Error! Select a valid option')
            bankoperation(user)
            return False


def withdrawal(user):
    print("How Much Will You Like To Withdraw? \n")
    balance = user[4]
    while True:
        try:
            withdrawalAmount = int(input('Amount must be multiples of NGN 500 \n'))
            if (withdrawalAmount <= balance):
                print('Take your cash!')
                currentbalance = balance - withdrawalAmount
                print('Your current balance is %d' % currentbalance)
                option()

            else:
                withdrawalAmount > balance
                print('Insufficient Funds')
                print('Your Current Balance is %d NGN' % balance)
                option()

        except ValueError:
            print(' Error! Select a valid option')
            bankoperation(user)
            return False


def complaint(user):
    print('What issue will you like to report?')
    complain = input('Type complaint in 300 words or less\n')
    if 0 < len(complain) <= 300:
        print('Thank you for contacting us! Our support team will reach out via mail')
        option()
        print('Error! Please fill box with at least not more than 300 words')
        option()


def accountnumbergenerator():
    return random.randrange(2200000000, 9999999999)


def option():
    selectoption = input('Do you want to perform another transaction? Yes, Enter 1. No, Enter 2 \n')
    while True:
        try:
            int(selectoption)
            if selectoption == str(1):
                login()
            elif selectoption == str(2):
                print('Thanks for CHOOSING Zuri Goodbye')
                exit()
        except ValueError:
            print('Invalid! Select a Valid Option')
            option()
            return False

    else:
        print('Invalid Selection! Please Try Again')
        selectoption = input('Do you want to perform another transaction')


# After every successful transaction, you have to log in to carry out another.


def cancel():
    print('Thank you! Goodbye')
    exit()


init()
