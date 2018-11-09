import pandas
import numpy
from plotnine import *

# Problem 1:
google=pd.read_csv("Google.txt",sep='\t',header=0)
google_scatter=ggplot(google,aes(x="Date",y='Popularity of Google Search for "IRS"'))+theme_classic()+xlab('Date')+ylab('Google Search Popularity')
google_scatter+geom_point()+stat_smooth(method="lm")

# Problem 2:
# # Part 1: show a barplot of the means of the four populations
pop_data=ggplot(data, aes(x="region",y="observations"))+theme_classic()+ylab("Mean Observations")+xlab("Region")
pop_data+geom_bar(stat="summary",fun_y=numpy.mean)
#Part 2: show a scatter plot of all of the observations
pop_data2=ggplot(data, aes(x="region",y="observations"))+theme_classic()+ylab("Observations")+xlab("Region")
pop_data2+geom_point()+geom_jitter()

# Do the bar and scatterplots tell different stories?

# The barplot displays that the average number of observations for each population is roughly equal, but this is misleading because
# scatterplot shows that despite this, the distribution of the actual number of observations varies wildly.

# The North population data is entirely primarily roughly equal to the average number of observations.
# The South population data has two concentrated areas, one above and one below the average. 
# The East population data spans from around 0 to 35 observations
# The West Population data also spans around 0 to 35 observations
# As discussed in class and in one of the Sakai quizzes, this further emphasizes how the means in which
# we choose to convey our data have incredible implications on the conclusions one can draw from the data