import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Rekomendasi Game Steam",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Memuat dan memproses dataset Steam"""
    try:
        df = pd.read_csv('steam.csv')
        df = df[['name', 'genres', 'negative_ratings', 'positive_ratings']]
        df.dropna(inplace=True)
        
        df['combined'] = (
            df['genres'] + " " +
            df['negative_ratings'].astype(str) + " " +
            df['positive_ratings'].astype(str)
        )
        
        return df
    except FileNotFoundError:
        st.error("❌ File steam.csv tidak ditemukan! Pastikan file berada di direktori yang sama dengan aplikasi ini.")
        return None

@st.cache_data
def create_recommendation_model(df):
    """Membuat model rekomendasi menggunakan TF-IDF dan cosine similarity"""
    if df is None:
        return None, None, None
    
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['combined'])
    
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['name']).drop_duplicates()
    
    return cosine_sim, indices

def recommend_games(game_title, df, cosine_sim, indices, top_n=6):
    """Fungsi untuk mendapatkan rekomendasi game berdasarkan judul game yang diberikan"""
    if df is None or cosine_sim is None or indices is None:
        return []
    
    idx = indices.get(game_title)
    if idx is None:
        return []
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
    recommendations = []
    for i, (game_idx, score) in enumerate(sim_scores):
        game_name = df.iloc[game_idx]['name']
        game_genre = df.iloc[game_idx]['genres']
        positive_ratings = df.iloc[game_idx]['positive_ratings']
        negative_ratings = df.iloc[game_idx]['negative_ratings']
        
        recommendations.append({
            'name': game_name,
            'genre': game_genre,
            'similarity_score': score,
            'positive_ratings': positive_ratings,
            'negative_ratings': negative_ratings,
            'total_ratings': positive_ratings + negative_ratings,
            'rating_ratio': positive_ratings / (positive_ratings + negative_ratings) if (positive_ratings + negative_ratings) > 0 else 0
        })
    
    return recommendations

def main():
    df = load_data()
    cosine_sim, indices = create_recommendation_model(df)

    st.title("🎮 Rekomendasi Game Steam")

    pilihan = st.selectbox("Pilih game favoritmu:", df['name'].sample(10).tolist())

    if st.button("Rekomendasikan Game Serupa"):
        hasil = recommend_games(pilihan, df, cosine_sim, indices)
        st.subheader("Game yang mungkin kamu suka:")
        for i, game in enumerate(hasil, 1):
            st.write(f"{i}. {game['name']}")

if __name__ == "__main__":
    main() 