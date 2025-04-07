import os

SVG_DIR = "svg_cards"
README_PATH = "README.md"
START_TAG = "<!-- BLOG-POST-START -->"
END_TAG = "<!-- BLOG-POST-END -->"

# GitHub Repository 이름 추출 (예: dalcheonroadhead/svg-blog)
repo_name = os.environ.get("GITHUB_REPOSITORY", "dalcheonroadhead/svg-blog")

# SVG 파일들을 이미지 태그로 변환
svg_lines = []
for filename in sorted(os.listdir(SVG_DIR)):
    if filename.endswith(".svg"):
        svg_url = f"https://raw.githubusercontent.com/{repo_name}/main/scripts/{SVG_DIR}/{filename}"
        svg_lines.append(f'<img src="{svg_url}" width="600" height="200"/>')

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
