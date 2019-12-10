#Created and Initiated by Pranay Joshi
import pandas as pd
data = pd.read_csv("data.csv", usecols=['laboratory', 'coordinate', 'city', 'country', 'contact'])
data.to_csv(r'main.csv')
