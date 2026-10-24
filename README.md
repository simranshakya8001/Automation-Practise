# Web Scraping Automation

Python scripts that scrape websites and save the data to CSV files automatically.

## Scripts

| File | What it does |
|---|---|
| `books_scraper.py` | Scrapes 1000 books (title, price, rating) from [books.toscrape.com](https://books.toscrape.com) and saves them to `books.csv` |
| `news.py` | Scrapes the top stories (title, points, link) from [Hacker News](https://news.ycombinator.com) |
| `auto_news.py` | Runs the news scraper automatically every 15 minutes and saves each run as a separate CSV snapshot |

## How I built it

**1. Books scraper**
- Used `requests` to download the page HTML
- Used `BeautifulSoup` to find every book on the page (`article` tag with class `product_pod`)
- Extracted the title, price and star rating of each book
- Added a `for` loop to repeat this for all 50 pages (1000 books)
- Saved everything to `books.csv` using Python's `csv` module

**2. Hacker News scraper**
- Inspected the page in the browser (right-click, then Inspect) to find where the stories live
- Extracted the title, points and link of each story
- Added a User-Agent header so the request looks like it comes from a browser
- Saved each run to a CSV file with the date and time in its name, so old files are never overwritten

**3. Automation**
- Wrapped the scraping logic into functions
- Added `time.sleep()` to run the scraper automatically at a fixed interval
- Added `try/except` so the script keeps running even if one request fails
- Each run saves a new snapshot, so the changes in the data can be compared over time

## How to use

**1. Install Python 3** from [python.org](https://www.python.org/downloads/)
(tick "Add python.exe to PATH"
