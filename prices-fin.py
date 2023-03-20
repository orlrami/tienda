#Import Inv, log and tax
#1st cd line quit sell register
#
#
#
import os
import csv
import time
import datetime
import sys
import random
import math
import string

os.chdir('C:\\Users\\rami298861\\Documents\\CIS 155 TIENDITA')
import Inv
import log
import tax


#creating register function, it assigns prices to the items in the inventory (file is on the making), enters value in csv file with id and price. and logs the action. If choose 1, asks for id, if 2 quits
def register():
    
    print('\\Register\\')
    print('Enter 1 for Registering a Product, enter 2 to quit')
    choice = input()
    if choice == '1':
        print('Enter the ID of the product')
        id = input()
        print('Enter the price of the product')
        price = input()
        Inv.setPrice(id, price)
        log.log('Register', id)
        register()
    if choice == '2':
        print('Quitting Register')
        return
    else:
        print('Invalid input')
        register()
        