#!/usr/bin/env python
# coding: utf-8

# In[6]:


import function_exercises
function_exercises.is_vowel("b")


# In[8]:


import function_exercises
function_exercises.capitalize_if_consonant("tacos")


# In[9]:


import function_exercises 
function_exercises.calculate_tip(.3, 50)


# In[12]:


import itertools

from itertools import combinations
combinations('ABC',2)


# In[13]:


import itertools as it
len(list(it.product([1, 2, 3], 'abc')))

len(list(it.combinations('abcd', 2)))


# In[18]:


import json
profiles = json.load(open('profiles.json'))


# In[10]:


# Total number of uses 
len(profiles)


# In[16]:


# Total number of active users 
len([profile for profile in profiles if profile['isActive']])


# In[11]:


# Total number of inactive users
len([profile for profile in profiles if not profile['isActive']])


# In[12]:


# Grand total of balances for all users 
def clean_balance(balance):
    balance = balance.replace(',', '')
    balance = balance.replace('$', '')
    return float(balance)

balances = [profile['balance'] for profile in profiles]
balances = [balance.replace(',', '') for balance in balances]
balances = [balance.replace('$', '') for balance in balances]
balances = [float(balance) for balance in balances]
sum(balances)


# In[13]:


sum(balances) / len(balances)


# In[17]:


#User with lowest balance
user_with_lowest_balance = profiles[0]
# Now we can loop through the remaining profiles and compare the balances
for profile in profiles[1:]:
    # if the current profile has a lower balance than our lowest balance so far,
    if clean_balance(profile['balance']) < clean_balance(user_with_lowest_balance['balance']):
        # set this profile as the user with the lowest balance
        user_with_lowest_balance = profile

user_with_lowest_balance['name']


# In[23]:


#User with highest balance
user_with_highest_balance = profiles[0]
for profile in profiles[1:]:
    if clean_balance(profile['balance']) > clean_balance(user_with_highest_balance['balance']):
        user_with_highest_balance = profile

user_with_highest_balance


# In[24]:


# Most common favorite fruit

favorite_fruits = [profile['favoriteFruit'] for profile in profiles]
favorite_fruits


# In[26]:


# Most common favorite fruit
# Our goal here is to transform the list above into a dictionary where the keys are the unique fruit names,
# and the values are the number of times that fruit appears in the list above.

# To do so, we'll start with an empty dictionary:
fruit_counts = {}

# Now we can loop through the list of favorite fruits
for fruit in favorite_fruits:
    # if the fruit name already exists as a key in the fruit_counts dictionary
    if fruit in fruit_counts:
        # We already have started a acount for this fruit
        # add 1 to the number of times that fruit appears
        fruit_counts[fruit] += 1
    else:
        # We don't yet have an entry for this fruit
        # Create it and set it to 1
        fruit_counts[fruit] = 1

fruit_counts


# In[ ]:


# Strawberry is most common favorite fruit. 
# Apple is least common favorite fruit. 


# In[27]:


#Total number of unread messages for all users
def extract_digits(s):
    return ''.join([c for c in s if c.isdigit()])

n_unread_messages = [extract_digits(profile['greeting']) for profile in profiles]
sum([int(message) for message in n_unread_messages]) 

