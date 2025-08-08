# Gen-AI Story Writing Assistant

A web application built with Python (Flask) and powered by Google's Gemini API to collaboratively write creative stories. Users can select a genre, provide an initial prompt, and let the AI generate compelling continuations.



***

## ## Live Application

**You can access a live deployed demo here:**
[**➡️ Live Story Writing App**](https://your-live-app-url.com)  ***

## ## Features

* **Interactive Story Generation**: Continuously build a story by feeding AI-generated text back as the new prompt.
* **Genre Selection**: Tailor the story's tone by choosing from genres like Fantasy, Sci-Fi, Mystery, and more.
* **Custom Prompts**: Guide the narrative with your own creative starting points.
* **Simple Web Interface**: A clean and intuitive UI built with Flask and standard web technologies.
* **Powered by Gemini**: Leverages the advanced reasoning and text generation capabilities of Google's Gemini Pro model.

***

## ## Tech Stack

* **Backend**: Flask
* **AI Model**: Google Gemini Pro
* **Frontend**: HTML, CSS, JavaScript (Fetch API)

***

## ## Getting Started

To run this project on your local machine, follow these steps.

### ### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### ### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chaitanyananepallicn/Gen-AI-Story-Writing.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd Gen-AI-Story-Writing
    ```

3.  **Create and activate a virtual environment (Recommended):**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your environment variables:**
    * Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Create a file named `.env` in the root project directory.
    * Add your API key to the `.env` file:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

6.  **Run the Flask application:**
    ```bash
    flask run
    ```
    * After running the command, open your web browser and navigate to the local URL provided (usually `http://127.0.0.1:5000`).
