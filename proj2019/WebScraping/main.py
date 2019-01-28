from bs4 import BeautifulSoup
import requests

#AC waveform tutorial on electronics-tutorials
res = requests.get("https://www.electronics-tutorials.ws/accircuits/ac-waveform.html")
#print(res)

soup = BeautifulSoup(res.text, 'html.parser') # Download the HTML
#print(soup)

for item in soup.find_all("p"): # Find all the text starting with <p> in the HTML
    if item.text.startswith("In the next tutorial"):break
    print(item.text)



# res = requests.get("https://www.electronics-tutorials.ws/inductor/inductor.html")
# #print(res)
#
# soup = BeautifulSoup(res.text, 'html.parser') # Download the HTML
# #print(soup)
#
# for item in soup.find_all("p"): # Find all the text starting with <p> in the HTML
#     if item.text.startswith("In the next tutorial"):break
#     print(item.text)
