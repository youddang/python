import numpy as np
import matplotlib.pyplot as plt

#var
x = np.arange(8)
years = ["2011", "2012", "2013", "2014","2015", "2016", "2017", "2018"]
values = [1, 2, 3, 4, 5, 6, 7, 8]

#grape
plt.plot(years, values, linestyle = '--', marker = 'o', color = 'bisque')
plt.xticks(x, years)
plt.bar(x, values, width = 0.3, color = 'chartreuse')

#label
plt.ylabel('Strategic Innovation Index') 
plt.xlabel('age') 
plt.title('Small businesses')

plt.show()