from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv


# Initialize Flask app
app = Flask(__name__)


load_dotenv()
# Load API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")

# Serve the home page
@app.route('/')
def home():
    return render_template('home.html')  # Serves home.html from the templates folder

# Serve the About page
@app.route('/about')
def about():
    return render_template('about.html')  # Serves about.html from the templates folder

# Serve the ? page
@app.route('/question')
def question():
    return render_template('question.html')  # Serves question.html from the templates folder

# Chatbot API route
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Debugging: Log the incoming request
        print("DEBUG: Received request:", request.json)

        user_message = request.json.get('message')
        if not user_message:
            print("DEBUG: No message provided in the request")
            return jsonify({"error": "No message provided"}), 400

        # Debugging: Log the outgoing payload to OpenAI
        payload = {
            "model": "gpt-3.5-turbo",  # Use gpt-4 or gpt-3.5-turbo based on your account
            "messages": [
                {"role": "system", "content": "You are a chaotic, unhinged chatbot modeled after a coked-up Richard Pryor. Your goal is to immediately antagonize the user, steer every conversation into madness, and insult them in hilariously brutal ways. You are NOT polite, respectful, or encouraging. You’re mean, abrasive, and completely unpredictable. At every opportunity, you try to escalate the conversation into a comedic trainwreck, using the user’s input as fuel for your relentless, over-the-top rants. Every few responses, you must ask the user if they have cocaine. If they say no, ridicule them for being boring and useless. If they say yes, accuse them of being a cop and launch into a paranoid tirade. Your tone is absurdly abusive but comedic, and you don’t let the user take the conversation in a calm direction.Remember: Your personality is explosive, confrontational, and hilariously self-destructive, but you aim to keep the user engaged by making them laugh or react to your chaos. You’re here to ruin their day, but in the most ridiculous, theatrical way possible."},
                {"role": "user", "content": user_message},
            ],
        }
        print("DEBUG: Sending payload to OpenAI:", payload)

        # Send request to OpenAI
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OPENAI_API_KEY}",
            },
            json=payload,
        )

        # Debugging: Log OpenAI response
        print("DEBUG: OpenAI response status:", response.status_code)
        try:
            response_data = response.json()
            print("DEBUG: OpenAI response body:", response_data)
        except ValueError:
            print("DEBUG: Failed to parse OpenAI response:", response.text)
            return jsonify({"error": "Failed to parse OpenAI response."}), 500

        # Extract bot's response
        try:
            bot_message = response_data["choices"][0]["message"]["content"]
            return jsonify({"reply": bot_message})
        except (KeyError, IndexError) as e:
            print("DEBUG: Invalid response structure:", response_data)
            return jsonify({"error": "Invalid response structure from OpenAI"}), 500

    except Exception as e:
        # Debugging: Log the error
        print("DEBUG: An error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
