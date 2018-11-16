##EDA code
cols = seeds.columns[:-1]
sns.pairplot(seeds, x_vars=cols, y_vars= cols, hue='species')
#seeds is a df, cols are columns that are numeric
#creates a mass scatter plot, pairwise

someqwhat equiavlent ->corrplot
https://towardsdatascience.com/clustering-why-to-use-it-16d8e2fbafe 

ct=pd.crosstab(df['labels'], df['species'])  
print(ct)
#output
species  Bream  Pike  Roach  Smelt
    labels                            
    0            0     0      0     13
    1           33     0      1      0
    2            0    17      0      0
    3            1     0     19      1
#generates a crosstable good for showing distribution. But data needs to be in DF form.

x = [iris.sepal_length[iris.species==sp_name] for sp_name in ['setosa', 'versicolor', 'virginica']]
plt.hist(x, 8, density=True, histtype='bar', stacked=True)
#plots histogram with 1 variable, stacked bars using another variable (species)
#used in Titanic:
x = [df.SibSp[df.Survived==sp_name] for sp_name in [1,0]]
plt.hist(x,histtype='bar', stacked=True)
plt.legend(['alive','dead'])
plt.show()

DataFrame.select_dtypes(include=None, exclude=None)
#selects the subset of DF that is of dtype.
for numbers, use include='number'

Manipulation in pandas
df2['todrop']=['yes' if pd.isnull(x) else 'no' for x in df2['Age']]
->make a new variable 'todrop' dependent on whether a value in 'Age' is null or not 

df['Family'] = np.where(np.logical_or(df['SibSp']>0, df['Parch']>0),'yes', 'no')
create a new variable 'family' with a yes/no depending on sibsp and parch vars.
