import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/fantastico/"

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the page.")
        return None

def extract_href_links(page_content):
    links = []
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        # Find all <a> tags (links) and get the 'href' attribute
        for link in soup.find_all('a', href=True):
            links.append(link.get('href'))
    return links

page_content = get_page(url)
if page_content:
    href_links = extract_href_links(page_content)
    
    # Save the links to a file named "links.txt"
    with open("links.txt", "w") as file:
        for link in href_links:
            file.write(link + "\n")
