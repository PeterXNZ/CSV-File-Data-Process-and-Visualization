import csv
import os
import pandas as pd
import numpy as np
import sys
from itertools import islice
from scipy.signal import savgol_filter

for info in os.listdir('''D:\\presen'''):
    domain = os.path.abspath(r'''D:\\presen''')
    info = os.path.join(domain, info)

    data = pd.read_csv(info, skip_blank_lines=False)
    le = int(len(data))
    adresse = info
    #print(data)

    if os.path.exists(adresse):
        with open(adresse, "r") as f:
            y = np.array(data)

            #print(y)
            d = y.tolist()
            f=data.columns.tolist()
            print(d[1])
            nums = []
            print(d[3][1])
            print(d[5][1])
            if (len(d[1])):
                print(len(d[1]))
            #print(f)
            #print(f[2])
            h= (d[5][1] + d[3][1] ) / 2
            #nums.append(h)
            #print(nums)
            k=0
            s=0
            for i in range(2, 8):
                if d[i][2] > 0:
                    # print(d[i][j])

                    k = k + 1
            print(k)
            #print(h)
            for j in range (0,1024):

                    for i in range(2,8):
                        if d[i][2]>0:
                           #print(d[i][j])
                           s=s+d[i][j]
                           #print(s)
                    if k>0:
                     nums.append(s / k)
                     s=0



            #print(nums)

        with open(adresse, "w", newline='') as out:

            writer = csv.writer(out)
            writer.writerow(f)
            if k>0:
             writer.writerow(nums)


