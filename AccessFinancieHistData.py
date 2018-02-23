import pandas as pd
import pandas_datareader.data as web 
import datetime
import matplotlib.pyplot as plt   # Import matplotlib
import pylab
import numpy as np
 
#stock prices starting from 01/01/2005 to 02/15/2018
start = datetime.date(2005,1,1)
end = datetime.date(2018,2,15)
 
# First argument is the stock symbol, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
BoeingCompany = web.DataReader('BA', "yahoo", start, end)
JPMorganChase = web.DataReader('JPM', "yahoo", start, end)

# Test the variable type
type(BoeingCompany)
type(JPMorganChase)

# Test if the data is read and display the default first 5 data(leave blank).
BoeingCompany.head()
JPMorganChase.head()

# DataFrame consisting of the adjusted closing price of Boeing Company and JPMorgan
adjClose = pd.DataFrame({"Boeing Company": BoeingCompany["Adj Close"],
                      "JPMorgan Chase": JPMorganChase["Adj Close"]
                      })
#Test the variable display result
adjClose.head()

#Plot them in the same figure					  
adjClose.plot(grid = True)
pylab.ylabel('Adj Close**')
pylab.title('Boeing Company (BA) V.S. JPMorgan Chase & Company (JPM)')
plt.show()

# Let's use NumPy's log function, though math's log function would work just as well
log_return_change = adjClose.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
log_return_change.head()
log_return_change.plot(grid = True).axhline(y = 0, color = "black", lw = 2)
pylab.ylabel('Log Return')
pylab.title('Boeing Company (BA) V.S. JPMorgan Chase & Company (JPM)')
plt.show()
