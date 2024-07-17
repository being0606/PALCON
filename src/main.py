import cv2
import numpy as np
from ultralytics import YOLO

def main():
    # Load the YOLO model
    model = YOLO("yolov8n-seg.pt")

    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # Define the target class indices and their corresponding colors
    target_class_indices = [41, 43, 44, 45, 46, 47]
    class_names = ["cup", "fork", "knife", "spoon", "bowl", "plate"]
    colors = [
        (205, 115, 15),   # Red for cup
        (0, 255, 0),   # Green for fork
        (0, 0, 255),   # Blue for knife
        (255, 255, 0), # Cyan for spoon
        (255, 0, 255), # Magenta for bowl
        (0, 255, 255)  # Yellow for plate
    ]

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        results = model(frame)
        img = frame.copy()

        if results[0].masks is not None:
            for mask, cls, box in zip(results[0].masks.data, results[0].boxes.cls, results[0].boxes.xyxy):
                cls = int(cls)
                if cls in target_class_indices:
                    mask = mask.cpu().numpy().squeeze()

                    # Get original mask dimensions
                    mask_height, mask_width = mask.shape

                    # Resize mask to match image dimensions
                    mask_resized = cv2.resize(mask, (img.shape[1], img.shape[0]))

                    # Calculate moments on the resized mask
                    moments = cv2.moments(mask_resized)
                    if moments["m00"] != 0:
                        center_x = int(moments["m10"] / moments["m00"])
                        center_y = int(moments["m01"] / moments["m00"])
                    else:
                        center_x, center_y = 0, 0

                    color = colors[target_class_indices.index(cls)]

                    # Apply mask to image
                    img[mask_resized > 0.5] = img[mask_resized > 0.5] * 0.5 + np.array(color) * 0.5

                    x1, y1, x2, y2 = map(int, box)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

                    class_name = class_names[target_class_indices.index(cls)]
                    label = f"{class_name} ({center_x},{center_y})"
                    cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3, cv2.LINE_AA)

                    # Draw a red circle at the center of the segmentation mask
                    cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)

        cv2.imshow('Original Image with Predictions', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()