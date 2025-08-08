import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash-001')

def generate_story_plot(genre, characters, theme):
    prompt = f"""
    Create an original and creative short story plot with:
    - Genre: {genre}
    - Main Characters: {characters}
    - Theme/Setting: {theme}
    Include a title and plot summary in under 250 words.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating story: {str(e)}"
