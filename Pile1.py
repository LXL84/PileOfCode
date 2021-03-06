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

#Check if DF is null in any way - return True if so
df.isnull().any().any()
#Check which row have null in specific column
nan_rows = df[df['name column'].isnull()]

#DF.info(), nulls specific
df.info(null_counts=True)


startTime=datetime.now() 
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

print(strfdelta((datetime.now() - startTime), "{hours}:{minutes}:{seconds}s")+' to complete the prediction')
#1 days 20:18:12

http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ChiSquare/BS704_HypothesisTesting-ChiSquare_print.html 
# chi-squared test with similar proportions
from scipy.stats import chi2_contingency
from scipy.stats import chi2
# contingency table
table = [	[10, 20, 30],
			[6,  9,  17]]
print(table)
print(table)
stat, p, dof, expected = chi2_contingency(table)
print('dof=%d' % dof)
print(expected)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
