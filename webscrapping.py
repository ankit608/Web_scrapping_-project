import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website to scrape
url = "https://www.scrapinghub.com/learn"  # Replace this with the actual URL you want to scrape

# Send a request to fetch the content of the page
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched the web page")
    page_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_content, "html.parser")

    # Example: Extract all headlines from the page
    # Modify the selector according to the website structure

    headlines = soup.find_all('h2')
    paragraphs = soup.find_all('p')

    # Create lists to store the extracted data
    titles = []
    links = []

    for headline in headlines:
        title = headline.get_text(strip=True)  # Get the text of the headline
        link = headline.find('a')['href'] if headline.find('a') else None  # Get the link (if present)

        titles.append(title)
        links.append(link)
    for paragraph in paragraphs:
        title = paragraph.get_text(strip=True)  # Get the text of the headline
        link =  paragraph.find('a')['href'] if paragraph.find('a') else None  # Get the link (if present)

        titles.append(title)
        links.append(link)

    # Create a DataFrame to structure the data
    data = {
        'Title': titles,
        'Link': links
    }

    df = pd.DataFrame(data)

    # Save the data to a CSV file
    df.to_csv('scraped_data.csv', index=False)
    print("Data has been saved to scraped_data.csv")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
