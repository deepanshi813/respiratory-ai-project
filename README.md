# 🫁 AI-Based Respiratory Health Monitoring System

## 📌 Overview

This project is a Machine Learning-based respiratory health monitoring system that analyzes key physiological parameters such as **Carbon Dioxide (CO2)**, **Oxygen Saturation (SpO2)**, and **Breathing Rate**.
The system predicts the patient's condition as **Normal**, **Moderate**, or **Critical** using a trained ML model.

Unlike traditional systems that focus only on oxygen levels, this project emphasizes **CO2 monitoring**, which is a more direct indicator of lung efficiency and respiratory health.

---

## 🎯 Objective

The main objective of this project is to develop an intelligent and user-friendly system that can:

* Monitor respiratory parameters
* Predict health conditions using Machine Learning
* Provide early alerts for critical situations

---

## ✨ Key Features

* 📊 CO2-based respiratory monitoring (primary focus)
* 🤖 Machine Learning prediction using Decision Tree
* 🖥️ Interactive dashboard built with Streamlit
* 🎚️ Real-time input using sliders
* 📈 Data visualization using bar charts
* 🚨 Alert system for critical conditions
* ✅ Simple and easy-to-use interface

---

## 🛠️ Technology Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **Machine Learning Model:** Decision Tree Classifier
* **Libraries Used:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Joblib

---

## ⚙️ Working

1. The user inputs CO2 level, SpO2, and breathing rate using sliders.
2. The system visualizes the input using a bar chart.
3. The trained Decision Tree model analyzes the data.
4. The model predicts the respiratory condition.
5. The result is displayed as:

   * ✅ Normal
   * ⚠️ Moderate
   * 🚨 Critical

---

## 📊 Input Parameters

* **CO2 Level (ppm)**
* **SpO2 (%)**
* **Breathing Rate**

---

## 📤 Output

The system classifies the patient’s condition into:

* Normal
* Moderate Risk
* Critical Condition

---

## 📁 Project Structure

```
respiratory-ai-project/
│
├── dataset.csv        # Training dataset
├── model.py           # ML model training script
├── model.pkl          # Trained model file
├── app.py             # Streamlit web application
└── README.md          # Project documentation
```

---

## ▶️ How to Run the Project

1. Install required libraries:

```
py -m pip install pandas scikit-learn streamlit joblib
```

2. Train the model:

```
python model.py
```

3. Run the application:

```
py -m streamlit run app.py
```

---

## ✅ Advantages

* Early detection of respiratory issues
* Easy to use and interactive interface
* Cost-effective home monitoring solution
* Real-time prediction and visualization

---

## ⚠️ Limitations

* Uses a simulated dataset (not real sensor data)
* Accuracy depends on dataset quality
* Not yet validated for clinical use

---

## 🔮 Future Scope

* Integration with IoT sensors for real-time monitoring
* Mobile application development
* Cloud-based data storage and analytics
* Doctor dashboard for remote patient monitoring

---

## 🏁 Conclusion

This project demonstrates how Machine Learning can be applied in healthcare to monitor respiratory conditions effectively.
It provides a simple yet powerful solution for early detection of respiratory risks and can be extended into a real-world healthcare system.

---

## 👩‍💻 Author

**Deepanshi Sharma**
Added README file
