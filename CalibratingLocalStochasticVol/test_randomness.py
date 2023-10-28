from statistics import mean
from unittest import result
import pandas as pd
import numpy as np
import os
import tensorflow as tf
import pickle

# get the parent path
parent_dir = os.path.dirname(os.path.abspath(__file__))

#Name of Cali file
calibration_name_1 = 'sim1'
calibration_name_2 = 'sim2'

#File path for finsurf instance
finsurf_path_1 = parent_dir + '\\PastCalibrations\\'  + calibration_name_1 + '\\histData.npz'
finsurf_path_2 = parent_dir + '\\PastCalibrations\\'  + calibration_name_2 + '\\histData.npz'

#READ NPZ FILE
data1 = np.load(finsurf_path_1)
data2 = np.load(finsurf_path_2)

#Get arrrays with payoffs
payoffs_MK_1 = data1['mc_prices_model'] 
payoffs_MK_2 = data2['mc_prices_model'] 

def checkEqual(arr1,arr2):
    #if the length of arrays are different return false
    if np.shape(arr1)!= np.shape(arr2):
        return False
    else:
        #sort both the arrays
        arr1.sort()
        arr2.sort()
        #traverse each index of arrays
        for i in range(len(arr1)):
            #for same index if the value in the sorted arrays are different return false
            if arr1[i]!=arr2[i]:
                return False
    #if none of the above conditions satisfied return true
    return True

print(np.shape(payoffs_MK_1 ))

# checkEqual(payoffs_MK_1 ,payoffs_MK_1)
print("HERE IS SIM 1")
print(payoffs_MK_1 )
print("HERE IS SIM 2")
print(payoffs_MK_2 )