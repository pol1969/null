# coding: utf-8
import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date
import json
get_ipython().run_line_magic('ls', '')
data = json.load('lk.json')
with open('lk.json') as data_file:
    data = json.load(data_file)
    
data = json.load("lk.json")
with open("lk.json", "r") as read_file:
    data = json.load(read_file)
    
with open("lk.json", "r") as read_file:
    data = json.load(read_file)
    
data
from pprint import pprint
pprint(data)
