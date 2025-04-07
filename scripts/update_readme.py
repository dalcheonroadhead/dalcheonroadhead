import os
from cairosvg import svg2png

SVG_DIR = "svg_cards"
PNG_DIR = "png_cards"
README_PATH = "README.md"
START_TAG = "<!-- BLOG-POST-START -->"
END_TAG = "<!-- BLOG-POST-END -->"

# GitHub Repository 이름 추출 (예: dalcheonroadhead/svg-blog)
repo_name = os.environ.get("GITHUB_REPOSITORY", "dalcheonroadhead/svg-blog")

# PNG 카드 폴더 생성
os.makedirs(PNG_DIR, exist_ok=True)

# SVG → PNG 변환 및 README에 들어갈 <img> 라인 준비
lines = []
for filename in sorted(os.listdir(SVG_DIR)):
    if filename.endswith(".svg"):
        svg_path = os.path.join(SVG_DIR, filename)
        png_filename = filename.replace(".svg", ".png")
        png_path = os.path.join(PNG_DIR, png_filename)

        # PNG로 변환 (cairosvg 필요)
        with open(svg_path, "r", encoding="utf-8") as svg_file:
            svg2png(bytestring=svg_file.read().encode("utf-8"), write_to=png_path)

        # 이미지 URL 작성
        png_url = f"https://raw.githubusercontent.com/{repo_name}/main/{PNG_DIR}/{png_filename}"
        lines.append(f'<img src="{png_url}" width="600" height="200"/>')

# README.md 내용 갱신
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find(START_TAG)
end = content.find(END_TAG)

if start != -1 and end != -1:
    new_block = START_TAG + "\n" + "\n".join(lines) + "\n" + END_TAG
    updated = content[:start] + new_block + content[end + len(END_TAG):]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
