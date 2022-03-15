from bs4 import BeautifulSoup as beauty
import cloudscraper


# returns a CloudScraper instance
scraper = cloudscraper.create_scraper(delay=10, browser='chrome') #
url = "https://opensea.io/rankings"

info = scraper.get(url).text
soup = beauty(info, "html.parser")
soup = soup.find_all('script')


for data in soup:
    print(data.get_text())

# for c in data:
#     print(c.get_text())

print(our_data)
