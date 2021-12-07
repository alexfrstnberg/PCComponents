from dateutil.parser import parse
from random import choice
from Components.stuff import *
import datetime


class Component:
    '''Represents the PC components'''

    def __init__(self, name='', country='', prod_date='', price=0, quantity=0, rand=False):
        
        if rand: self.component_update(choice(names), choice(countries), random_date(),
                                    randint(500, 5000), randint(1, 200), choice(['Some cool stuff', '']))
        else: self.component_update(name, country, prod_date, price, quantity)

    def name_update(self, new_name): self.name = new_name

    def country_update(self, new_country): self.country = new_country

    def prod_date_update(self, new_prod_date):
        if isinstance(new_prod_date, datetime.date): 
            self.prod_date = new_prod_date
        else: 
            try: self.prod_date = parse(new_prod_date).strftime("%m/%d/%Y")
            except: self.prod_date = ''

    def price_update(self, new_price): self.price = new_price

    def quantity_update(self, new_quantity): self.quantity = new_quantity

    def properties_update(self, new_properties): self.properties = new_properties

    def component_update(self, name: str, country: '', prod_date = None, 
                    price = 0, quantity = 0, properties = ''):
        self.name_update(name)
        self.country_update(country)
        self.prod_date_update(prod_date)
        self.price_update(price) 
        self.quantity_update(quantity)

    def input_info(self):
        self.component_update(input('Enter component info:\nName: '), input('Manufacturer country: '),
                         parse(input('Pruduction date: ')), int(input('Price:')),
                         int(input('Quantity: ')))
        








        

        