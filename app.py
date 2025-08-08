from flask import Flask, render_template, request, jsonify
from story_utils import generate_story_plot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    genre = data.get('genre', '')
    characters = data.get('characters', '')
    theme = data.get('theme', '')

    plot = generate_story_plot(genre, characters, theme)
    return jsonify({'plot': plot})

if __name__ == '__main__':
    app.run(debug=True)
