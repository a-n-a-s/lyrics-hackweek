
# Taylor Swift Lyrics Explorer 🎤

A Streamlit web application that fetches Taylor Swift song lyrics and generates stylized word clouds.

![Demo Screenshot](./song.jpg)

## Features
- 🔍 Search any Taylor Swift song lyrics
- ☁️ Generate colorful word clouds with custom shape masking
- 🎨 Bright color scheme (pink, orange, blue, red)
- ✨ Lyrics cleaning and formatting

## Installation
1. Clone the repository
2. Install requirements:
```bash
pip install -r requirements.txt
 ```


## Configuration
1. Get a Genius API client access token from https://genius.com/api-clients
2. Replace the Genius client token in main.py :
```python
genius = lyricsgenius.Genius('YOUR_TOKEN_HERE')
 ```


## Usage
Run the application with:

```bash
streamlit run main.py
 ```

The app will:

1. Show a text input for song titles (default: "Love Story")
2. Display cleaned lyrics in a scrollable box
3. Generate a word cloud shaped like a music note (using song.jpg as mask)
4. Show interactive Streamlit components
## Dependencies
- Streamlit - Web interface
- LyricsGenius - API access for lyrics
- WordCloud - Word cloud generation
- Matplotlib - Visualization
- Pillow - Image processing
- NumPy - Array operations