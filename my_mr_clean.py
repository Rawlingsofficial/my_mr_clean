#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install seaborn')
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


def get_content(title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles={title}&explaintext&format=json"  
    
    response = requests.get(url)
    data = response.json()
    
    return data


# In[5]:


def merge_contents(json_data):
    key = list(json_data['query']['pages'].keys())[0]
    data = str(json_data['query']['pages'][key]['extract'])

    data = re.sub(r'\{.*?\}', '', data)
    data = re.sub(r'\(.*?\)', '', data)
    data = re.sub(r'[\n\\]', ' ', data)

    return data


# In[6]:


def tokenize(content):
    content = re.sub(r'[,.]', '', content)
    tokens = content.split()
    return tokens


# In[12]:


def lower_collection(collection):
    lowered_collection = [word.lower() for word in collection]
    return lowered_collection


# In[13]:


def count_frequency(tokens):
    frequencies = {}
    for token in tokens:
        frequencies[token] = frequencies.get(token, 0) + 1
    return frequencies


# In[14]:


def print_most_frequent(frequencies, n):
    df = pd.DataFrame(frequencies.items(), columns=['words', 'frequent'])
    df = df.sort_values(by='frequent', ascending=False).head(n)
    
    plt.style.use('dark_background')
    f, ax = plt.subplots(figsize=(20, 15))
    ax.grid(False)
    sns.set_color_codes("muted")
    sns.set(style="darkgrid")
    sns.barplot(x="frequent", y="words", data=df, label="Ozone Layer", orient="h").set(title='Most Common Tokens in the Ozone Layer article')


# In[15]:


def remove_stop_words(frequencies, stop_words):
    filtered_frequencies = {word: freq for word, freq in frequencies.items() if word not in stop_words}
    return filtered_frequencies

data = get_content("Ozone_layer")
merge_content = merge_contents(data)
tokens = tokenize(merge_content)
frequencies = count_frequency(tokens)
print_most_frequent(frequencies, 20)

stop_words = ["the", 'a', "of", "is", "and", "by", "to", "that", "are", "at", "on", 'an', "uv", 'for', 'be', 'it', 'as', 'this', 'about', 'from', 'these', 'has', 'do', 's', 'so', 'out', 'or', 'du']
filtered_frequencies = remove_stop_words(frequencies, stop_words)
print_most_frequent(filtered_frequencies, 25)


# In[17]:


get_ipython().system(' gandalf')


# In[ ]:




