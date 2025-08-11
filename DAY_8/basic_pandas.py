# import libraries
import pandas as pd

students={
    'Names': ['Bob', 'Alice','Joe', 'Mike', 'Lisa', 'Tom', 'James'],
    'Major': ['Accounting', 'Finance','Chemistry', 'Art', 'Engineering', 'Art', 'Physics'],
    'GPA': [3.5, 3.8, 3.2, 3.7, 4.0, 3.5, 3.1],
    'Age': [22, 23, 31, 40, 25, 30, 24]
}
roster_df = pd.DataFrame(students)
print(roster_df)
# this reurns the first 5 rows in the dataset
print(roster_df.head())

# returns the first 'n rows in the dataset
# print(roster_df.head('n'))

# gives the first 3 rows
print(roster_df.head(3))

# gives the last 5 rows in the dataframe
print(roster_df.tail())

# last 2 rows
print(roster_df.tail(2))

# .shape - returns a tuple of dimensions of the dataset (rows, cols)
print(roster_df.shape)

# .describe() returns a dataframe containing statistics of columns
print(roster_df.describe())

# sorting the coloumns in alphabetical order
# .sort_index(axis=1, ascending False) - sorts the datasent 0- sorting rows (horizontal indexes), 1 sorting columns (vertical indexes)
print(roster_df.sort_index(axis=1, ascending=False))


# sorting the coloumns in numerical order
print(roster_df.sort_index(axis=0, ascending=True))

# sorting the coloumns in reverse numerical order
print(roster_df.sort_index(axis=0, ascending=False))


# .sort_values(by=column_name) sorts a column in ascending order
print(roster_df.sort_values(by='GPA'))


# .sort_values(by=column_name, ascending = False) sorts a column in reverse ascending order
print(roster_df.sort_values(by='GPA', ascending=False))

# .T - returns a transpose of the dataset
# it filps the rows with coloumns 
print(roster_df.T)


# DataFrame['start_row_index': 'end_row_index'] - returns the specific rosw in the dataframe

print(roster_df)


# write python code to return the 2nd through the 5th rows (inclusive of the endpoint) in the dataframe above. 
print(roster_df[1:5])

# using filter mask

# find all students with a gpa >= 3.5
print(roster_df['GPA']>=3.5)
# this is a mask covers certian parts and exposes certain parts
mask = roster_df['GPA']>=3.5
print(roster_df[mask])






#another way
print(roster_df[roster_df['GPA']>=3.5])

# another way
print(roster_df.loc[mask])

# finding the gpa lower than 3.5 the opposite use ~
print(roster_df[~mask])

# reading a csv file into pandas

flower_df=pd.read_csv('https://raw.githubusercontent.com/avinashjairam/avinashjairam.github.io/refs/heads/master/Iris.csv')
print(flower_df)

print(flower_df.describe())

import matplotlib as plt 
# Generating a scatter plot using pandas


# plothing sepal length vs sepal width
print(flower_df.plot(x='SepalLengthCm', y= 'SepalWidthCm', kind = 'scatter'))
plt.title('Sepal Lendth vs Sepal Width')
plt.show()

# plothing petal length vs petal width
print(flower_df.plot(x='PetalLengthCm', y= 'PetalWidthCm', kind = 'scatter'))
plt.title('Petal Lendth vs Petal Width')
plt.show()

# get a list of columns in the dataframe
print(list(flower_df.columns))

# print correlation df 
# check the datatypes that exists in the dataframe 
print(flower_df.dtypes())



# drop the species column temp fix 
# .corr - generates a correlation matrix
print(flower_df.drop('Species', axis =1).corr())


# Combining DataFrames
roster_1_df=roster_df
print(roster_1_df)
roster_2 = {
            'Name': ['Sam', 'Luch', 'Henry', 'Marlon', 'Louise'],
            'Major': ['Marketing', 'Music', 'Chemistry', 'History', 'Math'],
            'GPA': [3.2, 3.6, 2.5, 3.7, 3.9],
            'Age': [25, 27, 35, 40, 20]
        }
roster_2_df=roster_2
print(roster_2_df)

# .concat(list_of_dataframes, ignore_index= True/False)
# this will stack it vertically 
# combined_df = pd.concat(roster_1_df, roster_2_df)
combined_df = pd.concat([roster_1_df, roster_2_df], ignore_index=True)
print(combined_df)

# this will stack it horizontally
combined_df_horizontally = pd.concat([roster_1_df, roster_2_df], axis=1,ignore_index=True)
print(combined_df_horizontally)

# .info() tells you about the colums in your dataframe 
print(combined_df.info())


# changing the index of the dataframe
# .set_index(name_of_column)

print(combined_df.set_index('Major'))


# permanently change the index of a dataframe to that of another column by using the inplace parameter and setting it to True 
print(combined_df.set_index('Major', inplace=True))

# listing all indexes
print(combined_df.index)
# sort by index
print(combined_df.sort_index())

# sorting the indexes in revere aplp
print(combined_df.sort_index(ascending=False))

# .loc to lookup data by index
print(combined_df.loc['Chemistry'])
print(combined_df.loc['Chemistry', 'Age'])


# setting the index of dataframe that has duplicate columns will result in 'tuples' being the index
print(combined_df_horizontally.set_index('Name'))


# we can reset the index of a dataframe to its original state - the actual row indexes via the .reset() method

print(combined_df.reset_index(inplace=True))

# a more complicated filter
# find all chemistry majors above age 30 and with a gpa lower than 3.0 
print(combined_df)
print(combined_df['Major']=='Çhemistry')
print(combined_df['Age']>30)
print(combined_df['GPA']<3.0)

# need to combine these 3 together
print(combined_df['Major']=='Çhemistry')
print(combined_df['Age']>30)
print(combined_df['GPA']<3.0)

filter_mask=(combined_df['Major']=='Çhemistry')& (combined_df['Age']>30)& (combined_df['GPA']<3.0)

print(combined_df[filter_mask])
# who do NOT match the conditions 
print(combined_df[~filter_mask])

# find all students who are physics majors or have a gpa>3.6
print(combined_df['Major']=='Physics')
print(combined_df['GPA']>3.6)
# the | means or 
filter_mask_2=(combined_df['Major']=='Physics')| (combined_df['GPA']>3.6)
print(combined_df[filter_mask_2])

# .iloc - used to access rows by thier positions in the dataframe 
# name_of_dataframe.iloc['start_post:ed_pos']
print(combined_df[1:4])
# or 
print(combined_df.iloc[1:4])



# NEW TOPIC

# Merging 
roster1 = {"emplid": [3421, 4723, 1331, 5435, 9453, 2345, 6234, 6845, 6245, 9645],
          "Name" : ["Bob", "Alice", "Joe", "Mike", "Lisa", "Alan", "Eli", "Mark", "Liz", "Jane"],
          "Major": ["Accounting", "Finance", "Chemistry", "Art", "Engineering", "Biology", "Physics", "History", "Art", "Engineering"],
          "GPA": [3.5, 3.8, 3.2, 3.7, 4.0, 3.5, 3.8, 3.2, 3.1, 3.0],
          "Age": [22, 23, 31, 40, 25, 22, 33, 31, 27, 55]
          }

roster1_df = pd.DataFrame(roster1)

print(roster1_df)

address = {"emplid": [3421, 1331, 5435, 2345, 6845, 7425, 4045, 8245],
          "Address" : ["1 Hyland Blvd", "88 Parkside Ave", "848 Jersey Turnpike", "3 Main Street", "231 Water Street", "22 1st Ave", "4 Grand Concourse", "222 William Street"],
          "City": ["Staten Island", "Brooklyn", "Hoboken", "Queens", "New Haven", "Manhattan", "Bronx", "Hempstead"],
          "State": ["NY", "NY", "NJ", "NY", "CT", "NY", "NY", "NY"],
          "Zipcode": [10304, 11220, 70086, 11432, 60511, 10024, 10458, 24231]
          }

address_df = pd.DataFrame(address)

print(address_df)

# .left_merge(left_dataframe, right_dataframe, merge_type, column)
result=pd.merge(roster1_df, address_df, how='left', on=['emplid'])
print(result)

# result=pd.merge(roster1_df, address_df, how='left', on=['emplid', 'Age'])
# print(result)

athletics = {"emplid": [3333,4723, 1331, 1111, 5435,  2345, 2222, 6234, 6245, 9645,4444],
          "Sport" : ["Basketball", "Baseball", "Soccer", "Basketball", "Swimming", "Soccer", "Volleyball","Chess","Soccer","Tennis","Basketball"],
          "Medals": [1, 0, 2, 0, 3, 5, 0,4,5,0,1],
          "Stipend": ["yes", "no", "no", "yes", "yes", "no","yes","yes","yes","no","no"],
          "Practice Hours": [220, 123, 331, 140, 125, 252, 3, 24,51,20,55]
          }

athletics_df = pd.DataFrame(athletics)

print(athletics_df)
# .right_merge(left_dataframe, right_dataframe, merge_type, column)
result1= pd.merge(roster1_df, athletics_df, how='right',on=['emplid'])
print(result1)

# inner merge
# .inner merge(left_dataframe, right_dataframe, merge_type, column)
result2= pd.merge(roster1_df, athletics_df, how='inner',on=['emplid'])
print(result2)

# .outer merge(left_dataframe, right_dataframe, merge_type, column)
result3= pd.merge(roster1_df, athletics_df, how='outer',on=['emplid'])
print(result3)