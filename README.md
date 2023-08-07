# Welcome to My Mr Clean
 It  is time to get our hands dirty and to manipulate some real world data. You have been hired by a new company named EncyclEarthpedia and your first task it build a search engine.
  EncyclEarthpedia is an online encyclopedia but specialized in the planet Earth, its geology, biology, and everything related to the Earth.
 The search engine should be simple at first. The user needs to be able to type some words and the engine returns the most relevant articles.
 There is a problem though. The engineers working on the database messed up and EncyclEarthpedia's database and API are not available for a week.
 This is a bummer ! If we can't have access to the articles, how are we going to build our engine ?
 Instead of waiting for a week, we are going to build a simple model for some similar article from Wikipedia.

## Task
What is the problem? And where is the challenge?
Retrieving Wikipedia content: Retrieving the content of a specific Wikipedia article using the Wikipedia API requires constructing the correct API URL and handling the response data in JSON format.

Text processing: The content obtained from Wikipedia may contain various elements such as formatting tags, citations, references, and other irrelevant information. Cleaning and processing the text data to extract meaningful content while removing unwanted elements can be challenging.

Tokenization: Splitting the processed text into individual tokens (words) involves handling punctuation, special characters, and different word forms. Ensuring accurate tokenization and handling edge cases like hyphenated words or contractions can be challenging.

Counting token frequency: Counting the frequency of each token requires an efficient and accurate method to iterate over the tokens and update their counts. Dealing with case sensitivity, stop words, and special characters while maintaining the accuracy of the frequency count can be challenging.

Data visualization: Presenting the most frequent tokens in a visually appealing and informative manner is important. Choosing the appropriate visualization technique and configuring the plot parameters to effectively communicate the token frequencies can be challenging.

## Description
How have you solved the problem?
get_content(title): This function takes a Wikipedia article title as input and uses the Wikipedia API to retrieve the content of the article in JSON format. The JSON data is then returned.

merge_contents(json_data): This function takes the JSON data retrieved from the Wikipedia API and extracts the text content from it. It removes any curly braces ({...}) and parentheses (...) using regular expressions. It also replaces newlines and backslashes with spaces. The processed text data is returned.

tokenize(content): This function takes the processed text content and tokenizes it by splitting the text into individual words. It removes any commas and periods from the tokens. The tokens are returned as a list.

lower_collection(collection): This function takes the list of tokens and converts each token to lowercase. The lowercase tokens are returned as a new list.

count_frequency(tokens): This function takes the list of tokens and counts the frequency of each token using a dictionary. It iterates over the tokens, updating the count for each token in the dictionary. The dictionary containing the token frequencies is returned.

print_most_frequent(frequencies, n): This function takes the dictionary of token frequencies and the number of most frequent tokens to display. It creates a pandas DataFrame from the dictionary, sorts the DataFrame based on the frequency in descending order, and selects the top n most frequent tokens. It then visualizes the tokens and their frequencies using a horizontal bar plot with the seaborn library.

remove_stop_words(frequencies, stop_words): This function takes the dictionary of token frequencies and a list of stop words. It filters out the stop words from the dictionary, creating a new dictionary with only the non-stop words and their frequencies. The filtered dictionary is returned.

## Installation
!pip install seaborn

import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
## Usage
 How does it work?
 data = get_content("Ozone_layer")
merge_content = merge_contents(data)
tokens = tokenize(merge_content)
frequencies = count_frequency(tokens)
print_most_frequent(frequencies, 20)

stop_words = ["the", 'a', "of", "is", "and", "by", "to", "that", "are", "at", "on", 'an', "uv", 'for', 'be', 'it', 'as', 'this', 'about', 'from', 'these', 'has', 'do', 's', 'so', 'out', 'or', 'du']
filtered_frequencies = remove_stop_words(frequencies, stop_words)
print_most_frequent(filtered_frequencies, 25)
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
