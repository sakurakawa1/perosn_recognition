import cv2
import os
from tqdm import tqdm

fsp = 9
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

n = 0
video_path = 'videos/lepton_out1.mp4'
img_path = r"D:\Python\thermal_processing\lepton_out"
list_image = os.listdir(img_path)
list_image.sort()

list_image = [os.path.join(img_path, x) for x in list_image]
width = cv2.imread(list_image[0]).shape[1]
heighth = cv2.imread(list_image[0]).shape[0]

video_out = cv2.VideoWriter(video_path, fourcc, fsp, (width, heighth))

count = 0
for i in tqdm(range(len(list_image))):
    if os.path.exists(list_image[i]):
        frame = cv2.imread(list_image[i])
        video_out.write(frame)
        count += 1

print('cout', count)

video_out.release()