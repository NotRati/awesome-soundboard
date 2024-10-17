import requests
from bs4 import BeautifulSoup
import re

def getLink(query, index):
    response = requests.get(f'https://www.myinstants.com/en/search/?name={query}') #get search
    if not response.ok:
        print("Error fetching the search")
        return ''
    soup = BeautifulSoup(response.text, 'html.parser') #parse for buttons
    buttons = soup.findAll('button', class_='small-button')
    links = []
    for button in buttons: #loop each button
        onclick = button.get('onclick') #get onclick code
        link = re.search(r"play\('([^']+)'\,",onclick).group(1) # get media link (the first in the group)
        link = "https://www.myinstants.com" + link.replace(' ', '+') #add the link to get the file
        links.append(link)

    return links[index]
        


    
    
    