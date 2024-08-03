import streamlit as st
import pickle
import base64

# Load the trained model
with open(r"C:\Users\mahes\phase 2 machine learning\model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

# Define the label to image path mapping
label_to_image = {
    "sad": r"C:\Users\mahes\OneDrive\Pictures\sad1.png",
    "joy": r"C:\Users\mahes\OneDrive\Pictures\joy.png",
    "love": r"C:\Users\mahes\OneDrive\Pictures\love.png",
    "anger": r"C:\Users\mahes\OneDrive\Pictures\anger.png",
    "fear": r"C:\Users\mahes\OneDrive\Pictures\fear.png",
    "surprise": r"C:\Users\mahes\OneDrive\Pictures\surprise.png"
}

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.image(r"C:\Users\mahes\OneDrive\Pictures\innomatcis logo.webp")

# Set the title of the Streamlit app
st.title("Emotion Detection")

# Text input
input_text = st.text_area("Enter some text:")

# Button to trigger prediction
if st.button("DETECT"):
    if input_text:
        # Predict the emotion
        predicted_label = model.predict([input_text])[0].lower()  # Ensure the label is in lowercase
        image_path = label_to_image.get(predicted_label, None)  # Get the image path

        # Display the predicted emotion and corresponding image
        if image_path:
            image_base64 = get_image_base64(image_path)
            st.write(f"Predicted Emotion: {predicted_label.capitalize()}")
            st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="{predicted_label}" style="width:300px;height:300px;">', unsafe_allow_html=True)
        else:
            st.write(f"Predicted Emotion: {predicted_label.capitalize()}")
    else:
        st.write("Please enter some text.")
