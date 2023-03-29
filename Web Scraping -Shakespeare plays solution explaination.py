
# 1ST CODE EXPLAINATION

import os
import requests
from bs4 import BeautifulSoup
#These lines import the necessary modules to download the text files from the website and process the HTML content using BeautifulSoup.


url = 'http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/'
#This line sets the URL of the directory containing the text files to be downloaded.

response = requests.get(url)
html = response.content
#These lines send a GET request to the URL and retrieve the content of the response. 
#The html variable is set to the content of the response.


soup = BeautifulSoup(html, 'html.parser')
#This line creates a BeautifulSoup object to parse the html content.

txt_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.txt'):
        txt_links.append(href)
#These lines use a for loop to find all the links on the page that end with '.txt'. 
#For each link found, the href attribute is extracted and checked to see if it ends with '.txt'. If it does, the href value is appended to the txt_links list.

if not os.path.exists('shakespeare_texts'):
    os.makedirs('shakespeare_texts')
#This block checks if a directory called 'shakespeare_texts' exists in the current directory. 
#If it does not, it creates the directory.

counter = 1
for text_link in txt_links[:5]:
    file_url = url + text_link
    response = requests.get(file_url)
    filename = str(counter) + '_' + text_link
    file = open('shakespeare_texts/' + filename, 'wb')
    file.write(response.content)
    file.close()
    print('Downloaded ' + filename + ' successfully.')
    counter += 1
#This block sets the counter variable to 1 and uses a for loop to download and save the content of the first 5 text files. 
#For each file, the URL is constructed by concatenating the base url and the text_link. 
#The content of the file is downloaded using a GET request, and a filename is constructed by combining the counter and text_link values. 
#The content of the file is then saved to the 'shakespeare_texts' directory, and the counter is incremented.
#A message is printed to indicate that the file was downloaded successfully.


# 2ND CODE

import os

# Create an empty dictionary to store file contents
file_dict = {}

# Loop through all the files in the shakespeare_texts directory
for file_name in os.listdir('shakespeare_texts'):

    # Open the file in read mode
    file = open(os.path.join('shakespeare_texts', file_name), 'r')

    # Create an empty dictionary to store line contents
    line_dict = {}

    # Loop through each line in the file
    line_num = 1
    for line in file:
        # Count the number of words in the line
        word_count = len(line.split())

        # Add the line number and word count to the line dictionary
        line_dict[line_num] = word_count

        line_num += 1

    # Add the line dictionary to the file dictionary
    file_dict[file_name] = line_dict

    # Close the file
    file.close()

# Print the file contents
print(file_dict)


# 3RD CODE 

import os

# Create an empty dictionary to store the line counts
line_counts = {}

# Loop through all the files in the shakespeare_texts directory
for file_name in os.listdir('shakespeare_texts'):

    # Open the file in read mode
    file = open(os.path.join('shakespeare_texts', file_name), 'r')

    # Initialize the line count to zero
    line_count = 0

    # Loop through each line in the file
    for line in file:

        # Count the number of words in the line
        word_count = len(line.split())

        # If the line has more than 10 words, increment the line count
        if word_count > 10:
            line_count += 1

    # Add the line count to the dictionary
    line_counts[file_name] = line_count

    # Close the file
    file.close()

# Print the line counts
print(line_counts)

# 4th Code

import os
import re

# Define the regular expression
regex = r'^([A-Z][a-z]+|[A-Z]+)(\t[^\n]*)?\n\n(?=[A-Z])'

# Specify the directory containing the files
directory = r'C:\Users\Prafull_Thokal\shakespeare_texts'

# Initialize the character data dictionaries
character_names = {}
character_lines = {}

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            # Read the file contents
            data = f.read()
            # Find all the matches for the regular expression
            res = re.findall(regex, data, re.MULTILINE)
            # Process the matches for each character
            for match in res:
                character = match[0]
                dialogue = match[1].strip() if match[1] else ""
                if character in character_names:
                    character_lines[character] += dialogue
                else:
                    character_names[character] = 1
                    character_lines[character] = dialogue

# Calculate the total number of words for each character
for character, lines in character_lines.items():
    total_words = sum(len(line.split()) for line in lines)
    print(f"{character}: {total_words}")

# 5th Code

import os
import re

# Define the regular expression
regex = r'^([A-Z][a-z]+|[A-Z]+)(\t[^\n]*)?\n\n(?=[A-Z])'

# Specify the directory containing the files
directory = r'C:\Users\Prafull_Thokal\shakespeare_texts'

# Initialize the character data dictionaries
character_names = {}
character_lines = {}

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            # Read the file contents
            data = f.read()
            # Find all the matches for the regular expression
            res = re.findall(regex, data, re.MULTILINE)
            # Process the matches for each character
            for match in res:
                character = match[0]
                dialogue = match[1].strip() if match[1] else ""
                if character in character_names:
                    character_lines[character] += dialogue
                else:
                    character_names[character] = 1
                    character_lines[character] = dialogue

# Calculate the total number of words for each character
for character, lines in character_lines.items():
    # Split the lines into words
    words = lines.split()
    # Initialize a dictionary to count the words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Sort the words in descending order of count
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # Print the top 10 words for the character
    print(f"{character}:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")
    print()  # Add a blank line between characters


# 4th and 5th code explaination:

import os
import re

regex = r'^([A-Z][a-z]+|[A-Z]+)(\t[^\n]*)?\n\n(?=[A-Z])'

directory = r'C:\Users\Prafull_Thokal\shakespeare_texts'

character_names = {}
character_lines = {}

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            data = f.read()
            res = re.findall(regex, data, re.MULTILINE)
            for match in res:
                character = match[0]
                dialogue = match[1].strip() if match[1] else ""
                if character in character_names:
                    character_lines[character] += dialogue
                else:
                    character_names[character] = 1
                    character_lines[character] = dialogue

for character, lines in character_lines.items():
    total_words = sum(len(line.split()) for line in lines)
    print(f"{character}: {total_words}")
    
    words = lines.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words[:10]:
        print(f"\t{word}: {count}")
    print()


# 4th and 5th combined explaination:

# Importing required libraries
import os  # for interacting with the operating system
import re  # for regular expression matching

# Regular expression pattern to match character names and their dialogue
regex = r'^([A-Z][a-z]+|[A-Z]+)(\t[^\n]*)?\n\n(?=[A-Z])'

# Directory containing the text files to be processed
directory = r'C:\Users\Prafull_Thokal\shakespeare_texts'

# Dictionary to store character names and the number of times they appear in the texts
character_names = {}

# Dictionary to store character names and their dialogue
character_lines = {}

# Loop through all files in the specified directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        # Open the file for reading
        with open(filepath, 'r') as f:
            # Read the entire file into a string variable
            data = f.read()
            # Use regular expression to find all character names and their dialogue in the text
            res = re.findall(regex, data, re.MULTILINE)
            # Loop through all matches and store the character names and their dialogue in the dictionaries
            for match in res:
                character = match[0]
                dialogue = match[1].strip() if match[1] else ""
                if character in character_names:
                    character_lines[character] += dialogue
                else:
                    character_names[character] = 1
                    character_lines[character] = dialogue

# Loop through all character names and print their total word count and top 10 most frequent words
for character, lines in character_lines.items():
    # Calculate total word count
    total_words = sum(len(line.split()) for line in lines)
    # Print the character name and their total word count
    print(f"{character}: {total_words}")
    # Split the dialogue into individual words
    words = lines.split()
    # Dictionary to store word counts
    word_count = {}
    # Loop through all words and store their count in the dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Sort the word count dictionary by frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # Print the top 10 most frequent words for the character
    for word, count in sorted_words[:10]:
        print(f"\t{word}: {count}")
    # Print a blank line for readability
    print()

# 6TH CODE

# Import necessary libraries
import os
import csv

# Set file and directory paths
dir_path = r'C:\Users\Prafull_Thokal'
file_path = os.path.join(dir_path, 'shakespeare_texts')

# Create a list to store the file info
file_info_list = []

# Loop through all the files in the shakespeare_texts directory
for file_name in os.listdir(file_path):
    # Get the full file path
    full_path = os.path.join(file_path, file_name)
    
    # Get the file size
    size = os.path.getsize(full_path)
    
    # Get the last modified datetime
    mod_time = os.path.getmtime(full_path)
    
    # Add the file info to the list
    file_info_list.append({
        'File Name': file_name,
        'Size': size,
        'Last Modified': mod_time,
        'Absolute Path': full_path
    })

# Write the file info to a CSV file
with open('file_info.csv', 'w', newline='') as csvfile:
    # Define the fieldnames for the CSV file
    fieldnames = ['File Name', 'Size', 'Last Modified', 'Absolute Path']
    
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data rows
    writer.writerows(file_info_list)

# Read and print the contents of the CSV file
with open('file_info.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Loop through each row in the CSV file
    for row in reader:
        # Print the row
        print(row)


# 6TH CODE EXPLAINATION

import os
import csv
The os module provides a way to interact with the operating system, while the csv module provides functionality to 
read from and write to CSV files.

dir_path = r'C:\Users\Prafull_Thokal'
file_path = os.path.join(dir_path, 'shakespeare_texts')
This sets the file and directory paths. dir_path is the path to the parent directory of the shakespeare_texts directory. 
file_path is the full path to the shakespeare_texts directory.

file_info_list = []
This creates an empty list to store information about each file in the shakespeare_texts directory.

for file_name in os.listdir(file_path):
This loops through each file in the shakespeare_texts directory.

full_path = os.path.join(file_path, file_name)
This creates the full path to the current file.

size = os.path.getsize(full_path)
This gets the size of the current file in bytes.

mod_time = os.path.getmtime(full_path)
This gets the last modified date and time of the current file.

file_info_list.append({'File Name': file_name, 'Size': size, 'Last Modified': mod_time, 'Absolute Path': full_path})
This appends a dictionary containing information about the current file to the file_info_list.

with open('file_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['File Name', 'Size', 'Last Modified', 'Absolute Path']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(file_info_list)
This writes the contents of the file_info_list to a CSV file named file_info.csv. The DictWriter class is used to 
write dictionaries to the CSV file. The writeheader() method writes the field names as the first row of the CSV file. 
The writerows() method writes each dictionary in the file_info_list as a row in the CSV file.

with open('file_info.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
This opens the file_info.csv file in read mode and reads each row using the csv.reader object. Each row is printed to the 
console using the print() function.