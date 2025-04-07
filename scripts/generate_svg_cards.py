import feedparser
import os
from datetime import datetime
from xml.sax.saxutils import escape

RSS_URL = "https://dalcheonroadhead.tistory.com/rss"
SAVE_DIR = "svg_cards"
MAX_ITEMS = 5
CARD_WIDTH = 600
CARD_HEIGHT = 200

SVG_TEMPLATE = """
<svg width=\"600\" height=\"200\" xmlns=\"http://www.w3.org/2000/svg\">
    <image href=\"https://raw.githubusercontent.com/dalcheonroadhead/img-cloud/main/2025-04/Tistory_card_for_readMe.png\" x=\"0\" y=\"0\" width=\"100%\" height=\"100%\" />
    <text x=\"{x}24\" y=\"40\" font-size=\"14\" font-weight=\"bold\" fill=\"#FFF2CE\" text-anchor=\"{anchor}\">dalchoenroadhead.tistory.com</text>
    <text x=\"{x}24\" y=\"80\" font-size=\"22\" font-weight=\"bold\" fill=\"#FFF2CE\" text-anchor=\"{anchor}\">{title}</text>
    {tags_svg}
    <text x=\"{x}24\" y=\"180\" font-size=\"14\" fill=\"#FFF2CE\" text-anchor=\"{anchor}\">{pub_date}</text>
</svg>
"""


def format_tags(tags, x_offset):
    svg_tags = []
    current_x = x_offset
    for tag in tags:
        width = max(len(tag) * 8 + 20, 50)  # rough width calc
        svg_tags.append(f'<rect x=\"{current_x}\" y=\"125\" rx=\"8\" ry=\"8\" width=\"{width}\" height=\"20\" fill=\"#FFF2CE\"/>')
        svg_tags.append(f'<text x=\"{current_x + 6}\" y=\"139\" font-weight=\"bold\" fill=\"#FF6969\">{escape(tag)}</text>')
        current_x += width + 10
    return "\n    ".join(svg_tags)


def main():
    os.makedirs(SAVE_DIR, exist_ok=True)
    feed = feedparser.parse(RSS_URL)

    for i, entry in enumerate(feed.entries[:MAX_ITEMS]):
        title = escape(entry.title)
        date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
        tags = [tag.term for tag in entry.get("tags", [])] if "tags" in entry else []

        x_align = "" if i % 2 == 0 else str(CARD_WIDTH - 24 * 2 - 400)  # 좌우 기준 위치
        anchor = "start" if i % 2 == 0 else "start"  # text-anchor=start 고정

        tags_svg = format_tags(tags, 24 if i % 2 == 0 else 24)

        svg = SVG_TEMPLATE.format(
            x="" if i % 2 == 0 else "",
            title=title,
            pub_date=date,
            tags_svg=tags_svg,
            anchor=anchor
        )

        with open(os.path.join(SAVE_DIR, f"card_{i+1}.svg"), "w", encoding="utf-8") as f:
            f.write(svg)


if __name__ == "__main__":
    main()


# scripts/update_readme.py

import os

SVG_DIR = "svg_cards"
README_PATH = "README.md"
START_TAG = "<!-- BLOG-POST-START -->"
END_TAG = "<!-- BLOG-POST-END -->"

# 이미지 태그로 삽입
svg_lines = []
for filename in sorted(os.listdir(SVG_DIR)):
    if filename.endswith(".svg"):
        svg_url = f"https://raw.githubusercontent.com/dalcheonroadhead/{os.environ.get('GITHUB_REPOSITORY').split('/')[-1]}/main/{SVG_DIR}/{filename}"
        svg_lines.append(f'<img src="{svg_url}" width="600" height="200"/>')

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find(START_TAG)
end = content.find(END_TAG)

if start != -1 and end != -1:
    new_block = START_TAG + "\n" + "\n".join(svg_lines) + "\n" + END_TAG
    updated = content[:start] + new_block + content[end + len(END_TAG):]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)