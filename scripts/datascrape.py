import requests
from bs4 import BeautifulSoup

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get("https://www.zomato.com/bangalore/top-restaurants", headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser")

top_rest = soup.find_all("div",attrs={"class": "sc-bke1zw-1 ixpGXU"})
top_rest.extend(soup.find_all("div",attrs={"class": "sc-bke1zw-1 ijNBpr"}))
top_rest.extend(soup.find_all("div",attrs={"class": "sc-bke1zw-1 dFBCmH"}))
top_rest.extend(soup.find_all("div",attrs={"class": "sc-bke1zw-1 djiZfy"}))

list_rest = []
print(top_rest)
for rest in top_rest:
    dataframe = {}
    dataframe["rest_name"] = rest.find("div", attrs={"class": "sc-fzmwXB fWLrQG"})
    print(dataframe["rest_name"])
    list_rest.append(dataframe)