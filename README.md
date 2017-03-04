# wa-matchmaker

This is the matchmaker code for Water Assassins. The algorithm is obfuscated because it will be used later in Settle and other undisclosed projects.

In order for the matchmaker to work, you will need to install the follow module(s):
  * BeautifulSoup4 (for parsing the leaderboards HTML - teams will a score < 0 are left out)

To programmatically call the matchmaker, use the ```calculate()``` method. See the code snippet below:

```python

'''
@param significant_others A list of tuples, with each tuple containing a couple: [('John Doe', 'Jane Doe'), ('Bob Smith'), ('Mary Stalin')]
@param verbose If verbose = 1, print debug statements.
'''
results = calculate(significant_others, verbose=0)

```

The return value from the ```calculate()``` method is a dictionary. Each entry in the dictionary corresponds to this {Key:Value} format - {TeamName[String]:TeamTargets[List]}. Note: team members are not included in the dictionary, only team targets.




