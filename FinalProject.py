#Written by Chandler Lopez and Austin Jones
#Computational Project
#Due April 26
#Source codes for histogram and scatter plot (which have been edited to meet our needs) were found on 
# warning handling was found on https://stackoverflow.com/questions/3920502/how-to-suppress-a-third-party-warning-using-warnings-filterwarnings
#pickling from https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type/27745539#27745539


#creats empty class lists for the required subject to be used later
MathGrade=[];

#imports libraries that will be used in the computing, outputing, and warning handling
import random
import statistics
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import warnings
import pickle

#makes a random list with values between 0 and 100 given the length n
i=0
def makelist(n):
    randlist=[]
    for i in range(n):
        x = random.randint(0, 100)
        randlist.append(x)
        i=i+1
    return randlist

#user inputs an int n, n must be between 15 and 25 to continue
n=int(input("please enter the amount of students: "))
boolean = False
while (boolean==False):
    if (15<=n and n<=25):
        boolean=True
    else:
        print("you need to input a value between 15 and 25")
        n=int(input("please enter the amount of students: "))

#Fills the class lists with random values given the length n
MathGrade=makelist(n)
print("Math Grades are:" , MathGrade)

#finds min of the given list
def calcmin(TempList):
    minimum=min(TempList)
    return minimum

#finds max of the given list
def calcmax(TempList):
    maximum=max(TempList)
    return maximum

#finds med of the given list
def calcmed(TempList):
    median=statistics.median(TempList)
    return median

#finds average of the given list
def calcav(TempList):
    total=sum(TempList)
    average=total/n
    return average

#finds standered deviation of the given list
def calstdev(TempList):
    stdev=statistics.stdev(TempList)
    return stdev



#reads and writes values from the txt file
#Pickles the list into the txt file
with open("input.txt", "wb") as pic:   
    pickle.dump(MathGrade, pic)
# Unpickles the list from the txt file as TempList to be used throught the code
with open("input.txt", "rb") as pic:  
    TempList = pickle.load(pic)

              
print("For Math grades: min= " , calcmin(TempList) ,", max= ", calcmax(TempList),", median= ", calcmed(TempList),", average= ", calcav(TempList),", standered deviation= ", calstdev(TempList))

#comparing grades of each student using a scatter plot
#the x axis goes from 1-n+1
#y values are dependent upon the class
x = range(1,n+1)
y1 = TempList


#labels both axis
plt.xlabel('Student', fontsize=18)
plt.ylabel('Grade', fontsize=18)

#plots all values on the same x axis with different markers and/or colors
plt.scatter(x, y1, c='b', marker="s", label='Math')


#adds a legend appearing in the top right corer
plt.legend(loc='upper left');

#displays the scatter plot
plt.show()



#histogram

# defines a variable for the mean of distribution
mu =  calcav(TempList)

# defines a variable for the standard deviation of distribution
sigma = calstdev(TempList)  

#grades are on the x axis(only for math class as asked by the assighnment)
x=TempList

#thicknes/ amount of bars
num_bins = 50

#plots values
fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)

# add a 'best fit' line
#catches the warnings (made for depricaton) and ignores them
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    y = mlab.normpdf(bins, mu, sigma)


#lables and plots
ax.plot(bins, y, '--')
ax.set_xlabel('Grades')
ax.set_ylabel('Probability density')
ax.set_title('Histogram of Math Grades')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()



