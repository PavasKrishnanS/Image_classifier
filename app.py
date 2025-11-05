import streamlit as st
from PIL import Image
import numpy as np
from tensorflow import keras

# CIFAR-10 class names
class_names = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

st.set_page_config(page_title="CIFAR-10 Image Classifier", page_icon="🚢", layout="centered")

st.title("🚘Image Classifier using CIFAR-10")
st.caption("Upload a **photo of an airplane, car, animal, or ship** (CIFAR-10 classes) and see if your image is recognized!")

if 'uploader_key' not in st.session_state:
    st.session_state['uploader_key'] = 0

uploaded_file = st.file_uploader(
    "Upload an image...",
    type=["jpg", "jpeg", "png"],
    key=st.session_state['uploader_key']
)

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Your Uploaded Image', use_container_width=True)
    img = img.resize((32, 32)).convert('RGB')
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Load model (cached)
    @st.cache_resource
    def load_model():
        return keras.models.load_model('trainedd.keras')

    model = load_model()

    # Model prediction
    pred = model.predict(img_array)
    pred_idx = np.argmax(pred)
    pred_class = class_names[pred_idx]
    pred_probability = float(pred[0][pred_idx])

   
    threshold = 0.9
    if pred_probability < threshold:
        st.error("❌ Sorry, I can't recognize this image. It doesn't match any CIFAR-10 class.")
    else:
        st.success(f"🧠 I hope this is: **{pred_class.capitalize()}**")

    
    if st.button("🔄 Reset"):
        st.session_state['uploader_key'] += 1
        st.rerun()
else:
    st.info("Please upload a JPG or PNG image (will be resized to 32x32, so clarity matters!).")