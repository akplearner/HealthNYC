import csv
import pandas as pd

healthSurv = pd.read_csv('/home/akp1/Documents/HealthNYC/DOHMH_Community_Health_Survey__2010-2016_.csv')
diseaseSurv = pd.read_csv('/home/akp1/Documents/HealthNYC/Communicable_Disease_Surveillance_Data.csv')

dsList=diseaseSurv.columns.values
hsList=healthSurv.columns.values

dsList
hsList