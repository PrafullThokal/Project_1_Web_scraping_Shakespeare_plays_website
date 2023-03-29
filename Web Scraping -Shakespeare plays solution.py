# 1st code:

'''Download first 5 text files (Shakespeare’s plays) from the following URL using a python script: http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/
Store these in a separate folder.
(Find the 5 URLs pointing to .txt files in the above page using code. Do not manually put any URL other than the above mentioned one in the code.)
'''

'''
Steps:
Set the URL of the webpage containing the Shakespeare's plays text files.
Send a GET request to the URL and get the HTML content of the page.
Use BeautifulSoup to parse the HTML content and find all links on the page.
Iterate over all the links and check if they point to a text file (ends with '.txt').
If a link is pointing to a text file, append the link to a list of text file links.
Create a new directory 'shakespeare_texts' to store downloaded text files, if it does not already exist.
Set a counter to 1 to number the downloaded text files.
Iterate over the first 5 text file links in the list.
Build the complete URL for the text file by appending it to the base URL.
Send a GET request to the text file URL and get the content of the text file.
Build a unique filename for the text file by concatenating the counter and the text file name.
Create a new file in the 'shakespeare_texts' directory with the unique filename and write the text file content to it.
Increment the counter.
Print a success message indicating that the text file has been downloaded.
Repeat steps 10-14 for each of the first 5 text files in the list.
'''

import os
import requests
from bs4 import BeautifulSoup

url = 'http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

txt_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.txt'):
        txt_links.append(href)

if not os.path.exists('shakespeare_texts'):
    os.makedirs('shakespeare_texts')

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
    
************************************************************************************************************************************
# 2nd code:

#EXAMPLE 2:
'''Get all { file name : { line number : number of words in the line } } combinations in a dictionary.'''
'''
Steps:
Create an empty dictionary to store file name and line information.
Iterate over all the files in the 'shakespeare_texts' directory using os.listdir() method.
Open each file and read its content.
Create an empty dictionary to store the line number and word count information for each file.
Set the line number to 1.
Iterate over each line in the file.
Split the line into words and count the number of words in the line using the len() method.
Store the line number and word count information as a key-value pair in the line dictionary.
Increment the line number.
Store the line dictionary as a value in the file dictionary, with the file name as the key.
Close the file.
Repeat steps 3-11 for each file in the directory.
Print the file dictionary containing all { file name : { line number : number of words in the line } } combinations.
'''

import os
file_dict = {}
for file_name in os.listdir('shakespeare_texts'):

    file = open(os.path.join('shakespeare_texts', file_name), 'r')
    line_dict = {}
    line_num = 1
    for line in file:
        word_count = len(line.split())
        line_dict[line_num] = word_count
        line_num += 1

    file_dict[file_name] = line_dict
    file.close()

print(file_dict)

**********************************************************************************************************************************
# 3rd code:

#EXAMPLE 3:
'''Find number of lines with more than 10 words in each file.'''

'''
Steps:
Create an empty dictionary to store file name and line count information.
Iterate over all the files in the 'shakespeare_texts' directory using os.listdir() method.
Open each file and read its content.
Set the line count to 0 for the current file.
Iterate over each line in the file.
Split the line into words and count the number of words in the line using the len() method.
If the number of words in the line is greater than 10, increment the line count.
Store the line count as a value in the line count dictionary, with the file name as the key.
Close the file.
Repeat steps 3-9 for each file in the directory.
Print the line count dictionary containing the number of lines with more than 10 words in each file.
'''

import os

line_counts = {}

for file_name in os.listdir('shakespeare_texts'):
    file = open(os.path.join('shakespeare_texts', file_name), 'r')
    line_count = 0
    for line in file:

        word_count = len(line.split())

        if word_count > 10:
            line_count += 1

    line_counts[file_name] = line_count
    file.close()

print(line_counts)

****************************************************************************************************************************************
# 4th code:

#EXAMPLE 4:
'''Find number of words spoken by each character in all the plays.'''

'''
Steps:
Import necessary libraries - os and re
Define a regular expression pattern using re.compile function.
a. The pattern should match lines starting with a capitalized word (a character's name) or a sequence of capitalized words (a character's title).
b. The pattern should capture the character's name or title in the first group.
c. The pattern should capture any text following the character's name or title up to the first empty line in the second group.
d. The pattern should use positive lookahead to ensure that the empty line is followed by another line starting with a capitalized word.
Define a directory where the text files to be processed are located.
Create two empty dictionaries to store the character names and their lines.
Iterate over each file in the directory using os.listdir function.
Check if the file has a .txt extension using the endswith method.
If the file is a text file, open it and read the data.
Use the re.findall function with the compiled pattern to extract all the character names and their lines from the file.
Iterate over each match in the result of re.findall.
Extract the character name and dialogue from the match.
If the character name already exists in the character_names dictionary, add the dialogue to the existing value in the character_lines dictionary.
If the character name does not exist in the character_names dictionary, add the character name to the dictionary with a value of 1 and add the dialogue to the character_lines dictionary.
Iterate over the character_lines dictionary and calculate the total number of words for each character's lines using the split method to split each line into words and the len function to count the number of words.
Print the character name and total number of words for each character.
'''

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
    
*********************************************************************************************************************************
# 5th Code :

    
'''
Steps:
Import necessary libraries - os and re.
Define a regular expression pattern using re.compile function.
a. The pattern should match lines starting with a capitalized word (a character's name) or a sequence of capitalized words (a character's title).
b. The pattern should capture the character's name or title in the first group.
c. The pattern should capture any text following the character's name or title up to the first empty line in the second group.
d. The pattern should use positive lookahead to ensure that the empty line is followed by another line starting with a capitalized word.
Define a directory where the text files to be processed are located.
Create two empty dictionaries to store the character names and their lines.
Iterate over each file in the directory using os.listdir function.
Check if the file has a .txt extension using the endswith method.
If the file is a text file, open it and read the data.
Use the re.findall function with the compiled pattern to extract all the character names and their lines from the file.
Iterate over each match in the result of re.findall.
Extract the character name and dialogue from the match.
If the character name already exists in the character_names dictionary, add the dialogue to the existing value in the character_lines dictionary.
If the character name does not exist in the character_names dictionary, add the character name to the dictionary with a value of 1 and add the dialogue to the character_lines dictionary.
Iterate over the character_lines dictionary.
Split the lines into words using the split method.
Create an empty dictionary to store the word counts.
Iterate over each word in the lines.
If the word already exists in the word_count dictionary, add 1 to its value.
If the word does not exist in the word_count dictionary, add the word to the dictionary with a value of 1.
Sort the word_count dictionary by value in descending order using the sorted function and the lambda function.
Print the character name.
Iterate over the first 10 items in the sorted_words list.
Print the word and its count.
Add a blank line after each character's output.
'''

#EXAMPLE 5:
'''Find 10 most common words spoken by each character'''
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
    words = lines.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print(f"{character}:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")
    print()
    
**********************************************************************************************************************************
# Combined 4th and 5th code:

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

*************************************************************************************************************************************
# 6th Code:
'''
Steps:
Set the directory path as a string variable using r'path' format.
Set the file path variable using os.path.join() method to combine the directory path and 'shakespeare_texts' folder name.
Create an empty list to store file information.
Iterate over each file in the file path using os.listdir() method.
Get the full path of the file using os.path.join() method.
Get the size of the file in bytes using os.path.getsize() method.
Get the last modified datetime of the file using os.path.getmtime() method.
Append a dictionary of file information to the file_info_list containing the file name, size, last modified datetime, and absolute path.
Open a new CSV file in write mode using 'w' flag and newline='' parameter.
Define the field names for the CSV file as a list of strings.
Create a DictWriter object using the csv module and write the header using the writer.writeheader() method.
Write the rows of file_info_list to the CSV file using the writer.writerows() method.
Open the same CSV file in read mode using 'r' flag.
Create a CSV reader object using the csv module.
Iterate over each row in the CSV file using a for loop.
Print each row to the console.
'''

#EXAMPLE 6:
'''Find the following information about each file and store in a single csv:
Size in bytes
Last modified datetime
Absolute path
'''
import os
import csv

dir_path = r'C:\Users\Prafull_Thokal'
file_path = os.path.join(dir_path, 'shakespeare_texts')

file_info_list = []

for file_name in os.listdir(file_path):
    full_path = os.path.join(file_path, file_name)
    size = os.path.getsize(full_path)
    mod_time = os.path.getmtime(full_path)
    file_info_list.append({
        'File Name': file_name,
        'Size': size,
        'Last Modified': mod_time,
        'Absolute Path': full_path
    })
with open('file_info.csv', 'w', newline='') as csvfile:
    # Define the fieldnames for the CSV file
    fieldnames = ['File Name', 'Size', 'Last Modified', 'Absolute Path']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(file_info_list)
with open('file_info.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)