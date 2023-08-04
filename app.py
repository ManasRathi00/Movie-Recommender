import streamlit as st
import pickle
import pandas as pd
import requests


st.title('Movie Recommender System')
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)

    return  recommended_movies


selected_movie = st.selectbox('Which base movie?',movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
    