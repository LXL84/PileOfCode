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


DataFrame.select_dtypes(include=None, exclude=None)
#selects the subset of DF that is of dtype.
for numbers, use include='number'
