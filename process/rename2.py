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

    g=len(adresse)

    #print(g)

    new=adresse[int(g-35):g]
    new2=adresse[0:10]
    #print(adresse)
    #print(new)
    #print(os.path.basename(adresse))
    #print(os.path.dirname(adresse))
    g=os.path.dirname(adresse)
    h=os.path.basename(adresse)
    print(new2)
    #print(h)




    os.rename(adresse, new2+new)