import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import threading


# Send a GET request to the webpage
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser") #parsing the information in a forn of html

movie_data = soup.find_all( "li", class_="ipc-metadata-list-summary-item") 
#print(soup) #prints the hole html data   ipc-metadata-list-summary-item
#the data we are going to scrape

i=1

movie_list = []
"""
def job(movie_list,j):
    print("starting thread "+ movie_list[j]['name'])
    response = requests.get(full_imdb_url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    genres =soup.findAll('span', class_='ipc-chip__text')
    movie_list[j]['genres'] = []

    for g in genres:
        if not g.text.startswith('Back'):
            movie_list[j]['genres'].append(g.text)

    #the director of the movie

    director = soup.find('div', class_='ipc-metadata-list-item__content-container')
    if director is None:
        movie_list[j]['director']='*******'
    else:
        director=director.text
        movie_list[j]['director']=director



    
    #the rating of the movie
    rating = soup.find('span', class_='sc-bde20123-1 cMEQkK')
    if rating is None:
        movie_list[j]['rating']='*******'
    else:
        rating=rating.text
        movie_list[j]['rating']=rating
    
    
    #released year of the movie and the length of the movie
    yearAndTime=soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt').text
    year=yearAndTime[:4]
    movie_list[j]['year']= year
    time=yearAndTime[-6:]
    movie_list[j]['time']= time
   
    #the main actors of the movie
    allActors = soup.findAll('a', attrs={'data-testid': 'title-cast-item__actor'})
    movie_list[j]['actors']=[]
    for a in range (5):
        movie_list[j]['actors'].append(allActors[a].text)

    print("ending thread "+ movie_list[j]['name'])

"""

for store in movie_data:
    temp_dict = {}
    print(i)
    i+=1
    #the name of the movie
    name = store.find ('h3' ,class_= 'ipc-title__text' ).text.split('. ')[1]
    #creating a list of the movies genres
    imdb_url = store.find('a', class_='ipc-lockup-overlay').get('href')
    full_imdb_url = f"https://www.imdb.com{imdb_url}"
    #temp_dict['full_imdb_url'] = full_imdb_url
    temp_dict['name'] = name
    print(name)
    response = requests.get(full_imdb_url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    genres =soup.findAll('span', class_='ipc-chip__text')
    temp_dict['genres'] = []

    for g in genres:
        if not g.text.startswith('Back'):
            temp_dict['genres'].append(g.text) 

    #the director of the movie

    director = soup.find('div', class_='ipc-metadata-list-item__content-container')
    if director is None:
        temp_dict['director']='*******'
    else:
        director=director.text
        temp_dict['director']=director

    
    #the rating of the movie
    rating = soup.find('span', class_='sc-bde20123-1 cMEQkK')
    if rating is None:
        temp_dict['rating']='*******'
    else:
        rating=rating.text
        temp_dict['rating']=rating
    
    
    #released year of the movie and the length of the movie
    yearAndTime=soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt')
    if yearAndTime is not None:
        year=yearAndTime.text[:4]
        temp_dict['year']= year
        try:
            time=yearAndTime.text[yearAndTime.text.index(' ')-2 : ]
        except:
            time=yearAndTime.text[-2: ]
        print(time)
        temp_dict['time']= time
    else:
        temp_dict['year']='^^^^^^'
        temp_dict['time']='^^^^^^'
   
    #the main actors of the movie
    allActors = soup.findAll('a', attrs={'data-testid': 'title-cast-item__actor'})
    temp_dict['actors']=[]
    #check ifn allActors[a] exists!!!!!!!!!!!!!!!!!!!!!!
    for a in range(5):
        if len(allActors) > a:
            temp_dict['actors'].append(allActors[a].text)
        else:
            break  
    
    movie_list.append(temp_dict)
"""
threads = []
for j in range(len(full_imdb_url)):
    t= threading.Thread(target=job, args=(movie_list,j,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
"""


df = pd.DataFrame(movie_list)

# Specify CSV file path
csv_file_path = 'movies.csv'

# Export DataFrame to CSV
df.to_csv(csv_file_path, index=False)


"""
for store in movie_data:
    print(i)
    temp_dict = {}
    #the name of the movie
    name = store.find ('h3' ,class_= 'ipc-title__text' ).text.split('. ')[1]
    temp_dict['name'] = name
    
    #creating a list of the movies genres
    imdb_url = store.find('a', class_='ipc-lockup-overlay').get('href')
    full_imdb_url = f"https://www.imdb.com{imdb_url}"
    i+=1
    response = requests.get(full_imdb_url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    
    genres =soup.findAll('span', class_='ipc-chip__text')
    temp_dict['genres'] = []
    for g in genres:
        if not g.text.startswith('Back'):
            temp_dict['genres'].append(g.text)

    print(name)
    #the director of the movie

    director = soup.find('div', class_='ipc-metadata-list-item__content-container')
    if director is None:
        temp_dict['director']='*******'
    else:
        director=director.text
        temp_dict['director']=director



    
    #the rating of the movie
    rating = soup.find('span', class_='sc-bde20123-1 cMEQkK')
    if rating is None:
        temp_dict['rating']='*******'
    else:
        rating=rating.text
        temp_dict['rating']=rating
    
    
    #released year of the movie and the length of the movie
    yearAndTime=soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt').text
    year=yearAndTime[:4]
    temp_dict['year']= year
    time=yearAndTime[-6:]
    temp_dict['time']= time
   
    #the main actors of the movie
    allActors = soup.findAll('a', attrs={'data-testid': 'title-cast-item__actor'})
    temp_dict['actors']=[]
    for a in range (5):
        temp_dict['actors'].append(allActors[a].text)


movie_header = "Title,Genres,Director,Rating,Released year,Length,Main actros "
with open("movie_list.csv", "w") as f:
    f.write(movie_header)
    for movie in movie_list:
        f.write(movie['name'] + ',')
        for genre in movie['genres']:
            f.write(genre + " "  )
        f.write(',')
        f.write(movie['director'] + ',')
        f.write(movie['rating'] + ',')
        f.write(movie['year'] + ',')
        f.write(movie['time'] + ',')
        for actor in movie['actors']:
            f.write(actor + " " )
        f.write(',')  
 """