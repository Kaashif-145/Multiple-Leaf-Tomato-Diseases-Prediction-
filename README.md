# 🍅 Tomato Disease Detection & Classification System

A comprehensive deep learning-based application designed to identify diseases in tomato plants using leaf image analysis. This system helps farmers and gardeners quickly diagnose plant health issues and provides actionable treatment advice, including pesticide recommendations and severity levels.

---

## 🌟 Key Features

*   **Disease Identification**: Recognizes 9 specific tomato diseases and distinguishes them from healthy leaves.
*   **Deep Learning Models**: Utilizes state-of-the-art architectures including NASNetMobile (default), DenseNet121, EfficientNetB0, and EfficientNetV2S.
*   **Treatment Recommendations**: Provides suggested pesticides for each identified disease.
*   **Severity Assessment**: Indicates the urgency of the infection (Low, Medium, High, Very High).
*   **User-Friendly Web Interface**: Simple upload-and-detect workflow built with Flask.

---

## 🦠 Supported Disease Classes

The model is trained to detect the following:
1.  **Bacterial Spot**
2.  **Early Blight**
3.  **Late Blight**
4.  **Leaf Mold**
5.  **Septoria Leaf Spot**
6.  **Spider Mites** (Two-spotted spider mite)
7.  **Target Spot**
8.  **Yellow Curl Virus**
9.  **Mosaic Virus**
10. **Healthy**

---

## 🛠️ Technology Stack

*   **Backend**: Flask (Python)
*   **Deep Learning**: TensorFlow / Keras
*   **Image Processing**: OpenCV, PIL, NumPy
*   **Frontend**: HTML5, CSS3 (Google Fonts - Nunito)
*   **Environment**: Python 3.10

---

## 📂 Project Structure

```text
WORK/
├── app.py                      # Main Flask application
├── chatbot.py                  # Experimental AI chatbot script
├── nasnetmobile_plant_model.h5 # Pre-trained model (NASNetMobile)
├── templates/                  # Web interface templates (index.html, results.html)
├── uploads/                    # Directory for uploaded images
├── train/                      # Training dataset
├── valid/                      # Validation dataset
├── test/                       # Testing dataset
├── train_models.ipynb          # Notebook for model training & evaluation
└── tf310_env/                  # Python virtual environment
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed. It is recommended to use the provided virtual environment or create a new one.

### 2. Installation
Clone the repository and install dependencies using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

---

## 📊 Model Performance
The project includes a training notebook (`train_models.ipynb`) where multiple models were compared. While NASNetMobile is used for the production app, other models like **EfficientNetV2S** and **DenseNet121** are also available in the repository for experimentation.

---

## 🤖 AI Chatbot (Experimental)
The repository also contains a `chatbot.py` script that uses OpenAI's GPT-3.5 and web scraping to provide additional gardening and agricultural advice based on specific website content.

---

## 📜 License
This project is for educational and research purposes.
