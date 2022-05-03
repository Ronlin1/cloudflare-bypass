from bs4 import BeautifulSoup as beauty
import cloudscraper


# returns a CloudScraper instance
scraper = cloudscraper.create_scraper(delay=10, browser='chrome') #
url = "https://opensea.io/rankings"

info = scraper.get(url).text
soup = beauty(info, "html.parser")
soup = soup.find_all('script')

our_data = list()
for data in soup:
    our_data.append(data.get_text())
    # print(data.get_text())

print(our_data)
