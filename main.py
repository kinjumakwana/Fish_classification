import streamlit as st
import requests

def main():
    st.title("Welcome to Fish classification/ Object Detection with Roboflow.")

    st.markdown("<h4>Please upload an image of a fish of the Flounder, Haddock, HakeRed, or Pollock type.</h4>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    print("uploaded_file-------->>>>>>",uploaded_file)

    if uploaded_file is not None:
        image = uploaded_file.read()
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        

        # Send the image to Flask API for prediction
        response = requests.post('http://localhost:5000/predict', files={'image': image})
        
        if response.status_code == 200:
            prediction = response.json()
            st.write(prediction)
        else:
            st.error("Error occurred while processing image")

if __name__ == "__main__":
    main()

# import streamlit as st
# import requests
# import io

# def main():
#     st.title("Image Upload and JSON Response")

#     uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_image:
#         st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

#         # Convert the uploaded image to bytes
#         image_bytes = uploaded_image.read()

#         # Get the filename
#         filename = uploaded_image.name

#         # Upload the image as a file to the API endpoint and get JSON response
#         api_endpoint = 'http://localhost:5000/api/upload-image'  # Change to your API endpoint URL
#         response = requests.post(api_endpoint, files={'image': (filename, image_bytes)})

#         if response.status_code == 200:
#             json_response = response.json()
#             st.json(json_response)
#         else:
#             st.error('Failed to get JSON response from the API')

# if __name__ == '__main__':
#     main()
