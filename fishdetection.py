from ultralytics import YOLO

class FishObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_fish(self, image_url):
        # Predict with the model
        results = self.model(image_url)

        for result in results:
            boxes = result. boxes  # Boxes object for bounding box outputs
            names = result.names
            conf = result.boxes.conf   # confidence score, (N, 1)
            cls = result.boxes.cls    # cls, (N, 1)
            orig_shape = result.boxes.orig_shape
            # print(f"boxes is: {boxes}, names is: {names},cls is: {cls},conf is: {conf}, orig_shape is: {orig_shape}")
            
        result_json = {
            "image": {
                "height": orig_shape[0],
                "width": orig_shape[1]
            },
            "predictions": []
        }
        max_confidence_index = -1
        max_confidence = -1
        
        # Find the index of the prediction with the highest confidence
        for i, conf_score in enumerate(conf):
            if conf_score > max_confidence:
                max_confidence = conf_score
                max_confidence_index = i

        # Add the prediction with the highest confidence to the result_json
        if max_confidence_index != -1:
            prediction = {
                "class": names[int(cls[max_confidence_index])],
                "class_id": int(cls[max_confidence_index]),
                "confidence": float(conf[max_confidence_index]),
                "image_url": image_url,
                "prediction_type": "ObjectDetectionModel",
                # "image_height": orig_shape[0],
                # "image_width": orig_shape[1]
            }
            result_json["predictions"].append(prediction)
        # print(result_json)

        return result_json

# Usage
detector = FishObjectDetector(r'D:\Kinjal\Projects\Fish Classification\Application\model\best.pt')
image_url = 'https://images.saymedia-content.com/.image/t_share/MTc0NjE5MDI4ODIyODk0NTM3/how-to-cook-haddock.jpg'
result = detector.detect_fish(image_url)
print(result)
