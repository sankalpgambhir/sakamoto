# bot.py
# Copyright 2020 Sankalp Gambhir

# Comment format
# <Description>. %<Expected_Type>

import os
from sakamoto_client import *


if __name__ == '__main__':
    # login to discord only if this is the head process
    client = sakamoto_client(env)