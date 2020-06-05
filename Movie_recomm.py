import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.title("Simple Movie Recommendation System")
data = pd.read_csv('data//movie_dataset.csv')

def get_title_from_index(index):
    return data[data.index == index]['title'].values[0]

def get_title_from_title(title):
    return data[data.title == title]['index'].values[0]


features = ['keywords','cast','genres','director']

for f in features:
    data[f] = data[f].fillna("")

def combine_feat(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']

data['combined_feats'] = data.apply(combine_feat,axis = 1)

cv = CountVectorizer()

count_matrix = cv.fit_transform(data['combined_feats'])

cosine_sim = cosine_similarity(count_matrix)

movie_user_likes = st.selectbox("Choose a Movie that you like",data['title'])

movie_index = get_title_from_title(movie_user_likes)

similar_movies =  list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1],reverse =True)

val = st.selectbox("Number of Recommendation",[x for x in range(1,11)])

i=0
if st.button("Suggestion"):
    for movie in sorted_similar_movies:
        if i == 0 :
            i+=1
        else:
            st.write(get_title_from_index(movie[0]))
            i+=1
            if i == val+1:
                break
