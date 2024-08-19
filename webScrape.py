# Import required libraries
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# Step 1: Download the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
response = requests.get(url)

# Step 2: Create a soup object
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Scrape language names and salaries
languages = []
salaries = []

# Find all table rows
table_rows = soup.find_all('tr')

# Step 4: Iterate through rows to get the data
for row in table_rows[1:]:  # Skip the header row
    cols = row.find_all('td')
    language = cols[0].text.strip()
    salary = cols[1].text.strip()
    
    languages.append(language)
    salaries.append(salary)

# Step 5: Save data to CSV file
with open('popular-languages.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Language', 'Average Salary'])
    writer.writerows(zip(languages, salaries))

print("Data scraped and saved to popular-languages.csv successfully!")

# Step 6: Read the CSV file using Pandas
df = pd.read_csv('popular-languages.csv')

# Display the dataframe
print(df.head())

