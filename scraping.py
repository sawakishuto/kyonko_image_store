import requests
from bs4 import BeautifulSoup
import os

# ブログのURL
url = "https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&ct=6"

# リクエストを送信してHTMLを取得
response = requests.get(url)
html_content = response.content

# BeautifulSoupを使ってHTMLをパース
soup = BeautifulSoup(html_content, "html.parser")

# 画像タグを全て取得
img_tags = soup.find_all("img")

# 画像を保存するディレクトリを作成
if not os.path.exists("images"):
    os.makedirs("images")

# 各画像タグから画像URLを取得し、保存
for idx, img_tag in enumerate(img_tags):
    img_url = img_tag.get("src")
    
    # 相対URLの場合は絶対URLに変換
    if not img_url.startswith("http"):
        img_url = f"{url}/{img_url}"
    
    # 画像をダウンロード
    img_data = requests.get(img_url).content
    
    # 画像を保存
    img_filename = f"images/image_{idx}.jpg"
    with open(img_filename, "wb") as f:
        f.write(img_data)
    
    print(f"{img_filename} を保存しました。")