# Project_1_Web_scraping_Shakespeare_plays_website
This is a Python project for web scraping Shakespeare's plays website. The objective of this project is to download the first 5 text files from the given URL and store them in a separate folder. The project also aims to extract various information from the downloaded files such as the number of words spoken by each character, the number of lines with more than 10 words in each file, and the 10 most common words spoken by each character.

To accomplish this, the project uses Python libraries such as BeautifulSoup and requests for web scraping, and pandas for data analysis and storage. The project first downloads the text files from the given URL using a Python script and stores them in a separate folder. Then, it extracts all { file name : { line number : number of words in the line } } combinations in a dictionary. The project also finds the number of lines with more than 10 words in each file and the number of words spoken by each character in all the plays.

Furthermore, the project finds the 10 most common words spoken by each character and stores the following information about each file in a single CSV file: Size in bytes, Last modified datetime, and Absolute path. The project achieves all of these objectives by using efficient web scraping techniques and data analysis tools.

This project provides a great opportunity to learn web scraping and data analysis with Python. The code is open-source and available on GitHub for anyone to use and contribute to.
