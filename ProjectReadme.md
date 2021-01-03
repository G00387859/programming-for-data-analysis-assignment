# programming-for-data-analysis-Project
## Introduction

This will contain the jupiter notebook project for this module.
For the jupiter note book you will be able to run and see the output from the investigation into Scipy.stats and Numpy.random.
While there are many Distrbuted funtions in Numpy there are much more in scipy.stats.

This project is about creating a dataframe or dataset. 
This project will take some analysis I have do already of covid 19, where the dataset is taken from the world health organization and recreate the dataset by identifing the distrbutions of the variables, and finding the distrbutions equivelent in numpy. Implementing and showing the scipy.stats and numpy.random distrubtions.

The only code that should be run is the cells in section 2. 
Pressing ctrl and enter will run the code cells . 
Running the note requires a little knowledge of working with jupiter but in the code cell pressing ctrl and enter will run each cell.

## Code analysis 
****
Section 2 is the only code cells that need to be run to combine the dataset. Section 1 contains shows the finding of how the distrubtions where found and how the Section 2 code cells were created. 
code. There are 4 variable generated with the np.random. but variable are generated with calcution based on those variables.
#### function to create new cases random variables that are sorted.
****
##### The first function below is a uses the numpy random gamma distruibtion.
****
![](https://media.geeksforgeeks.org/wp-content/uploads/20200711163155/Screenshot20200711162300.png)<br>
****
The gamma distrubtion takes three paramenters.
then sort the resulting ndarry. 
The round to two decimal places
def new_cases():
    gfg = np.random.gamma(1,1545,305)
    #parmeteres( upper bounds, lower bounds, now many)
    arrr = np.sort(gfg, axis = 0)
    for i in range(len(arrr)):
        arrr[i] = round(arrr[i], 2)
    return arrr
****
##### The second function.
****
#### function to create new deaths, and new_patients random variables that are sorted. 
****
![](https://media.geeksforgeeks.org/wp-content/uploads/20200805150533/Screenshot20200805145651.png)<br>
****
The random samples from Wald or Inverse Gaussian distribution and return the random samples as numpy array.
The wald function takes three (mean, scale, size=None)
def new_deaths()
    gfg = np.random.wald(7.26 , 3.7, 305)
    arrr = np.sort(gfg, axis = 0)
    for i in range(len(arrr)):
        arrr[i] = round(arrr[i], 0)
    return arrr
**** 
## Analysis. 
****
Section 3 contains analysis of the who covid 19 dataset. This good practice in analysis of datsets and help find the relationship of the variable in this dataset. 
****
