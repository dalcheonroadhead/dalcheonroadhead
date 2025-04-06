import feedparser

# 티스토리 RSS 주소
rss_url = "https://dalcheonroadhead.tistory.com/rss"
feed = feedparser.parse(rss_url)

max_items = 5
markdown_lines = []

for entry in feed.entries[:max_items]:
    title = entry.title
    link  = entry.link
    thumbnail = ""
    for media in entry.get("media_thumbnail", []):
        thumbnail = media["url"]
    markdown_lines.append(f'<a href="{link}"><img src="{thumbnail}" width="120"/><br>{title}</a><br><br>')

# README 파일 내용 교체
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start_tag = "<!-- BLOG-POST-START -->"
end_tag = "<!-- BLOG-POST-END -->"

new_content = start_tag + "\n" + "\n".join(markdown_lines) + "\n" + end_tag
updated = readme.split(start_tag)[0] + new_content + readme.split(end_tag)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)