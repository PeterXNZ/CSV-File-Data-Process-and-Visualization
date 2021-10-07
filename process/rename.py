import csv
import time
import os
import pandas as pd
import numpy as np
import sys
from datetime import datetime
from itertools import islice
from scipy.signal import savgol_filter

for info in os.listdir('''D:\\presen'''):
    domain = os.path.abspath(r'''D:\\presen''')
    info = os.path.join(domain, info)

    data = pd.read_csv(info,error_bad_lines=False)
    le = int(len(data))
    adresse = info
    print(le)
    print(data)

    c=data.iloc[0,1]
    d = data.iloc[4,1]
    e=datetime.fromtimestamp(int(c))
    f = e.strftime("%Y%m%d-%H%M%S")



    print(c)
    print(d)
    print(e)
    print(f)


    os.rename(adresse, adresse+"barrel"+str(d)+"time"+str(f)+".csv")