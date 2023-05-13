# Code explanation for prediction of CO2 emissions for India with/without carbon pricing

## Analysis.py
To install the required libraries run the following commands
`pip3 install pandas
pip3 install numpy
pip3 install matplotlib`

The dataset for yearwise CO2 emissions of countries from 1990 to 2019 was downloaded from this [link](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC)
The code has been fully commented explaining each line. 

To visualise the plots for different countries, enter the relevant country name in the data.loc field.
I have made a lineplot for visualisation, to get a scatter plot(for discrete values) use plt.scatter(x,y) instead of plt.plot(x,y)
