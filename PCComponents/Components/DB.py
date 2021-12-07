import pandas as pd
from tabulate import tabulate
from Components.Component import * 
from random import choice
from Components.stuff import *
import datetime

class Components_DB:
    '''Needed to work in console only'''

    def __init__(self, size = 3):   
        global names
        self.size = size
        self.list = [Component(rand=True) for _ in range(size)]

    
    def table(self):
        return pd.DataFrame([vars(i) for i in self.list], index = [x for x in range(self.size)])   
    
    def show(self):
        print(tabulate(self.table(), headers = 'keys', tablefmt = 'grid'))

    def add_item(self, item):
        self.size += 1
        self.list.append(item)

    def update_item(self, id, name: str, country: '', prod_date = None, price = 0, quantity = 0, properties = ''):
        self.list[id].component_update(name, country, prod_date, price, quantity, properties)

    def remove_item(self, id):
        self.size -= 1
        self.list.pop(id)

    def find_by_id(self, id):
        print(tabulate(self.table().loc[id:id], headers = 'keys', tablefmt = 'grid'))

    def find_by_properties(self, name, props):
        print(tabulate(self.table()[self.table()[name].isin(props)]))