#Needed to work in console only

from Components.Features import *

def exit_the_program():
    exit()

def errhandler():    
    print("not sure what you want")

actions = {'1':show_all,
    '2':update_DB_manually, 
    '3':update_DB_automatically, 
    '4':show_item, 
    '5':show_by_properties, 
    'x':exit_the_program}

selectedaction = None
def show_menu():
    global selectedaction
    for key in actions: 
        print (key + '. ', actions[key].__name__)
    selectedaction = input("please select an option from the list:    ")

#show_menu()

while True:
    show_menu()
    actions.get(selectedaction, errhandler)()
    print()
exit()