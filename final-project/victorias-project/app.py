from flask import Flask, render_template, jsonify, request
from openai import OpenAI
from create_user import create_user

# REPLACE WITH YOUR OPENAI API KEY

client = OpenAI(api_key=OPEN_AI_API_KEY)

app = Flask(__name__)

# MAIN CODE FOR RENDERING LANDING PAGE
@app.route('/')
def home(): 
    return render_template('index.html')

# EXAMPLE CODE FOR CALLING OPENAI API
@app.route('/api/chat')
def chat():

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a poem about learning programming"
            },
            {
                "role": "assistant", 
                "content": "In the world of code, Python is thebest to learn. It is so simple."
            }
        ]
    )
    return jsonify({'message': completion.choices[0].message.content})


@app.route('/api/image')
def image():
    response = client.images.generate(
        model="dall-e-3",
        prompt="A weather broadcaster that provides essential information about daily forecasts",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})

@app.route('/api/user/create', methods=['POST'])
def create_user_route():
    data = request.json
    name = data['name']
    email = data['email']
    create_user(name, email)
    return jsonify({'message': 'User created successfully!'})