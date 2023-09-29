import argparse
import cv2
import face_recognition
import os
import tqdm as tqdm


# Create the parser for selecting the mode to run
parser = argparse.ArgumentParser(description='Select mode')
parser.add_argument('-m', '--mode', type=str, help='train or test', required=True, choices=['face', 'logo'])
parser.add_argument('-f', '--folder', type=str, help='path to folder with images', required=True)
args = parser.parse_args()
mode = args.mode
folder = args.folder

# Create setup IO for image load and save
images = os.listdir(folder)
out_folder = folder + '_output'
if not os.path.exists(out_folder):
    os.makedirs(out_folder)
else:
    print(f'Output folder "{out_folder}" already exists. Delete it or rename it and try again.')
    exit()

# Face crop main branch
if mode == 'face':
    print('=== Running face mode on {} images ==='.format(len(images)))
    for image in tqdm.tqdm(images):
        img = cv2.imread(folder + '/' + image)
        height, width, channels = img.shape
        new_side = min(height, width)

        # Face recognition
        face_locations = face_recognition.face_locations(img)
        for face_location in face_locations:
            top, right, bottom, left = face_location
            center = (int((left + right) / 2), int((top + bottom) / 2))
            center_x, center_y = center
            if width > height:
                top = 0
                bottom = new_side
                left = min(max(0, center_x - int(new_side / 2)), width - new_side)
                right = min(left + new_side, width)
            else:
                left = 0
                right = new_side
                top = min(max(0, center_y - int(new_side / 2)), height - new_side)
                bottom = min(top + new_side, height)
                
            face = img[top:bottom, left:right]
            cv2.imwrite(out_folder + '/' + image, face)
            break


# Logo detection main branch
if mode == 'logo':
    print('Running logo mode on {} images'.format(len(images)))
