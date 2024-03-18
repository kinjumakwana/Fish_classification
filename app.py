from flask import Flask, request, jsonify
from roboflow import Roboflow

# project = rf.workspace("aahana").project("fish-classifications")
# version = project.version(4)
# dataset = version.download("yolov8")

app = Flask(__name__)
rf = Roboflow(api_key="fZuTo2OSTXezd8YarXg7")
# My
# rf = Roboflow(api_key="FiIRbumFQzhql7uhKyHK")
# project = rf.workspace("aahana").project("fish-classifications")
# version = project.version(4)
# dataset = version.download("yolov8")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    file_path = r"D:\Kinjal\Projects\Fish Classification\Application\images\image.jpg"
    file.save(file_path)
    
    # Predict on the uploaded image
    prediction = rf.workspace("uwconveyor").project("uw_conveyor").version(1).model.predict(file_path, confidence=40, overlap=30).json()
    
    # prediction = rf.workspace("aahana").project("fish-classifications").version(4).model.predict(file_path, confidence=40, overlap=30).json()
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)

# # api.py
# import base64
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from roboflow import Roboflow

# app = Flask(__name__)
# CORS(app)

# @app.route('/api/upload-image', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'})

#     image_file = request.files['image']

#     print("image_file--->>>>>>>>.",image_file)

#     # Initialize Roboflow instance
#     rf = Roboflow(api_key="fZuTo2OSTXezd8YarXg7")
#     project = rf.workspace("uwconveyor").project("uw_conveyor")
#     version = project.version(1)
#     model = project.version(1).model

#     try:
#         # Predict on the uploaded image
#         prediction = model.predict(image_file, confidence=40, overlap=30).json()

#         # Process the prediction if needed
#         # For example, you can format the prediction JSON or extract relevant information
#         predictions_formatted = [(pred['label'], pred['confidence']) for pred in prediction['predictions']]

#         # Encode the image file as base64
#         image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
#         json_response = {
#             'message': 'Image processed successfully',
#             'predictions': predictions_formatted,
#             'image_data': image_data
#         }

#         return jsonify(json_response)

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

#     # # Predict on the uploaded image
#     # prediction = model.predict(image_file, confidence=40, overlap=30).json()

#     # # Process the prediction if needed
#     # # For example, you can format the prediction JSON or extract relevant information
    
#     # # Example: Extracting class labels and confidence scores
#     # predictions_formatted = [(pred['label'], pred['confidence']) for pred in prediction['predictions']]

#     # # Encode the image file as base64
#     # image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
#     # json_response = {"result": "Image processed successfully"}

#     # # return jsonify(json_response)
#     # json_response = {
#     #     'message': 'Image processed successfully',
#     #     'predictions': predictions_formatted,
#     #     'image_data': image_data
#     # }

# if __name__ == '__main__':
#     app.run(debug=True)
