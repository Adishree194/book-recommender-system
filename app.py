import pickle
import numpy as np
import streamlit as st

st.header("Book Recommender System")

# Load the model and data
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion[0]:  # Access the first element of the suggestion array
        book_name.append(book_pivot.index[book_id])

    for name in book_name:
        ids = np.where(final_rating['title'] == name)[0]
        if ids.size > 0:  # Check if ids is not empty
            ids_index.append(ids[0])

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recommend_books(book_name):
    book_list = []
    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

        poster_url = fetch_poster(suggestion)

        for i in range(len(suggestion[0])):  # Access the first element of the suggestion array
            books = book_pivot.index[suggestion[0][i]]
            book_list.append(books)

        return book_list, poster_url
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return None, None

selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    books_name
)

if st.button('Show Recommendations'):
    recommendation_books, poster_url = recommend_books(selected_books)
    if recommendation_books and poster_url:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommendation_books[1])
            st.image(poster_url[1])
        with col2:
            st.text(recommendation_books[2])
            st.image(poster_url[2])
        with col3:
            st.text(recommendation_books[3])
            st.image(poster_url[3])
        with col4:
            st.text(recommendation_books[4])
            st.image(poster_url[4])
        with col5:
            st.text(recommendation_books[5])
            st.image(poster_url[5])
    else:
        st.warning("No recommendations found.")
