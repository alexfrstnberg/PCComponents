from Components.DB import Components_DB
import os
from Components.Component import *

Components = Components_DB()

def show_all():
    os.system('cls')
    Components.show()

def update_DB_manually():
    os.system('cls')
    Components.add_item(Component())

def update_DB_automatically(rand = True):
    os.system('cls')
    Components.add_item(Component(rand=rand))
    show_all()

def show_item():
    id = int(input('Enter id: '))
    os.system('cls')
    Components.find_by_id(id)

def show_by_properties():
    name = input('Enter search criteria: ')
    temp = input('Enter value: ').split()
    try: value = [int(x) for x in temp]
    except: value = temp
    os.system('cls')
    Components.find_by_properties(name, value)