# Lambda Functions: Sort a list of dictionaries by a specific key using a lambda function.


#  - Lambda unctions - 
# 1. small anonymous function
# 2. any number of arguments but only one expression
# 3. Pure function means impodent 
# 4. No side effect

myList = [
	{
		'Roll no':52,
		'Name': 'Habib'
	},
	{
		'Roll no':73,
		'Name': 'Junaid'
	},
	{
		'Roll no':3,
		'Name': 'Ans'
	},
	{
		'Roll no':1,
		'Name': 'Joni'
	},
	{
		'Roll no':56,
		'Name': 'Junaid'
	},

]

sorted = sorted(myList,key = lambda x: x['Roll no'])

for _ in sorted:
    print(_)