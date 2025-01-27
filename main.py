import feedparser
import time
URL = "https://dalcheonroadhead.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 12

# write down static Markdown text

markdown_text = """
![jeonsoomin_portfolio](https://github.com/user-attachments/assets/c076d2d2-df81-4202-8f56-8efc44a3bf23)
![project title](https://github.com/user-attachments/assets/48879d66-ce46-46b3-8972-bbe90609fdf3)

| [<img src="https://github.com/user-attachments/assets/e71935c5-6d37-46a1-b988-331a1668cf28" alt="5" />](https://github.com/6QuizOnTheBlock/OurClass) | [<img src="https://github.com/user-attachments/assets/e1677fb9-64d6-46b7-8cb0-1a1b57810fe2" alt="6" />](https://github.com/dalcheonroadhead/walk-walk) | [<img src="https://github.com/user-attachments/assets/3c7c6966-5c38-41b2-8071-0bd123a1eea5" alt="9" />](https://github.com/sesac-dev/eazione-back) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![8](https://github.com/user-attachments/assets/19770d6e-007e-46d9-9e21-733ece7eff19)](https://github.com/dalcheonroadhead/solsol-pokect) | [![7](https://github.com/user-attachments/assets/0ff8aeb3-47ef-4e05-bac1-158fa271b81a)](https://github.com/dalcheonroadhead/kkakka) | [![General Electronic Music Album Cover in Green and Pink Cartoony Mixed Media Style](https://github.com/user-attachments/assets/7a22f90b-823b-4873-bb38-a72cb2b3f0cd)](https://github.com/dalcheonroadhead/real-time-chat-server) |

[<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dalcheonroadhead&layout=donut&theme=tokyonight" alt="Top Langs" width="40%" />](https://github.com/anuraghazra/github-readme-stats)<img src="https://github-readme-stats.vercel.app/api?username=dalcheonroadhead&show_icons=true&theme=tokyonight" alt="dalcheonroadhead's GitHub stats" width="59%"  />
[<img src="https://github-readme-activity-graph.vercel.app/graph?username=dalcheonroadhead&theme=tokyo-night" alt="contribute"/>](https://github.com/ashutosh00710/github-readme-activity-graph)

👋 Today's visitor : <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdalcheonroadhead&count_bg=%23102C57&title_bg=%23102C57&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false" width="150%"/></a>
"""

