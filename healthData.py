#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
#=====================================HHC
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.healthcare.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.healthcare.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("fzk2-tfxn", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

HHC_df.to_csv("healthData.csv")

#=====================================Community Health Survey========================
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
CHS_results = client.get("hw9t-9zpc", limit=2000)

# Convert to pandas DataFrame
CHS_df = pd.DataFrame.from_records(CHS_results)
