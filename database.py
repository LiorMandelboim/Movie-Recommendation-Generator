from time import sleep
import pandas as pd
import requests
from bs4 import BeautifulSoup



# Send a GET request to the webpage
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
headers = {
    'Accept-Language': 'en-US',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser") #parsing the information in a forn of html

movie_data = soup.find_all( "li", class_="ipc-metadata-list-summary-item") 
#print(soup) #prints the hole html data   ipc-metadata-list-summary-item
#the data we are going to scrape

i=1

movie_list = []


for store in movie_data:
    sleep(1)
    temp_dict = {}
    print(i)
    i+=1
    #the name of the movie
    name = store.find ('h3' ,class_= 'ipc-title__text' ).text.split('. ')[1]
    #creating a list of the movies genres
    imdb_url = store.find('a', class_='ipc-lockup-overlay').get('href')
    full_imdb_url = f"https://www.imdb.com{imdb_url}"
    temp_dict['name'] = name
    print(name)
    response = requests.get(full_imdb_url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    while soup is None:
        sleep(2)
        print("trying again")
        soup = BeautifulSoup(html_content, "html.parser")
    genres =soup.findAll('span', class_='ipc-chip__text')
    temp_dict['genres'] = []

    for g in genres:
        if not g.text.startswith('Back'):
            temp_dict['genres'].append(g.text.lower()) 

    #the director of the movie

    director = soup.find('div', class_='ipc-metadata-list-item__content-container')
    if director is None:
        continue
    else:
        temp_dict['director']=director.text.lower()

    
    #the rating of the movie
    rating = soup.find('span', class_='sc-bde20123-1 cMEQkK')
    if rating is None:
        continue
    else:
        rating=rating.text
        temp_dict['rating']=rating
    
    
    #released year of the movie and the length of the movie
    yearAndTime=soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt')
    if yearAndTime is not None:
        yearAndTime=yearAndTime.text.replace('Not Rated' , 'NR')
        year=yearAndTime[:4]
        temp_dict['year']= year
        try:
            time=yearAndTime[yearAndTime.index(' ')-2 : ]
        except:
            time=yearAndTime[-2: ]
        print(time)
        temp_dict['time']= time
    else:
        continue
   
    #the main actors of the movie
    allActors = soup.findAll('a', attrs={'data-testid': 'title-cast-item__actor'})
    temp_dict['actors']=[]
    for a in range(5):
        if len(allActors) > a:
            temp_dict['actors'].append(allActors[a].text.lower())
        else:
            break 

    temp_dict['url'] = full_imdb_url 

    meta_tag = soup.find('meta' , property="og:image")

        # Extract the value from the content attribute
    try:
        image_url = meta_tag['content']
    except:
        continue


    temp_dict['picture'] = image_url
    
    movie_list.append(temp_dict)



df = pd.DataFrame(movie_list)

# Specify CSV file path
csv_file_path = 'movies.csv'

# Export DataFrame to CSV
df.to_csv(csv_file_path, index=False)


