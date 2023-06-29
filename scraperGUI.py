from bs4 import BeautifulSoup
import requests
import tkinter as tk



def scrape_website():
    url = "https://" + url_entry.get()
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')

    attrList = ['h1', 'h2', 'p', 'img']
    itemNum = 0

    for item in attrList:
        result_text.insert(tk.END, f"Item: {attrList[itemNum]}\n")
        result_text.insert(tk.END, f"{soup.findAll(item)}\n\n")

        with open("scraper.txt", 'a') as f:
            f.write(f"Item: {attrList[itemNum]}\n")
            f.write(str(soup.findAll(item)) + "\n\n")

        itemNum += 1

window = tk.Tk()
window.title("Web Scraper")

url_label = tk.Label(window, text="Enter URL: ")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

scrape_button = tk.Button(window, text="Scrape", command=scrape_website)
scrape_button.pack()

result_text = tk.Text(window, height=40, width=130)
result_text.pack()

window.mainloop()
