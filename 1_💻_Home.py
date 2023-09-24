import pickle
import streamlit as st
import numpy as np
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="BookFriend", page_icon=":desktop_computer:", layout="wide")
st.title("📝Main page")
st.sidebar.markdown(
    """
    <style>
        .css-145kmo2 .stMarkdown {
            background-color: #818589 !important; /* Change the background color */
        }
        .css-145kmo2 .stMarkdown p {
            color: #000000 !important; /* Change the text color */
        }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown('<div class="css-145kmo2"><p>Select a page above.</p></div>', unsafe_allow_html=True)


st.header('📚Book Recommender System Using Machine Learning')
model = pickle.load(open('pickle_files/model.pkl','rb'))
book_names = pickle.load(open('pickle_files/book_names.pkl','rb'))
final_rating = pickle.load(open('pickle_files/final_rating.pkl','rb'))
book_pivot = pickle.load(open('pickle_files/book_pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load assests
lottie_coding = load_lottieurl("https://lottie.host/d30724ea-df80-4786-a248-afab9c3f1100/bd0bFCM9Wg.json")
    
#---About Us----
with st.container():
         st.write("----------")
         left_column, right_column = st.columns(2)
         with left_column:
            st.header("About Us")
            st.write("##")
            st.write(
                """
                Welcome to BookFriend, your literary haven in the digital world! We're more than just a book recommendation website; we're passionate bookworms on a mission to ignite your love for reading.

                """
            )
            st.subheader("Our Mission")
            st.write("----------")
            st.write("At BookFriend, our mission is to make your reading experience as exhilarating as turning the first page of a new book. We're here to guide you through the vast literary landscape, helping you unearth hidden gems, explore new genres, and reconnect with timeless classics. Our team of dedicated book enthusiasts scours the literary world to curate personalized book recommendations that match your unique tastes and preferences."
            )
         with right_column:
            st_lottie(lottie_coding, height=400, key="Book_Reading")