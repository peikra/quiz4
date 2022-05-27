import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
file =  open('movies.csv','w', newline='\n')
#file.write("Title, Year  '\n' ")
obj = csv.writer(file)
obj.writerow(['Title','Year'])


page = 1



while page <= 6 :
    url = 'https://geo.saitebi.ge/main/new/' + str(page)
    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, 'html.parser')
    soub_soup = soup.find('div', id= 'content')
    #print(soub_soup)
    movies = soub_soup.find_all('div', class_= 'movie-items-wraper')
    #print(movies)

    for each in movies:
        title = each.find('div', class_ = 'h-title-origin').text
        print(title)
        year = each.find('div',class_='h-year').text
        print(year)
        #file.write(title + ',' + year + '\n')
        obj.writerow([title,year])
    page= page + 1
    sleep(5)










