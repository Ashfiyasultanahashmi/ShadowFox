import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com"
header = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
}
response = requests.get(url, headers=header)
if response.ok:
    content = BeautifulSoup(response.text, 'html.parser')
    print("Scraped content:")
    quote = content.select('span.text')
    for i, quote in enumerate(quote, start=1):
        print(f"{i}. {quote.get_text(strip=True)}")
else:
    print(f"Failed to fetch data")
