#########################
## OpenAI in Streamlit ##
#########################

# Importing Libraries
import streamlit as st
from openai import OpenAI
import os

# Setting up OpenAI


# key = add actual key here

client = OpenAI(api_key=key)

# Streamlit App

st.title('🎵 OpenAI Music Assistant 🎶')

st.write('Generate unique song lyrics with a specific genre, artist, and mood!')

# Sidebar Inputs
st.sidebar.header("Customize Your Song")
genre = st.sidebar.selectbox(
    '🎼 Select a genre:', 
    ['pop', 'rock', 'rap', 'country', 'jazz', 'metal', 'blues', 'folk', 'classical', 'reggae']
)

artist = st.sidebar.text_input('🎤 Enter an artist:', 'Sabrina Carpenter')

mood = st.sidebar.selectbox(
    '💭 Select a mood:',
    ['happy', 'sad', 'romantic', 'inspirational', 'melancholic', 'energetic']
)

title_placeholder = st.empty()

lyrics = st.empty()

# Generate Lyrics
if st.sidebar.button('🎵 Generate Lyrics'):
    with st.spinner("Crafting your song... 🎼"):
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a lyrical genius."},
                {
                    "role": "user",
                    "content": f"Write a song lyric in the {genre} genre by {artist} with a {mood} mood."
                }
            ]
        )
    generated_lyrics = completion.choices[0].message.content
    title_placeholder.markdown(f"### 🎶 **Generated Lyrics by {artist}** 🎶")
    lyrics.write(generated_lyrics)

    # Generate Song Title
    title_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative title generator for songs."},
            {
                "role": "user",
                "content": f"Suggest a {mood} title for a {genre} song by {artist}."
            }
        ]
    )
    song_title = title_completion.choices[0].message.content
    st.subheader(f"🎵 Song Title: {song_title}")

    # Save Lyrics Option
    if st.button('💾 Save Lyrics'):
        with open('lyrics.txt', 'w') as f:
            f.write(f"Song Title: {song_title}\n\n{generated_lyrics}")
        st.success("Lyrics saved to lyrics.txt!")
