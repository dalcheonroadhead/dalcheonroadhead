import os
import feedparser
from xml.sax.saxutils import escape

SVG_DIR = "svg_cards"
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")
START_TAG = "<!-- BLOG-POST-START -->"
END_TAG = "<!-- BLOG-POST-END -->"

# GitHub Repository 이름 추출 (예: dalcheonroadhead/svg-blog)
repo_name = os.environ.get("GITHUB_REPOSITORY", "dalcheonroadhead/dalcheonroadhead")

# 티스토리 RSS에서 최근 글 5개 파싱
feed = feedparser.parse("https://dalcheonroadhead.tistory.com/rss")
entries = feed.entries[:5]

# SVG → PNG 변환 및 README에 들어갈 <img> 라인 준비
svg_lines = []
for i, entry in enumerate(entries):
    link = escape(entry.link)
    align = "left" if i % 2 == 0 else "right"
    svg_url = f"https://raw.githubusercontent.com/{repo_name}/main/scripts/{SVG_DIR}/card_{i+1}.svg"
    svg_lines.append(f'<a href="{link}" target="_blank"><img src="{svg_url}" align="{align}" width="600" height="200"/></a> <br/>')

# README.md 내용 갱신
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find(START_TAG)
end = content.find(END_TAG)

if start != -1 and end != -1:
    new_block = START_TAG + "\n" + "\n".join(svg_lines) + "\n" + END_TAG
    updated = content[:start] + new_block + content[end + len(END_TAG):]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
