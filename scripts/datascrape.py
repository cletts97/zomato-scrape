import requests
from bs4 import BeautifulSoup
import re
import pandas



# Provide user agent to trick server in to thinking it's being access by a client

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get("https://www.zomato.com/bangalore/best-delivery-restaurants", headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser") # Stores html content in a structured tree form

top_rest = soup.find_all("div",attrs={"class": "jumbo-tracker"}) # Grabs all the div's with class "jumbo-tracker"

regex_name = re.compile('sc-1hp8d8a-0.*')
regex_rating = re.compile('sc-1q7bklc-1.*')
#regex_cuisine = re.compile('sc-1hez2tp-0.*') # Unfortunately this results in 3 different dynamic css classes that are used so brings back random information.
# Will come back to this later once i've learned more about scraping webpages that use dynamic css


list_rest = []
for rest in top_rest:
    dataframe = {}
    dataframe["rest_name"] = rest.find("h4", attrs={"class": regex_name}).text
    dataframe["rest_rating"] = rest.find("div", attrs={"class": regex_rating}).text.replace('star-fill', '')
    #dataframe["rest_cuisine"] = rest.find("p", attrs={"class": regex_cuisine}).text # 3 different classes use this regex and there is no way to uniquely identify the desired field.
    list_rest.append(dataframe)

df = pandas.DataFrame(list_rest)
df.to_csv("zomato_results.csv", index=False)