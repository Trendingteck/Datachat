### **DataChat - README**  

Welcome to **DataChat**, a powerful AI-powered application that allows you to **chat with your data** using state-of-the-art AI models like **Google Gemini** and **Mistral AI**. This application is designed to make data analysis intuitive, interactive, and accessible to everyone.  

---

## **Table of Contents**  
1. [Features](#features)  
2. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Running the App](#running-the-app)  
3. [Usage](#usage)  
   - [Uploading Data](#uploading-data)  
   - [Chatting with Data](#chatting-with-data)  
   - [Model Configuration](#model-configuration)  
4. [File Structure](#file-structure)  
5. [Technologies Used](#technologies-used)  
6. [Contributing](#contributing)  
7. [License](#license)  

---

## **Features**  
- **Upload Excel/CSV Files:** Easily upload your data files for analysis.  
- **AI-Powered Data Analysis:** Chat with your data using **Google Gemini** or **Mistral AI**.  
- **Interactive Chat Interface:** Ask questions and get instant responses.  
- **Data Preview:** View a preview of your uploaded data.  
- **Model Configuration:** Adjust AI model settings like **temperature** and **max tokens**.  
- **Modern UI:** A clean, responsive, and intuitive user interface built with **Bootstrap 5**.  

---

## **Getting Started**  

### **Prerequisites**  
Before running the app, ensure you have the following installed:  
- **Python 3.9+**  
- **Pip** (Python package manager)  
- **Node.js** (optional, for frontend development)  

### **Installation**  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-username/DataChat.git
   cd DataChat
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**  
   Create a `.env` file in the root directory and add your API keys:  
   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key
   MISTRAL_API_KEY=your_mistral_api_key
   ```

### **Running the App**  
1. **Start the Flask Backend:**  
   ```bash
   python main.py
   ```

2. **Open the App in Your Browser:**  
   Visit `http://127.0.0.1:5000` to access the app.  

---

## **Usage**  

### **Uploading Data**  
1. Click the **Upload** button and select an Excel or CSV file.  
2. Once uploaded, the app will display a preview of your data.  

### **Chatting with Data**  
1. Type your question in the chat input box (e.g., "What are the top 5 rows?").  
2. The AI model will analyze your data and provide a response.  

### **Model Configuration**  
1. Select an AI model from the dropdown (Gemini or Mistral).  
2. Adjust the **temperature** and **max tokens** settings to control the AI's creativity and response length.  

---

## **File Structure**  
```plaintext
DataChat/
├── backend/
│   ├── app.py                  # Flask backend
│   ├── utils/
│   │   ├── models/             # AI models (Gemini, Mistral)
│   │   ├── data_processor.py   # File processing
│   │   ├── data_cleaner.py     # Data cleaning
│   │   └── prompt_suggestions.py
├── frontend/
│   ├── index.html              # Main HTML file
│   ├── styles.css              # Custom CSS
│   ├── script.js               # Custom JavaScript
│   ├── assets/                 # Images, icons, etc.
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── README.md                   # This file
```

---

## **Technologies Used**  
- **Backend:**  
  - Flask (Python web framework)  
  - Pandas (data processing)  
  - Google Gemini API  
  - Mistral AI API  

- **Frontend:**  
  - HTML5, CSS3, JavaScript  
  - Bootstrap 5 (UI framework)  

- **Other Tools:**  
  - Dotenv (environment variable management)  
  - Werkzeug (file upload handling)  

---

## **Contributing**  
We welcome contributions! Here’s how you can help:  
1. **Fork the Repository:** Create your own fork of the project.  
2. **Create a Branch:** Make your changes in a new branch.  
3. **Submit a Pull Request:** Open a PR with a detailed description of your changes.  

---

## **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## **Acknowledgments**  
- **Google Gemini** and **Mistral AI** for their powerful language models.  
- **Bootstrap** for the beautiful and responsive UI components.  
- **Flask** for making backend development simple and efficient.  

---

## **Contact**  
For questions or feedback, feel free to reach out:  
- **Email:** your-email@example.com  
- **GitHub:** [your-username](https://github.com/your-username)  

---

Enjoy chatting with your data! 🚀