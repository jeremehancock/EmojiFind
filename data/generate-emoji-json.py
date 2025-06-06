import json
import requests
import re

URL = "https://unicode.org/Public/emoji/15.1/emoji-test.txt"
OUTPUT_FILE = "emojis.json"
STOPWORDS = {
    "with", "and", "the", "of", "on", "in", "a", "an", "to", "for",
    "face", "person", "skin", "tone", "light", "medium", "dark"
}

def download_emoji_test():
    response = requests.get(URL)
    response.raise_for_status()
    return response.text.splitlines()

def parse_lines(lines):
    emojis = []
    version_pattern = re.compile(r'^E\d+(\.\d+)?$')  # matches E1.0, E15.1, etc.

    for line in lines:
        if "; fully-qualified" not in line or "#" not in line:
            continue

        try:
            parts = line.split("#")[1].strip().split()
            emoji = parts[0]
            words = parts[1:]
        except IndexError:
            continue

        # Filter out stopwords and version markers
        seen = set()
        keywords = [
            word for word in words
            if word not in STOPWORDS and not version_pattern.match(word)
            and word not in seen and not seen.add(word)
        ]

        emojis.append({
            "emoji": emoji,
            "keywords": keywords
        })

    return emojis

def main():
    lines = download_emoji_test()
    emoji_data = parse_lines(lines)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(emoji_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Wrote {len(emoji_data)} emojis to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

