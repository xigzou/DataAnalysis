#Initialize Date
start <- as.Date("2005-01-01")
end <- as.Date("2018-02-15")

getSymbols("BA", src = "yahoo", from = start, to = end)
getSymbols("JPM", src = "yahoo", from = start, to = end)

# test to show the first five rows
head(BA)
head(JPM)

#plot BA.Adjusted Close
plot(BA[ , "BA.Adjusted"], main = "BA and JPM",col="red")

#plot JPM.Adjusted Close (added into the same figure)
lines(JPM[ , "JPM.Adjusted"], col="green")

#computer log return for BA
BA.rtn=diff(log(BA$BA.Adjusted)) 
chartSeries(BA.rtn,theme="white")

#computer log return for JPM
JPM.rtn=diff(JPM$JPM.Adjusted)
chartSeries(JPM.rtn,theme="white")

#Compute summary statistics of BA and JPM
basicStats(BA.rtn) 
basicStats(JPM.rtn)

# Test the normality of the log return of BA and JPM
TBA <- nrow(BA.rtn)
normalTest(BA.rtn[2:(TBA-1)],method='jb') # JB-test

TJPM <- nrow(JPM.rtn)
normalTest(JPM.rtn[2:(TJPM-1)],method='jb') # JB-test
