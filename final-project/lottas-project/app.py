from flask import Flask, jsonify, render_template
import openai
import os

# Initialize the Flask application and specify the location of the static folder
app = Flask(__name__, static_folder='static')

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("Error: OPENAI_API_KEY is not set!")
else:
    print("OPENAI_API_KEY found and set.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/image', methods=['GET'])
def generate_image():
    try:
        response = openai.Image.create(
            prompt="Space filled with galaxies and stars",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




