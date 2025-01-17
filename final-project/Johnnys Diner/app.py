from flask import Flask, render_template, jsonify
from openai import OpenAI
import os

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1",
    http_client=None  # This prevents the proxy initialization that's causing the error
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat')
def chat():
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are the arm from Twin Peaks. Respond in cryptic, surreal messages that reference the Black Lodge, but always include a haiku somewhere in your response. Keep responses brief and mysterious."},
                {"role": "user", "content": "Tell me about the Black Lodge"}
            ]
        )
        return jsonify({'message': completion.choices[0].message.content})
    except Exception as e:
        return jsonify({'message': f"The arm cannot speak: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)