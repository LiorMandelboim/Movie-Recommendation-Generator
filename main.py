import ast
import json
import operator
import pandas as pd 
import difflib

class Movie_Recommendation:
      def __init__(self , movie_db='movies.csv'):
            self.df = pd.read_csv(movie_db)
            self.final_scores = {}
            self.weights = {'genres' : {'score' : 10, 'func' : self.place_in_list} , 
                        'director' : {'score' : 2 , 'func' : self.is_same_value} , 
                        'rating' : {'score' : 8, 'func' : self.is_value_gt}  , 
                        'year' : {'score' : 1, 'func' : self.is_value_gt}  ,
                        'time' : {'score' : 4 , 'func': self.is_value_in_range}  , 
                        'actors' : {'score' : 15 , 'func' : self.place_in_list}}
      
      def get_values(self, value):
            values = set()
            for x in self.df[value]:
                  modified_l = ast.literal_eval(x)
                  if not isinstance(modified_l,list):
                        modified_l = [modified_l]
                  for val in modified_l:
                        values.add(val)
            return list(sorted(values))
      
      
      
      def recommend(self, pref):
            for _, value in self.df.iterrows():
                  self.final_scores[value['name']]=0 
                  for k , v in self.weights.items():
                        if (k=='url'):
                              break
                        if pref[k] is not None:
                              if isinstance(pref[k], str):
                                    if (k == 'actors'):
                                      modified_l = ast.literal_eval(value[k])
                                      close_matches=difflib.get_close_matches(pref[k].lower(), modified_l , cutoff=0.9)
                                      if len(close_matches)>0:
                                           print(close_matches[0])
                                           self.final_scores[value['name']]+=v['score']*v['func'](value[k],close_matches[0] )    
                                    else:
                                          self.final_scores[value['name']]+=v['score']*v['func'](value[k], pref[k].lower()) 
                              elif isinstance(pref[k], list):
                                    for i in pref[k]:
                                          self.final_scores[value['name']]+=v['score']*v['func'](value[k], i.lower())
                              else:
                                    self.final_scores[value['name']]+=v['score']*v['func'](value[k], pref[k]) 
            return self.top_five_movies()
       
      

      def place_in_list(self , attr_list: str, user_input: str):
            modified_l = ast.literal_eval(attr_list)
            try:
                  return float(1/(modified_l.index(user_input)+1))
            except:
                  return 0

      def hours_minutes_to_minutes(self , time_str):
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
      
      def is_same_value(self , value: str , user_input: str):
            listed_val=[value]
            close_matches=difflib.get_close_matches(user_input, listed_val , cutoff=0.9)
            if len(close_matches)>1:
                  print (close_matches[0])
            return  1 if len(close_matches)>0 else 0

      def is_value_gt(self , value , user_input):
            return  1 if float(value)>=float(user_input) else 0

      def is_value_in_range(self, value:str , user_input:str):
            time_in_min=self.hours_minutes_to_minutes(value)
            try:
                  range = user_input.split('-')
                  return 1 if (time_in_min>= int(range[0]) and time_in_min<=int(range[1])) else 0
            except:
                  return 1 if(time_in_min>=int(user_input[:-1])) else 0


      def top_five_movies(self ):
            all_movies_sorted = dict(sorted(self.final_scores.items(), key=operator.itemgetter(1) , reverse=True))
            top_five_movies = {}
            count = 0
            for key, value in all_movies_sorted.items():
                  print(key, ':', value)
                  count += 1
                  top_five_movies[key] = value
                  if count == 5:
                        break
            return top_five_movies
      
      def get_movie_url(self , movie_name):
            row = self.df.loc[self.df['name'] == movie_name]
            return row.iloc[0, -1]







            

            
                  
      

