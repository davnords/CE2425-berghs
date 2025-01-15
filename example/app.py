from flask import Flask, render_template, jsonify, request
from openai import OpenAI

# REPLACE WITH YOUR OPENAI API KEY
OPEN_AI_API_KEY = ''
client = OpenAI(api_key=OPEN_AI_API_KEY)

app = Flask(__name__)

# MAIN CODE FOR RENDERING LANDING PAGE
@app.route('/')
def home(): 
    return render_template('index.html')

# EXAMPLE CODE FOR CALLING OPENAI API
@app.route('/api/image')
def image():
    response = client.images.generate(
        model="dall-e-3",
        prompt="Big blue marlin in the ocean!",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})