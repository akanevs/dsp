[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Histograms are shown in 1a.png in the img folder!

First babies: We can see in the figure that the distribution is roughly normal (Gaussian),
with a mode of 7.5lb, and a tail that extends farther to the left than the right. The mean
is 7.2lb, variance is 2.02 and standard deviation is 1.42.

For others, the distribution is again roughly normal with a mode of 7.0lb, and a tail
that extends farther to the left than to the right. The mean is 7.33lb, the variance
is 1.94 and the standard deviation is 1.39. Even though the mode is smaller than for
the first born case, there are also very high frequency of babies with weights between
7 and 8 pounds.

For the pregnancy length, the Cohen distance is 0.029 standard deviations, which is
quite small, while for the birth weight, the Cohen distance is -0.089, which is quite
a bit larger but still small.

-----------------------

Python code:

preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]

#hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')

#thinkplot.Hist(hist)

#thinkplot.Show(xlabel='pounds', ylabel='frequency')

firsts = live[live.birthord == 1]

others = live[live.birthord != 1]

first_hist = thinkstats2.Hist(firsts.prglngth)

other_hist = thinkstats2.Hist(others.prglngth)


#for total weight

first_hist = thinkstats2.Hist(firsts.totalwgt_lb)

other_hist = thinkstats2.Hist(others.totalwgt_lb)

width = 0.25

thinkplot.PrePlot(2, cols=2)

thinkplot.Hist(first_hist, align='center', width=width, label='firsts', color='red')

thinkplot.Config(xlabel='lbs',

ylabel='frequency',

axis=[0, 16, 0, 180])



thinkplot.PrePlot(2)

thinkplot.SubPlot(2)

thinkplot.Hist(other_hist, align='center', width=width, label='others')

thinkplot.Show(xlabel='lbs', axis=[0, 16, 0, 180])  


mean = firsts.totalwgt_lb.mean()

var = firsts.totalwgt_lb.var()

std = firsts.totalwgt_lb.std()

mode_freq = 0

key = 0

for key in first_hist:

    val = first_hist[key]
    
    if val > mode_freq:
    
        mode_freq = val
        
        mode = key
        
print(mode, mode_freq)

print('firsts')

print('mean:', mean, 'var:', var, 'std:', std, 'mode:', mode)

mean = others.totalwgt_lb.mean()

var = others.totalwgt_lb.var()

std = others.totalwgt_lb.std()


mode_freq = 0

key = 0

for key in other_hist:

    val = other_hist[key]
    
    if val > mode_freq:
    
        mode_freq = val
        
        mode = key
        
print(mode, mode_freq)

print('others')

print('mean:', mean, 'var:', var, 'std:', std, 'mode:', mode)

#pregnancy length

d = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)

print('Cohen d', d)

#birth weight   

d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print('Cohen d', d)

------------

Text output:

firsts
======
mean: 7.20109443044 var: 2.01802730092 std: 1.42057287772 mode: 7.5

others
======
mean: 7.32585561497 var: 1.9437810259 std: 1.39419547621 mode: 7.0

Cohen d: -0.0886729270726
