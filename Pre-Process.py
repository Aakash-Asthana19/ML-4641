import cv2
import os

# Corrected path to the input video
video_path = 'C:/Users/samim/OneDrive - Georgia Institute of Technology/Desktop/ML 4641/Project/ML-4641/Dataset-ML/My_Movie_3.mp4'
output_dir = 'extracted_frames'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()
else:
    print(f"Video file {video_path} opened successfully.")

frame_count = 0

# Loop through the video and save frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No more frames to read or error occurred.")
        break
    
    # Debug print to confirm frame reading
    print(f"Reading frame {frame_count}")

    # Save the frame as an image file
    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    success = cv2.imwrite(frame_filename, frame)
    if not success:
        print(f"Error: Could not write frame {frame_count} to file {frame_filename}")
    
    frame_count += 1

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

print('Frame extraction completed.')

