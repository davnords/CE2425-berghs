from flask import Flask, render_template, jsonify, request
from openai import OpenAI

from openai import OpenAI


client = OpenAI(api_key=OPEN_AI_API_KEY)

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/api/image')
def image():
    response = client.images.generate(
        model="dall-e-3",
        prompt="Generate carzy looking patterns in black and white.", 
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = (response.data[0].url)
    return jsonify({'image_url': image_url})



@app.route('/api/chat')
def chat():

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            },
            {"role": "assistant",
             "content": "in the world of code, Python is the best to learn. it is so simple." 



            }
        ]
    )
    return jsonify({'message': completion.choices[0].message.content})



