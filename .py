# Dictionaries


Dictionaries
What are Dictionaries?
A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of the numerical indexes such as a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.

Image
An example of a Dictionary Dict:

# Create the dictionary
​
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict
{'key1': 1,
 'key2': '2',
 'key3': [3, 3, 3],
 'key4': (4, 4, 4),
 'key5': 5,
 (0, 1): 6}
The keys can be strings:

# Access to the value by the key
​
Dict["key1"]
1
Keys can also be any immutable object such as a tuple:

# Access to the value by the key
​
Dict[(0, 1)]
6
Each key is separated from its value by a colon ":". Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this "{}".

# Create a sample dictionary
​
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", 
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", 
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", 
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict
{'Thriller': '1982',
 'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977'}
In summary, like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be one single value, however, multiple keys can hold the same value. Keys can only be strings, numbers, or tuples, but values can be any data type.

It is helpful to visualize the dictionary as a table, as in the following image. The first column represents the keys, the second column represents the values.

Image
Keys
You can retrieve the values based on the names:

# Get value by keys
​
release_year_dict['Thriller'] 
'1982'
This corresponds to:

Image
Similarly for The Bodyguard

# Get value by key
​
release_year_dict['The Bodyguard'] 
'1992'
Image
Now let you retrieve the keys of the dictionary using the method release_year_dict():

# Get all the keys in dictionary
​
release_year_dict.keys() 
dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])
You can retrieve the values using the method values():

# Get all the values in dictionary
​
release_year_dict.values() 
dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])
We can add an entry:

# Append value with key into dictionary
​
release_year_dict['Graduation'] = '2007'
release_year_dict
{'Thriller': '1982',
 'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977',
 'Graduation': '2007'}
We can delete an entry:

# Delete entries by key
​
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict
{'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977'}
We can verify if an element is in the dictionary:

# Verify the key is in the dictionary
​
'The Bodyguard' in release_year_dict
True
Quiz on Dictionaries
You will need this dictionary for the next two questions:

soundtrack_dic
# Question sample dictionary
​
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 
{'The Bodyguard': '1992', 'Saturday Night Fever': '1977'}
a) In the dictionary soundtrack_dic what are the keys ?

soundtrack_dict
# Write your code below and press Shift+Enter to execute
soundtrack_dic.keys()
dict_keys(['The Bodyguard', 'Saturday Night Fever'])
Double-click __here__ for the solution.
​
<!-- Your answer is below:
soundtrack_dic.keys() # The Keys "The Bodyguard" and "Saturday Night Fever" 
-->
b) In the dictionary soundtrack_dic what are the values ?

# Write your code below and press Shift+Enter to execute
soundtrack_dic.values()
dict_values(['1992', '1977'])
Double-click __here__ for the solution.
​
<!-- Your answer is below:
soundtrack_dic.values() # The values are "1992" and "1977"
-->
You will need this dictionary for the following questions:

The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:

a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.

# Write your code below and press Shift+Enter to execute
album_sales_dict = {'Back in Black':50, 'The Bodyguard':50, 'Thriller':65}
album_sales_dict
{'Back in Black': 50, 'The Bodyguard': 50, 'Thriller': 65}
Double-click __here__ for the solution.
​
<!-- Your answer is below:
album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}
-->
b) Use the dictionary to find the total sales of Thriller:

'
# Write your code below and press Shift+Enter to execute
album_sales_dict['Thriller']
65
Double-click __here__ for the solution.
​
<!-- Your answer is below:
album_sales_dict["Thriller"]
-->
c) Find the names of the albums from the dictionary using the method keys:

.keys()
# Write your code below and press Shift+Enter to execute
album_sales_dict.keys()
dict_keys(['Back in Black', 'The Bodyguard', 'Thriller'])
Double-click __here__ for the solution.
​
<!-- Your answer is below:
album_sales_dict.keys()
-->
d) Find the names of the recording sales from the dictionary using the method values:

.values()
# Write your code below and press Shift+Enter to execute
album_sales_dict.values()
dict_values([50, 50, 65])
Double-click __here__ for the solution.
​
<!-- Your answer is below:
album_sales_dict.values()
-->
