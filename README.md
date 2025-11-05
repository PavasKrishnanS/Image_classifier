# ✈️ CIFAR-10 Image Classifier with TensorFlow & Streamlit 🚙

## 📌 Overview
An interactive deep learning project that classifies images into one of the 10 **CIFAR-10 categories** — **airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck**.

The project demonstrates the full pipeline of **building an image classification model**, from **dataset loading**, **data preprocessing**, and **custom CNN architecture design** to **model training**, **evaluation**, and **deployment** in a user-friendly web application.

---

## 🧠 Model Development
The training is performed using **TensorFlow/Keras**, where a **Convolutional Neural Network (CNN)** is constructed with:

- Multiple **Conv2D** layers (3x3 kernels) for feature extraction  
- **ReLU activations** for non-linearity  
- **MaxPooling** for spatial downsampling  
- **Dropout regularization** to prevent overfitting  
- A **Dense** layer for classification  
- **Softmax activation** in the output layer for probability distribution  

The dataset’s images are **normalized** (pixel values scaled to 0–1) and **resized** before being fed into the network. The model is optimized using the **Adam optimizer** and trained with the `sparse_categorical_crossentropy` loss function.

---

## 📊 Performance
After training, the model achieves **80%+ test accuracy** on the CIFAR-10 dataset.  
The trained model is saved in `.keras` format and integrated into an interactive **Streamlit** web interface.

---

## 🌐 Web Application
The Streamlit app allows users to **upload their own images** for instant classification.

**Workflow**:
1. Uploaded image is resized to **32x32**, converted to **RGB**, and normalized.  
2. Image is passed through the trained CNN model.  
3. Prediction probabilities are generated.  
4. If the confidence is below **0.9**, the prediction is rejected to avoid false positives.  

This ensures accurate and reliable results in real-time.
 ---

## 🗂 Dataset
This project uses the **CIFAR-10 dataset** from TensorFlow's built-in `keras.datasets` module.

- **Classes**:
  - airplane
  - automobile
  - bird
  - cat
  - deer
  - dog
  - frog
  - horse
  - ship
  - truck

---

## 🛠️ Tech Stack
- **Python** 🐍
- **TensorFlow / Keras** 🤖
- **NumPy** 🔢
- **Matplotlib & Seaborn** 📊
- **Streamlit** 🌐
- **Pillow** 🖼️

---
<img width="1918" height="703" alt="image" src="https://github.com/user-attachments/assets/0ad4b5e1-f254-47ce-a937-6b299c6c9341" />

<img width="1272" height="866" alt="image" src="https://github.com/user-attachments/assets/1cdf9d97-66e8-436c-ba58-1af96e692c9a" />

<img width="1703" height="845" alt="image" src="https://github.com/user-attachments/assets/db3341a6-af32-4e03-86a6-0c54d17aec5c" />



