from flask import Flask, request, jsonify, render_template, flash
import os
import pandas as pd
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize AI helpers
ai_helpers = {}

# Initialize Gemini
try:
    from utils.models.gemini import GeminiHelper
    if os.getenv("GEMINI_API_KEY"):
        ai_helpers["gemini"] = GeminiHelper(api_key=os.getenv("GEMINI_API_KEY"))
        print("Gemini initialized successfully")
    else:
        print("Gemini API key missing")
except Exception as e:
    print(f"Error initializing Gemini: {e}")

# Initialize Mistral
try:
    from utils.models.mistral import MistralModel
    if os.getenv("MISTRAL_API_KEY"):
        ai_helpers["mistral"] = MistralModel(api_key=os.getenv("MISTRAL_API_KEY"))
        print("Mistral initialized successfully")
    else:
        print("Mistral API key missing")
except Exception as e:
    print(f"Error initializing Mistral: {e}")

# Global variable to store the current dataframe
current_df = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global current_df
    
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "No file uploaded."})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "error": "No file selected."})
    
    if not file.filename.endswith(('.csv', '.xlsx')):
        return jsonify({"success": False, "error": "Invalid file type. Please upload CSV or Excel file."})
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Read the file
        if filename.endswith('.csv'):
            current_df = pd.read_csv(file_path)
        else:
            current_df = pd.read_excel(file_path)
        
        # Generate preview
        preview_html = current_df.head().to_html(classes='table table-striped', index=False)
        
        return jsonify({
            "success": True,
            "message": "File uploaded successfully.",
            "preview": preview_html
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    global current_df
    
    if current_df is None:
        return jsonify({"success": False, "error": "Please upload a file first."})
    
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "No data provided."})
        
        message = data.get('message')
        model = data.get('model', 'gemini').lower()
        temperature = float(data.get('temperature', 0.7))
        max_tokens = int(data.get('maxTokens', 200))
        
        if not message:
            return jsonify({"success": False, "error": "No message provided."})
        
        if model not in ai_helpers:
            available_models = list(ai_helpers.keys())
            return jsonify({
                "success": False, 
                "error": f"Model {model} not available. Available models: {available_models}"
            })
        
        # Get response from AI model
        response = ai_helpers[model].chat_with_data(
            current_df,
            message,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return jsonify({
            "success": True,
            "response": response,
            "model": model
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")  # Debug print
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    if not ai_helpers:
        print("Warning: No AI models were initialized. Check your API keys in .env file.")
    app.run(debug=True)