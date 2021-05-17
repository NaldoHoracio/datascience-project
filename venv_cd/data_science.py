# -*- coding: utf-8 -*-
"""
    Criação: 26/04/2021

    Modificação: DD/MM/AAAA

    @author: edvonaldo
"""

import os
import csv
import math
import random
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


#abono_2021 = pd.read_csv(r'datasets/ABONOP_012021.csv', sep=";")
aposentados_nov_2020 = pd.read_csv(r'datasets/APOSENTADOS_112020_FULL.csv', sep=";")
# = pd.read_csv(r'datasets/annual.csv')