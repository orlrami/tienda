import os
import csv
import time
import datetime
import sys
import random
import math
import string

os.chdir('C:\\Users\\rami298861\\Documents\\CIS 155 TIENDITA')

#register function
def register():
    print('Registering product')
    print('Please enter the product id')
    id = input()
    print('Please enter the product price')
    price = input()
    with open('inv.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == id:
                product = row[1]
                print('Product found')
                print('Product name: ' + product)
                print('Product id: ' + id)
                print('Product price: ' + price)
                print('Is this correct?')
                print('1. Yes')
                print('2. No')
                answer = input()
                if answer == '1':
                    with open('prices.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',')
                        writer.writerow([id, product, price])
                        print('Product registered')
                        # Logging the action in the log file
                        log_message = f"Product registered: {product} {id} {price} {time.strftime('%X %x %Z')}\n"
                        with open('log.txt', 'a') as log:
                            log.write(log_message + '\n') 
                if answer =='2':
                    print('Try again')
                    log_message = f"Product doesn't equal the id: {id} {time.strftime('%X %x %Z')}\n"
                    with open('log.txt', 'a') as log:
                         log.write(log_message + '\n') 



#selling function, 
def sell():
      print('Selling product')
      id = input('Please enter the product id: ')
      with open('prices.csv', 'r') as csvfile:
          reader = csv.reader(csvfile, delimiter=',')
          for row in reader: 
              if row[0] == id:
                    product = row[1]
                    price = row[2]
                    print('Product found')
                    print('Product name: ' + product)
                    print('Product id: ' + id)
                    print('Product price: ' + price)
                    answer = input('Is this correct? (1. Yes / 2. No): ')
                    if answer == '1':
                            money = input('Please enter the amount of money the client is giving: ')
                            try:
                                money = float(money)
                                break
                            except ValueError:
                                    print('Invalid input. Please enter a valid number.')
                            change = money - float(price)
                            print('The change is ' + str(change))
                    # Logging the action in the log file
                    log_message = f"Product sold: {product} {id} {price} {time.strftime('%X %x %Z')}\n"
                    with open('log.txt', 'a') as log:
                        log.write(log_message + '\n')

def quit():
    print('Quitting')
    sys.exit()

# Create the log file if it doesn't exist
if not os.path.exists('log.txt'):
    with open('log.txt', 'w') as log:
        log.write('Log file created: ' + time.strftime('%X %x %Z') + '\n')  

        log.write('Log file created: ' + time.strftime('%X %x %Z') + '')

# Create the prices file if it doesn't exist
if not os.path.exists('prices.csv'):
    with open('prices.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['id', 'product', 'price'])

def main_menu():
    print("Welcome to Prices")
    print("Please Press")
    print("1 for Registering a Product")
    print("2 for Selling a Product")
    print("3 to quit")
    answer = input()
    if answer == '1':
        register()
    if answer == '2':
        sell()
    if answer == '3':
        quit()

main_menu()
