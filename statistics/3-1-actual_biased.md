[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 1b.png shows the result.  In the biased distribution there are fewer low
number of children under 18, and more higher number of children under 18. The
mean for the biased distribution is 2.40, roughly 135% higher (vs. 1.02) than for the unbiased result.
The  mean  of  the  biased  distribution  is  29.1, almost 25% higher than the actual mean.

Python code:

resp = nsfg.ReadFemResp()

#number of children under 18 in household

hist = thinkstats2.Hist(resp.numkdhh)

#plot histogram

thinkplot.Hist(hist)

thinkplot.Show(xlabel='Number of children u18yrs', ylabel='frequency')

#construct pmf, and biased pmf

pmf = thinkstats2.Pmf(hist, label='actual')

biased_pmf = BiasPmf(pmf, label='observed')

#plot actual vs. observed

thinkplot.PrePlot(2)

thinkplot.Pmfs([pmf, biased_pmf])

#thinkplot.Config(xlabel='Number of children u18yrs', ylabel='PMF')

thinkplot.Show(xlabel='Number of children u18yrs', ylabel='PMF')

print('Actual mean', pmf.Mean())

print('Observed mean', biased_pmf.Mean())


Output:

Actual mean 1.02420515504

Observed mean 2.40367910066
