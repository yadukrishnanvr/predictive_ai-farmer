# 🌱 Predictive AI Farmer

An AI-powered crop recommendation system that helps farmers identify the most suitable crop based on soil and environmental conditions. The project leverages Machine Learning to analyze agricultural parameters and provide accurate crop recommendations, enabling better farming decisions and improved productivity.

---

## 📖 Overview

Agriculture is highly dependent on soil quality and climatic conditions. Choosing the wrong crop can result in poor yields and financial losses. Predictive AI Farmer uses Machine Learning to recommend the best crop based on user-provided soil and environmental parameters.

The system is designed to assist farmers, researchers, and agricultural professionals by providing quick and data-driven crop recommendations.

---

## ✨ Features

* 🌾 Crop recommendation using Machine Learning
* 📊 Predicts the most suitable crop for cultivation
* 🌱 Uses soil nutrient values (N, P, K)
* 🌡️ Considers environmental parameters such as:

  * Temperature
  * Humidity
  * pH
  * Rainfall
* 💻 Simple and user-friendly interface
* ⚡ Fast prediction using a trained ML model

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Framework

* Flask

### Frontend

* HTML
* CSS
* Bootstrap

---

## 📂 Project Structure

```
predictive_ai-farmer/
│
├── static/
├── templates/
├── dataset/
├── model.pkl
├── minmaxscaler.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 📥 Input Parameters

The model takes the following inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

---

## 📤 Output

The application predicts the most suitable crop for the given agricultural conditions.

Example:

```
Recommended Crop:
Rice
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yadukrishnanvr/predictive_ai-farmer.git
```

Move into the project directory:

```bash
cd predictive_ai-farmer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Model Training
5. Model Evaluation
6. Model Serialization
7. Web Application Integration

---

## 📊 Dataset

The model is trained using an agricultural crop recommendation dataset containing soil nutrient values and environmental factors.

Features include:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* pH
* Rainfall

Target:

* Recommended Crop

---

## 🎯 Future Improvements

* Weather API integration
* Fertilizer recommendation
* Plant disease detection
* Crop yield prediction
* Multilingual interface
* Mobile application
* GPS-based recommendations

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yadukrishnan V R**

* GitHub: https://github.com/yadukrishnanvr

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates further development.
