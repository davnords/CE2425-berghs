from flask import Flask, render_template, jsonify, request
from openai import OpenAI

# REPLACE WITH YOUR OPENAI API KEY
client = OpenAI(api_key=OPEN_AI_API_KEY)

app = Flask(__name__)

# MAIN CODE FOR RENDERING LANDING PAGE
@app.route('/')
def home(): 
    return render_template('index.html')

# EXAMPLE CODE FOR CALLING OPENAI API
@app.route('/api/answer', methods=['GET'])
def answer():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a love doctor"},
            {
                "role": "user",
                "content": "Give me one short love or heartbreak prediction phrase everytime and alternate randomly between love and heartbreak. Only one phrase"
            }
        ]
    )
    print(completion.choices[0].message)

    return jsonify({'text': completion.choices[0].message.content})

    