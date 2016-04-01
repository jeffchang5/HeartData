from import_from_csv import *
from numpy import linalg

patient_data = open_csv('data/heart_data.csv')
theta = patient_data[0]
results = patient_data[1]

print((linalg.pinv(theta.transpose() * theta)) * (theta.transpose() * results))



