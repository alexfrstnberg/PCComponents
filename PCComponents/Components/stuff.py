from random import randint
from dateutil.parser import parse
from datetime import datetime

names = ['Motherboard', 'CPU', 'GPU', 'RAM', 'Cooling', 
        'SSD', 'HDD', 'NVME', 'PSU', 'Mouse', 'Keyboard', 'Monitor']
countries = ['China', 'USA', 'Canada', 'Japan', 'South Korea']

def random_date(start = '01.01.2000', end = str(datetime.now())):
    '''Generates random date'''

    from_date = int(parse(start).timestamp())
    to_date = int(parse(end).timestamp())
    return datetime.fromtimestamp(randint(from_date, to_date)).date()
