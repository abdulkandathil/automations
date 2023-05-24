import csv
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.islamvakti.net/home/index/13/850/10433"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table element containing the data
table = soup.find("table", class_="table")

# Check if the table was found
if table is not None:
    # Create a CSV file to store the data
    csv_file = open("scraped_data.csv", "w", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["City", "Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"])

    # Iterate over each row in the table (except the header row)
    for row in table.find_all("tr")[1:]:
        # Extract the data from each column
        columns = row.find_all("td")
        city = columns[0].text.strip()
        fajr = columns[1].text.strip()
        sunrise = columns[2].text.strip()
        dhuhr = columns[3].text.strip()
        asr = columns[4].text.strip()
        maghrib = columns[5].text.strip()
        isha = columns[6].text.strip()

        # Write the extracted data to the CSV file
        csv_writer.writerow([city, fajr, sunrise, dhuhr, asr, maghrib, isha])

    # Close the CSV file
    csv_file.close()

    print("Data has been scraped and saved to 'scraped_data.csv'.")
else:
    print("Table not found on the webpage.")
