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

    data = pd.read_csv(info,skiprows=9)
    le = int(len(data))
    adresse = info
    print(le)
    print(data)


    def transform_minMaxScale(a):

        Maximum = float(a[0])
        for i in range(0, le):
            if float(a[i]) > Maximum:
                Maximum = float(a[i])

        Minimum = float(a[0])
        for i in range(0, le):
            if float(a[i]) < Minimum:
                Minimum = float(a[i])

        for j in range(0, le):
            a[j] = (float(a[j]) - Minimum) / (Maximum - Minimum)

        return a


    def isNoisy(c):
        sum = 0
        noiseThreshold = 0.02
        for i in range(0, le - 1):
            if abs(float(c[i + 1]) - float(c[i])) >= 0:
                sum += abs(float(c[i + 1]) - float(c[i]))
                if sum / (le - 1) >= noiseThreshold:
                    return True


    def process_smooth(e):

        e = savgol_filter(e, 51, 3)

        return e


    def clean_removeArtifacts(d):
        for i in range(1, le - 1):
            if int(d[i] - d[i - 1]) > 200 | int(d[i + 1] - d[i]) > 200:
                return True


    def isClipping(e):
        count = 0
        for i in range(0, le - 1):
            if (e[i] >= 60000):
                count = count + 1
        if count > 5:
            return True


    if os.path.exists(adresse):
        with open(adresse, "r") as f:
            y = np.loadtxt(adresse, delimiter=',', skiprows=10)
            p = y.T

            d = p.tolist()
            nums = []
            print(d)


            for l, i in enumerate(d):
                if l >=1 and i != []:
                        transform_minMaxScale(i)
                        print(l)
                        print("transformed")

            for l, i in enumerate(d):
                if l >=1 and i != []:
                    if isNoisy(i):
                        print(l)
                        print("isNoisy")
                        nums.append(l)

            for l, i in enumerate(d):
                if l >=1 and i != []:
                    if clean_removeArtifacts(i):
                        print(l)
                        print("removeArtifacts")
                        nums.append(l)

            for l, i in enumerate(d):
                if l >=1 and i != []:
                        process_smooth(i)
                        print(l)
                        print("smoothed")

            for l, i in enumerate(d):
                if l >=1 and i != []:
                    if isClipping(i):
                        print(l)
                        print("Clipping")
                        nums.append(l)






            for i in range(len(nums)):
                d[nums[i]] = []

            print(d)

        with open(adresse, "w", newline='') as out:
            writer = csv.writer(out)
            for row in d:
                writer.writerow(row)

