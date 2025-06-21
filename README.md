# Food Item Recognition FastAPI Server

Welcome to the **Food Item Recognition FastAPI Server**!  
This project combines deep learning and modern web technology to provide an interactive experience where users can identify food items they are holding in real time through their browser.

---

## 🚀 Features

- **Deep Learning Model**: Utilizes a Convolutional Neural Network (CNN) to recognize food items from images.
- **FastAPI Backend**: High-performance, easy-to-use API server.
- **Interactive Web Interface**: Users can grant camera access, capture a photo, and see instant recognition results.
- **Data Persistence**: Stores each recognition event (image, metadata, prediction) in an AWS-hosted PostgreSQL database.
- **Real-Time Feedback**: Instant prediction results shown on the web page.

---

## 🌐 How it Works

1. **User Experience**
    - Visit the web app's main page.
    - Grant camera access when prompted.
    - Hold a food item in your hand and click the capture button.
    - The image is sent to the FastAPI backend for processing.

2. **Backend Processing**
    - The backend receives the image.
    - The CNN model analyzes the image and predicts the food item.
    - Raw image data, filename, file mime type, timestamp, and prediction label are saved in the AWS PostgreSQL database.
    - The prediction is sent back to the web page and displayed for the user.

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/) (AWS-hosted or local)
- [Jupyter Notebook](https://jupyter.org/) (for model development)
- [HTML/CSS/JS](for frontend)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/anegouni-bhanuprasad-goud/Food_Item_Recognition_Fastapi_Server.git
    cd Food_Item_Recognition_Fastapi_Server
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Database**
    - Set your PostgreSQL connection parameters in your environment or a `.env` file as described in the documentation.

5. **Run the Server**
    ```bash
    uvicorn app:app --reload
    ```

6. **Access the Web Interface**
    - Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📸 User Guide

1. Go to the main page.
2. Allow camera access.
3. Position your hand holding a food item in front of the camera.
4. Click the **Capture** button.
5. Wait a moment for the prediction result to appear below the camera view!

---

## 🧑‍💻 Project Structure

- `app.py` or `main.py`: FastAPI backend with endpoints.
- `templates/index.html`: Main web interface.
- `static/`: JavaScript and CSS resources.
- `model/`: Jupyter Notebooks and model files for CNN training.
- `database/`: Scripts for PostgreSQL integration.

---

## 📝 Example API Usage

You can also interact with the API directly (e.g., using `curl` or Postman):

```bash
curl -X POST "http://localhost:8000/predict/" \
    -F "file=@your_image.jpg"
```

---

## 📂 Data Saved

Each prediction event stores:

- **Image** (raw data)
- **Filename**
- **File MIME type**
- **Date and Time**
- **Prediction Label**

All this information is securely stored in the AWS PostgreSQL database.

---

## 🤝 Contributing

Your contributions are welcome!  
1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request with a clear description.

---

## 📣 Feedback

- Found a bug? Have a suggestion? Please open an [issue](https://github.com/anegouni-bhanuprasad-goud/Food_Item_Recognition_Fastapi_Server/issues).
- For questions, feel free to contact the maintainer.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

**Enjoy recognizing your food items effortlessly!**
