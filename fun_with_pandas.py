import numpy as np
import pandas as pd


numbers = [1, 2, 3, 4, 5]
#mean
print np.mean(numbers)
#median
print np.median(numbers)
#standard devation
print np.std(numbers)


#Series: one dimensional object like a list or column in database, 0 to n-1 indices
series = pd.Series(['Shamikh', 'Hossain', 'Duke', 19, 223], index = ['First Name', 'Last Name', 'College', 'Age', 'Room Number'])
print series
print series['First Name']
print series[1] #normal index notation
print

cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig','Puppy', 'Kitten'])
print cuteness > 3 #prints booleans!
print cuteness[cuteness > 3] #prints values

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions','Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12] }

football = pd.DataFrame(data)
print football

print football.dtypes #data types for each column
print ""
print football.describe() #basic statistics
print ""
print football.head() #first five rows
print ""
print football.tail() #last five rows


#################
# DataFrame Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})


countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    # your code here
olympics = pd.DataFrame({'country_name': pd.Series(countries),
                                           'gold'   : pd.Series(gold),
                                           'silver' : pd.Series(silver),
                                           'bronze' : pd.Series(bronze)})

print olympics
print olympics[['gold', 'country_name']]
print olympics.loc[1]

#all countries with at least one medal
print olympics[olympics['gold'] >= 1]
print olympics['gold'].map(lambda x: x >= 1)
print olympics.applymap(lambda x: x >= 1)

avg = np.mean(olympics['bronze'][olympics['gold'] >= 1])
print avg

#take mean
print olympics['gold'].apply(np.mean)


numbers = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]
dotproduct = np.dot(numbers, numbers_2)
print dotproduct
#dot product is each index of each vector multiplied with the other, and then added

a = [1, 2]
b = [[2, 4, 6], [3, 5, 7]]
print np.dot(a, b)

medal_counts = olympics[['gold', 'silver', 'bronze']] #selecting specific columns from a dataframe
points = np.dot(medal_counts, [4, 2, 1]) #dot product for each country

olympic_points = pd.DataFrame({'country_name': pd.Series(countries),
                                'points'   : pd.Series(points)})

print olympic_points
