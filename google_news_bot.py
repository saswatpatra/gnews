import feedparser
from datetime import datetime
import os

CATEGORIES = {
    "top": "https://news.google.com/rss",
    "technology": "https://news.google.com/rss/headlines/section/technology",
    "sports": "https://news.google.com/rss/headlines/section/sports",
    "entertainment": "https://news.google.com/rss/headlines/section/entertainment",
    "science": "https://news.google.com/rss/headlines/section/science"
}

def fetch(category, url):
    parsed = feedparser.parse(url)
    return [entry.title for entry in parsed.entries]

def build_markdown(results, timestamp):
    lines = [f"# Google News Update ({timestamp})", ""]
    for cat, headlines in results.items():
        lines.append(f"## {cat.capitalize()}")
        for h in headlines:
            lines.append(f"- {h}")
        lines.append("")  # blank line between categories
    return "\n".join(lines)

def run():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")
    results = {}

    for cat, url in CATEGORIES.items():
        results[cat] = fetch(cat, url)

    md_content = build_markdown(results, timestamp)

    os.makedirs("news", exist_ok=True)
    filename = f"news/{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)

    print("Saved:", filename)

if __name__ == "__main__":
    run()
