import streamlit as st
import pandas as pd
import numpy as np
import requests

def get_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c6270a5a158f59550fc8983e457d045d&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" +data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = simty[movie_index]
    list_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in list_movies:
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_poster.append(movies.iloc[i[0]]['id'])
    return recommended_movies, recommended_movies_poster
st.title("Movie recommender system")
movies = pd.read_csv('movies.csv')
simty = pd.read_csv('final.csv')
simty = simty.to_numpy()
selected_movie_name = st.selectbox(
'Select a Movie',
movies['title'].values)
if st.button('Recommend'):
    mv, pst = recommend(selected_movie_name)
    list1=[]
    for i in pst :

        list1.append(get_poster(i))
    str1 = ['col1', 'col2', 'col3', 'col4' , 'col5', 'col6', 'col7', 'col8', 'col9', 'col10' ]
    st.image(list1, caption = mv, width = 150 )

