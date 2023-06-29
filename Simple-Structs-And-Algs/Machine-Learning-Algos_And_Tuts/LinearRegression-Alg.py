from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5, 6])
ys =  np.array([5, 4, 6, 5, 6, 7])

	
def best_fit_slope_and_intercept(xs, ys):

	'''I am stupid and i couldnt get the paratheses right so I had to resort to splitting it up
	   into parts numer1 is just the first part of the numerator so you can geuss what the rest mean '''	

	numer1 = np.mean(xs) * np.mean(ys)
	numer2 = np.mean(xs * ys)
	denom1 = np.mean(xs)**2
	denom2 = np.mean(xs**2)

	'''Just a note the formula here is called the least squares method '''
	m =  (numer1 - numer2) / (denom1 - denom2)   

	b = mean(ys) - m * mean(xs)
	return m, b

m, b = best_fit_slope_and_intercept(xs, ys)
#print(m, b)

regression_line = [(m*x) + b for x in xs]

predict_x = 8
predict_y = (m*predict_x) + b

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()

'''For better Explanations for the best fit line and why or how it works here are a couple resources:
	https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/regression-library/v/calculating-residual-example
	https://www.youtube.com/watch?v=P8hT5nDai6A - The formula here is different but work it out with both and youll see there really the same

	That being said there are a few things that I can provide as an explanation of sorts So you may notice we are taking means. 
	Well this is actually not random (crazy right?) if you think about it taking averages for what we are doing makes complete sense,
	of course the actual formula is not obvious and may require some signifigant math knowledge to understand (at least linear algerbra or calc 2)
	One very notable thing is something called the centroid which is effectivley the point where x is the mean of all x values and the y is the mean of all y values,
	the line must pass through that line, makes sense so far right? now for this next step i am going to use an example. The formula I use here looks different but is the same:

	ok so lets get a look at our values

	xs 	 | ys
	1  	 | 5
	2  	 | 4
	3  	 | 6
	4  	 | 5
	5  	 | 6
	6  	 | 7
	mean:| mean:
	3.5  | 5.5

	centroid: (3.5, 5.5) alright so now we know it must pass through here 

	(3.5 * 5.5) - ((each x * each y) / 6) / 3.5^2 - ((each x to the power of 2) / 6)
	
	and thats the slope then the b or in other words is a little less intuitive but its 5.5 - (slope * 3.5)

	you might see an equation with a ton of summations and it could be done that way its the same (the summation gets divided by the "average" making it the mean anyway) equation
 

	It is Also Important to understand what values are being affected! Part of understanding linear regression isnt just how but why as well. 
	Remember that with linear regression we are using the y = mx + b formula (basically) this means that the values you are using in the regression
	must have some sort of relationship!!! That being said with most datasets they wont give you data with no relationshio but some give you way to much data
	so you have to focus on the relationship between them and figure out is the cause of one thing related to the other? WITH THIS IN MIND remember a plot/graph is just a mapping
	that is an extremly important detail. I could say y = cats and x = dogs where 6,3 is when there is 6 cats there is 3 dogs. 
	Obviously this is a good example of something that doesnt have a relationship, but the point is this is where you should be able to detect a relationship. xs are the features and ys are the target value
	just like any normal graph right? You might notice by now that with sklearn you dont really need to know how the equation works or why and thats technically true right now but its nice to know so...
	definetley try and learn more about it. Also no one will ever see this so Im actually talking to my self which makes me clinically insane :(

	'''
