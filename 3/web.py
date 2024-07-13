# Script for web scraping and data fetching from APIs.

import requests
from bs4 import BeautifulSoup
from typing import List
import random

# Rotating user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
]

HEADERS = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def scrape_news(url: str, verbose: bool = False) -> List[str]:
    """
    Scrapes news articles from a given URL.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP error codes
        print("[html]" + response.text if verbose else f"[success] Scraped {url}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

# Example usage
if __name__ == "__main__":
    news_articles = scrape_news("https://economictimes.indiatimes.com/topic/market-trend", verbose=False)
    print(news_articles)
