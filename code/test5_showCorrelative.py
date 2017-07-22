# -*- coding: UTF-8 -*-
import pandas as pd

data = pd.read_csv('data_frame.txt', sep='\t')

print(data.corr())