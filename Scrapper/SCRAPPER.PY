import requests
from bs4 import BeautifulSoup
import csv
import time
import os
from datetime import datetime

URL = "https://news.ycombinator.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
INTERVAL_MINUTES = 15   # testing ke liye 1 rakh sakti ho
TOTAL_RUNS = 4          # kitni baar chalana hai

os.makedirs("snapshots", exist_ok=True)


def scrape_news():
    response = requests.get(URL, headers=HEADERS, timeout=15)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    news = []
    for story in soup.find_all("tr", class_="athing"):
        link_tag = story.select_one("span.titleline > a")
        title = link_tag.text
        link = link_tag["href"]
        if not link.startswith("http"):
            link = URL + link

        info_row = story.find_next_sibling("tr")
        score_tag = info_row.find("span", class_="score")
        points = score_tag.text if score_tag else "0 points"

        news.append([title, points, link])
    return news


def save_csv(news):
    filename = "snapshots/news_" + datetime.now().strftime("%Y-%m-%d_%H-%M") + ".csv"
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Points", "Link"])
        writer.writerows(news)
    return filename


for run in range(1, TOTAL_RUNS + 1):
    try:
        news = scrape_news()
        filename = save_csv(news)
        print(f"Run {run}/{TOTAL_RUNS} done -> {filename} ({len(news)} stories)")
    except Exception as e:
        print(f"Run {run} fail hua:", e)

    if run < TOTAL_RUNS:
        print(f"{INTERVAL_MINUTES} minute ruk rahi hai...\n")
        time.sleep(INTERVAL_MINUTES * 60)

print("\nSab runs complete!")