import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random


st.set_page_config(page_title="Taylor Swift Lyrics Explorer", page_icon="🎤")
st.title("🎤 Taylor Swift Lyrics Explorer")
st.write("Enter a Taylor Swift song title to view the lyrics and generate a word cloud!")

#genius client
genius = lyricsgenius.Genius('ekVYxXWNX4vYxiDv0FEKjTFNnZgweVZZNVmzmBWeqyI2ScSoOOfQDGse4hE0dH1j')
genius.verbose = False  
genius.remove_section_headers = True 


def clean_lyrics(lyrics):
    lyrics = re.sub(r'^.*?Read More', '', lyrics, flags=re.IGNORECASE | re.DOTALL)
    lyrics = re.sub(r'(\w+) Lyrics', '', lyrics, flags=re.IGNORECASE)
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    lyrics = '\n'.join(line.strip() for line in lyrics.split('\n') if line.strip())
    return lyrics


def get_lyrics(song_title):
    try:
        song = genius.search_song(song_title, "Taylor Swift")
        if song:
            print(song.lyrics) 
            return clean_lyrics(song.lyrics)
        return None
    except Exception as e:
        st.error(f"Couldnot find the song: {e}")
        return None

#
def generate_wordcloud(text):
    if not text:
        return None
    
    
    custom_colors = ['#FF69B4', '#FFA500', '#00BFFF', '#FF0000'] 
    
    
    def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return random.choice(custom_colors)
    
    masked_image_path = "./song.jpg"
    background_image = np.array(Image.open(masked_image_path))
    # plt.imshow(background_image)



    word_cloud = WordCloud(mask=background_image,background_color="white", max_words=1000,  contour_width=3, contour_color='#FF69B4' , width=800, height=400 , color_func=custom_color_func).generate(text)
    

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(word_cloud, interpolation='bilinear')
    ax.axis('off')
    return fig

# User input
song_title = st.text_input("Enter a Taylor Swift song title:", "Love Story")

if st.button("Get Lyrics"):
    with st.spinner(f"Fetching lyrics for '{song_title}'..."):
        lyrics = get_lyrics(song_title)
        
        if lyrics:
   
            st.subheader(f"Lyrics for '{song_title}'")
            st.text_area("", lyrics, height=300)
            

            st.subheader("Word Cloud")
            wordcloud_fig = generate_wordcloud(lyrics)
            if wordcloud_fig:
                st.pyplot(wordcloud_fig)
            else:
                st.warning("Couldn't generate word cloud.")
        else:
            st.error(f"Couldn't find lyrics for '{song_title}'. Please check the song title and try again.")

# Add some styling
st.markdown("""
<style>
    .stTextArea [data-baseweb=base-input] {
    }
    .css-1aumxhk {
        background-color: #f0f2f6;
        border: 1px solid #d6d6d6;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)
