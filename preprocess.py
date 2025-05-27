import glob
import cv2
import os
import argparse
def video2img_dataset(video_path, frame_interval, output_dir):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = fps/frame_interval
    frame_count = 0
    video_idx = os.path.basename(video_path).replace('.mp4', '')
    print(video_idx)
    # Read every frame of the video in a loop
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            # Calculate the timestamp corresponding to the current frame (in seconds)
            timestamp = frame_count / fps
            frame_name = f"{video_idx}_{timestamp:.2f}_.png"
            frame_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
    print("All frames saved successfully.")

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description="preprocessing")
    parser.add_argument('--root', type=str, help='path to videos')
    parser.add_argument('--output_dir', type=str, default=10, help='path to images')
    args = parser.parse_args()
    root = args.root
    output_dir = args.output_dir
    videos =  glob.glob(os.path.join(root, '**', '*.mp4'), recursive=True)
    print('--------------start--------------')
    for video in videos:
        video2img_dataset(video, 15, output_dir)
    print('--------------done--------------')
