from flask import Flask, render_template, jsonify
from openai import OpenAI

Open_AI_API_Key = ""
client = OpenAI(api_key=Open_AI_API_Key)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat')
def chat():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about Twin Peaks, the David Lynch show."
            }
        ]
    )
    return jsonify({'message': completion.choices[0].message.content})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)