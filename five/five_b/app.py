# 5b. Python for Data Science - Perform Data Visualization on Titanic Dataset
# a) Load the Titanic dataset into one of the data structures (NumPy or Pandas).
# b) Display header rows and description of the loaded dataset.
# c) Remove unnecessary features (E.g. drop unwanted columns) from the dataset.
# d) Manipulate data by replacing empty column values with a default value.
# e)Perform the following visualization on the loaded dataset:   
#   Passenger status (Survived/Died) against Passenger Class4


#import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic_df = pd.read_csv('train.csv')
#print(titanic_df)
# Convert the survived column to strings for easier reading
# titanic_df ['Survived'] = titanic_df ['Survived'].map({
# 0: 'Died',
# 1: 'Survived'
# })
#print(titanic_df)
print("======Data Headers Before Dropping Columns=======")
print(titanic_df.head(5))

# ======Data Headers Before Dropping Columns=======
#    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S


print("**** \n\nDATA TRANSFORMATION *****\n")
print("======Data Headers After Dropping Columns - First Way=======")
titanic_df.drop(['Parch','PassengerId','Name','Ticket'], axis=1,inplace=True)

# #axis =1 in drop method shows you are dropping a column
# #inplace=True means you are editing original dataframe

print(titanic_df.head(5))


# ======Data Headers After Dropping Columns - First Way=======
#    Survived  Pclass     Sex   Age  SibSp     Fare Cabin Embarked
# 0         0       3    male  22.0      1   7.2500   NaN        S
# 1         1       1  female  38.0      1  71.2833   C85        C
# 2         1       3  female  26.0      0   7.9250   NaN        S
# 3         1       1  female  35.0      1  53.1000  C123        S
# 4         0       3    male  35.0      0   8.0500   NaN        S



print("======Data Headers After Dropping Columns - Second Way =======")
titanic_df = titanic_df.drop(['SibSp','Fare'], axis=1)
print(titanic_df.head(5))

# ======Data Headers After Dropping Columns - Second Way =======
#    Survived  Pclass     Sex   Age Cabin Embarked
# 0         0       3    male  22.0   NaN        S
# 1         1       1  female  38.0   C85        C
# 2         1       3  female  26.0   NaN        S
# 3         1       1  female  35.0  C123        S
# 4         0       3    male  35.0   NaN        S


# # Convert the Class column to strings for easier reading
titanic_df ['Pclass'] = titanic_df ['Pclass'].map({
1: 'beangalore',
2: 'koople',
3: 'ganagavathi'
})

print("======Data Headers After Transforming Class Column =======")
print(titanic_df.head(5))

# ======Data Headers After Transforming Class Column =======
#    Survived       Pclass     Sex   Age Cabin Embarked
# 0         0  ganagavathi    male  22.0   NaN        S
# 1         1   beangalore  female  38.0   C85        C
# 2         1  ganagavathi  female  26.0   NaN        S
# 3         1   beangalore  female  35.0  C123        S
# 4         0  ganagavathi    male  35.0   NaN        S




titanic_df ["Embarked"] = titanic_df["Embarked"].fillna("S")
print("======Data Headers After Filling with default value for Embarked Column =======")
print(titanic_df.head(5))

# Survived       Pclass     Sex   Age Cabin Embarked
# 0         0  ganagavathi    male  22.0   NaN        S
# 1         1   beangalore  female  38.0   C85        C
# 2         1  ganagavathi  female  26.0   NaN        S
# 3         1   beangalore  female  35.0  C123        S
# 4         0  ganagavathi    male  35.0   NaN        S


# # Convert the Embarked column to strings for easier reading
titanic_df ['Embarked'] = titanic_df ['Embarked'].map({
'C':'Cherbourg',
'Q':'Queenstown',
'S':'Southampton'
})
print("======Data Headers After Transforming Embarked Column =======")
print(titanic_df.head(5))

# ======Data Headers After Transforming Embarked Column =======
#    Survived       Pclass     Sex   Age Cabin     Embarked
# 0         0  ganagavathi    male  22.0   NaN  Southampton
# 1         1   beangalore  female  38.0   C85    Cherbourg
# 2         1  ganagavathi  female  26.0   NaN  Southampton
# 3         1   beangalore  female  35.0  C123  Southampton
# 4         0  ganagavathi    male  35.0   NaN  Southampton


print("\n\n\n**** DATA VISUALIZATIONS****\n\n")
print("Visualization #1 : Survival Rate Based on Passenger Sitting  Class")

ax = sns.countplot(x = 'Pclass', hue = 'Survived', palette = 'Set1',data = titanic_df)
ax.set(title = 'Passenger status (Survived/Died) against Passenger Class',xlabel = 'Passenger Class', ylabel = 'Total')
plt.show()


# #crosstab - Cross tabulation of two or more factors
print("Visualization #2 : Survival Rate Based on Gender")
print(pd.crosstab(titanic_df["Sex"],titanic_df.Survived))
ax = sns.countplot(x = 'Sex', hue = 'Survived', palette = 'Set2', data= titanic_df)
ax.set(title = 'Total Survivors According to Sex', xlabel = 'Sex',ylabel='Total')
plt.show()

print("Visualization #3 : Survival Rate Based on Passenger Age Group")
# # We look at Age column and set Intevals on the ages and the map them to their categories as
# # (Children, Teen, Adult, Old)


print("Visualization #4 : Survival Rate Based on Passenger Embarked Port")
print(pd.crosstab(titanic_df['Embarked'], titanic_df.Survived))
ax = sns.countplot(x = 'Embarked', hue = 'Survived', palette = 'Set1',data = titanic_df)
ax.set(title = 'Survival distribution according to Embarking place')
plt.show()
