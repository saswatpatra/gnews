import feedparser, json
from datetime import datetime

CATEGORIES = {
    "top": "https://news.google.com/rss",
    "technology": "https://news.google.com/rss/headlines/section/technology",
    "sports": "https://news.google.com/rss/headlines/section/sports",
    "entertainment": "https://news.google.com/rss/headlines/section/entertainment",
    "science": "https://news.google.com/rss/headlines/section/science"
}

def fetch_category(name, url):
    parsed = feedparser.parse(url)
    return [entry.title for entry in parsed.entries]

def run_bot():
    output = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "news": {}
    }

    for category, url in CATEGORIES.items():
        headlines = fetch_category(category, url)
        output["news"][category] = headlines

    with open("google_news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print("Scraped categories:", ", ".join(CATEGORIES.keys()))
    print("Saved to google_news.json")

if __name__ == "__main__":
    run_bot()
