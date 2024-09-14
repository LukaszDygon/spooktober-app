import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_years_in_film"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
ul_tags = soup.find_all("ul")

# Create a new line delimited file "input.csv"
with open("input.csv", "w") as f:
    for ul_tag in ul_tags:
        li_tags = ul_tag.find_all("li")
        for li_tag in li_tags:
            i_tags = li_tag.find_all("i")
            for i_tag in i_tags:
                a_tag = i_tag.find("a")
                if a_tag:
                    b_tag = li_tag.find("b")
                    f.write(f"{i_tag.text}|{b_tag.text if b_tag else ''}\n")