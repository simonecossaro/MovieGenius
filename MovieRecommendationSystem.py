import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from tqdm import tqdm
from Levenshtein import distance

dataset_movies = pd.read_csv('movies_dataset_overview.csv')
# the dataset is the one obtained after preprocessing
# for more info: https://colab.research.google.com/drive/1chPt-SJ3CT5nDLnHFXfZ3LpymwuLsF5t#scrollTo=UiTzcNm5zUvd

###########################################################
# recommends movies similar to film_target

def recommendMovies(dataset, film_target, amount=1):
        distance = []
        # movie = i valori della riga del film
        movie = dataset[(dataset.title.str.lower() == film_target.lower())].head(1).values[0]
        # rec = il dataset a cui viene tolta la riga del film indicato
        rec = dataset[dataset.title.str.lower() != film_target.lower()]
        for film in tqdm(rec.values):
            d = 0
            for col in range(len(rec.columns)):
                if not col in [19]:
                    d = d + np.absolute(float(movie[col]) - float(film[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['title']
        return rec[columns][:amount]

###########################################################
# filters for the MoodRecommendation() function

def onlyMoodMovies(df,mood):
        if (mood == 'laugh'):
                df1 = df[df.Comedy == 1]
                df1 = df1[df1.Animation != 1]
                df1 = df1[df1.Fantasy != 1]
                df1 = df1[df1.Action != 1]
                df1 = df1[df1.Drama != 1]
                df1 = df1[df1.ScienceFiction!= 1]
                return df1
        if (mood == 'cry'):
                df1 = df[df.Drama == 1]
                df1 = df1[df1.Animation != 1]
                df1 = df1[df1.Fantasy != 1]
                df1 = df1[df1.Action != 1]
                df1 = df1[df1.ScienceFiction!= 1]
                df1 = df1[df1.Horror != 1]
                return df1
        if (mood == 'love'):
                df1 = df[df.Romance == 1]
                df1 = df1[df1.Animation != 1]
                df1 = df1[df1.Fantasy != 1]
                df1 = df1[df1.ScienceFiction!= 1]
                return df1
        if (mood == 'adrenaline'):
                return df[df.Thriller == 1]
        if (mood == 'fear'):
                return df[df.Horror == 1]
        if (mood == 'fantasy'):
                return df[df.Fantasy == 1]
        if (mood == 'science fiction'):
                df1 = df[df.ScienceFiction == 1]
                df1 = df1[df1.Fantasy != 1]
                df1 = df1[df1.Action != 1]
                return df1
        if (mood == 'adventure'):
                df1 = df[df.Adventure == 1]
                df1 = df1[df1.Animation != 1]
                df1 = df1[df1.Fantasy != 1]
                df1 = df1[df1.ScienceFiction!= 1]
                return df1
        if (mood == 'casual'):
                return df
        return df

###########################################################
# recommends movies based on mood

def MoodRecommendation(dataset, mood, amount=1):
        rec = onlyMoodMovies(dataset,mood)
        rec = rec.sort_values('revenue',ascending=False)
        columns = ['title']
        return rec[columns][:amount]
    
###########################################################    
# mood filter  

def selectMovies(df, mood):
        if (mood == 'laugh'):
                df1 = df[df.Comedy == 1]
                df1 = df1[df1.Drama != 1]
                return df1
        if (mood == 'cry'):
                return df[df.Drama == 1]
        if (mood == 'love'):
                return df[df.Romance == 1]
        if (mood == 'adrenaline'):
                return df[df.Thriller == 1]
        if (mood == 'fear'):
                return df[df.Horror == 1]
        if (mood == 'fantasy'):
                return df[df.Fantasy == 1]
        if (mood == 'science fiction'):
                return df[df.ScienceFiction == 1]
        if (mood == 'adventure'):
                return df[df.Adventure == 1]
        if (mood == 'casual'):
                return df
        return df

###########################################################
# function to know if a movie is present or not after the cuts to the dataset

def ispresent(lista, film):
        for x in lista:
                if (x.lower() == film.lower()):
                        return True
        return False

###########################################################

class MovieRecommendationSystem():
        def __init__(self):
                self.dataset = dataset_movies
                self.dataset = self.dataset.iloc[:,1:-1]
        def recommend(self,for_kids,mood,film_target,Tmax):
                if (not(film_target == '')):
                        movie = pd.Series(self.dataset[(self.dataset.original_title.str.lower() == film_target.lower())].head(1).values[0], index = self.dataset.columns )  
                d1 = self.dataset.iloc[:,1:]
                # verifico for_kids
                if (for_kids): # filtro for_kids
                        d1 = d1[d1.Animation == 1]
                        self.dataset = self.dataset[self.dataset.Animation == 1]
                else:# filtro mood
                        d1 = selectMovies(d1,mood)
                        self.dataset = selectMovies(self.dataset,mood)
                # rimuovo film con durata maggiore di tmax
                d1 = d1[d1.runtime <= Tmax]
                self.dataset = self.dataset[self.dataset.runtime <= Tmax]
                # se film_target non inserito consiglio in base al mood
                if (film_target == ''):
                        titoli = self.dataset.iloc[:,0].values
                        d1["title"] = titoli
                        recommendations = MoodRecommendation(d1,mood,10)
                        return recommendations
                # se film_target inserito
                # se non è presente dopo i tagli riaggiungo il film preferito
                elif(not ispresent(self.dataset['original_title'],film_target)):
                        d1.loc[len(d1)] = movie[1:19]
                        self.dataset.loc[len(self.dataset)] = movie
                # normalizzazione dei dati
                sc = StandardScaler() 
                sc.fit(d1) 
                d1_std = sc.transform(d1)
                # riporto il dataset nel formato DataFrame
                d2 = pd.DataFrame(d1_std)
                d2.columns = d1.columns
                # aggiungo i titoli dei film
                titoli = self.dataset['original_title'].values
                d2["title"] = titoli
        
                recommendations = recommendMovies(d2,film_target,10)
   
                return recommendations
