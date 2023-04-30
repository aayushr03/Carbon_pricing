import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
df=pd.read_csv("China_emis.csv")
df1=pd.read_csv("India_emis.csv")
popind=pd.read_csv("India_pop.csv")
popchin=pd.read_csv("Chin_pop.csv")
for i in range (0,30):
    df['Emission in kT'][i]=df['Emission in kT'][i]/popchin['Population'][i]
for i in range (0,30):
    df1['Emission in kT'][i]=df1['Emission in kT'][i]/popind['Population'][i]    
df.set_index('Year',inplace=True)
df1.set_index('Year',inplace=True)
result = adfuller(df['Emission in kT'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
model = ARIMA(df['Emission in kT'], order=(1,2,2))
results = model.fit()
predictions = results.predict(start=0, end=41)
model1=ARIMA(df1['Emission in kT'], order=(1,2,2))
results1 =model1.fit()
predictions1=results1.predict(start=0,end=41)
plt.plot(predictions1, color='red')
plt.show()