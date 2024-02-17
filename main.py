import ast
import json
import operator
import pandas as pd 


df = pd.read_csv('movies.csv')
pref = {'genres' : 'Action' , 'director' : None , 'rating' : 8.5 , 'year' : 1990 ,
        'time' : '120-150' , 'actors' : 'Brad Pitt'}

final_scores = {}

def place_in_list(attr_list: str, user_input: str):
    modified_l = ast.literal_eval(attr_list)
    try:
        return float(1/(modified_l.index(user_input)+1))
    except:
          return 0

def hours_minutes_to_minutes(time_str):
    try:
        components = time_str.split('h')

        hours = 0
        minutes = 0

        if len(components) > 0:
                hours = int(components[0])

        if len(components) > 1:
                minutes_str = components[1].replace('m', '').strip()
                if minutes_str:
                        minutes = int(minutes_str)

        total_minutes = hours * 60 + minutes
        return total_minutes
    except:
         return 0
    
def is_same_value(value: str , user_input: str):
      return  1 if value==user_input else 0

def is_value_gt(value , user_input):
      return  1 if float(value)>=float(user_input) else 0

def is_value_in_range(value:str , user_input:str):
      time_in_min=hours_minutes_to_minutes(value)
      try:
            range = user_input.split('-')
            return 1 if (time_in_min>= int(range[0]) and time_in_min<=int(range[1])) else 0
      except:
            return 1 if(time_in_min>=int(user_input[:-1])) else 0



weights = {'genres' : {'score' : 10, 'func' : place_in_list} , 
           'director' : {'score' : 2 , 'func' : is_same_value} , 
           'rating' : {'score' : 8, 'func' : is_value_gt}  , 
           'year' : {'score' : 1, 'func' : is_value_gt}  ,
        'time' : {'score' : 4 , 'func': is_value_in_range}  , 
        'actors' : {'score' : 15 , 'func' : place_in_list}}

for _, value in df.iterrows():
      final_scores[value['name']]=0 
      for k , v in weights.items():
         if pref[k] is not None:
                final_scores[value['name']]+=v['score']*v['func'](value[k], pref[k]) 


sorted_movies = dict(sorted(final_scores.items(), key=operator.itemgetter(1) , reverse=True))
count = 0
for key, value in sorted_movies.items():
    print(key, ':', value)
    count += 1
    if count == 5:
        break
      

           
            
    

