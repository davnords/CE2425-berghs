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
@app.route('/api/fortune', methods=['GET'])
def fortune():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a tarot reader."},
            {
                "role": "user",
                "content": "Give me a mystical phrase for good luck."
            }
        ]
    )
    print(completion.choices[0].message)

    return jsonify({'text': completion.choices[0].message.content})