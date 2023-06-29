from bs4 import BeautifulSoup
import requests

inp = input("Enter URL: ")
url = "https://"+inp
x = requests.get(url)
soup = BeautifulSoup(x.text, 'html.parser')

#print(soup.prettify())

attrList = ['h1','h2','p','img']
itemNum=0
f = open("scraper.txt", 'w')

for item in attrList:
    print("Item: " +  attrList[itemNum])
    print(soup.findAll(item))
    
    f = open("scraper.txt", 'a')
    f.write("Item: " + attrList[itemNum])
    f.write(str(soup.findAll(item)))

    itemNum+=1
    
f.close()

