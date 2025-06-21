from backend.app.utils.preprocess import preprocess_image
import cv2

image_path = "sample_assignment.png"
preprocessed = preprocess_image(image_path)

# Save for verification
cv2.imwrite("processed_output.png", preprocessed)
print("✅ Preprocessed image saved as processed_output.png")
