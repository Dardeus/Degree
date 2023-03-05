import cv2
import os

vidcap = cv2.VideoCapture("TestVideo23.mp4")
print(vidcap.read())
success,image = vidcap.read()
count = 0
success = True
while success:
  success, image = vidcap.read()
  if success == False:
    break
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1

image_folder = '.'
video_name = 'video.MP4V'

#images = [img for img in os.listdir(image_folder) if "frame" in img]

images = ["frame%d.jpg" % i for i in range (count)]

print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()