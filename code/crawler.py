#%%
import requests
from bs4 import BeautifulSoup

#%%
wiki = "https://zh.wikipedia.org/wiki/%E7%A5%9E%E9%B5%B0%E4%BF%A0%E4%BE%B6%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8"
page = requests.get(wiki)

#%%
soup = BeautifulSoup(page.text, "html.parser")
sel = soup.select("div.mw-parser-output ul li a")
for s in sel:
    print(s.text)