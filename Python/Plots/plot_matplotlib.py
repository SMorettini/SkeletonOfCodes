################################
# HISTOGRAM
# Package needed: matplotlib
################################
import matplotlib.pyplot as plt
data=[1,2,3,4]
plt.hist(data, color = 'blue', edgecolor = 'black')

################################
# BOXPLOT
# Package needed: numpy matplotlib pandas pyqt5
#################################

# import the required library 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
 
  
# load the dataset
df = pd.read_csv("data")

df.boxplot(by ='label', column =['dist'], grid = False)

plt.show()
