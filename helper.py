import tqdm as tqdm
import cv2
import face_recognition
import os
import requests
import csv
from PIL import Image
import pillow_heif
from io import BytesIO
import warnings

# Ignore warnings (Because I like to live dangerously, and they are extremely annoying. Sue me.)
warnings.filterwarnings("ignore")


# Function that extracts image urls from a csv file
# Input: path to csv file, index of column with image urls
# Output: list of image urls
def extract_from_csv(csv_file, column):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        # show the number of rows in the csv file
        print('📝 {} rows in the csv file'.format(len(your_list)-1))
        print
        image_array = [row[column] for row in your_list[1:]]
        out = [image for image in image_array if image != '']
        print('📝 {} potential images or non empty fields in column {} in the csv file'.format(len(out), column))
        return out
    
# Function that fixes HEIC images (Apple's image format)
def fix_heif_and_apple_trying_to_be_smart(image):
    heif_file = pillow_heif.read_heif(image)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    return image

# Function that fetches images from urls and saves them in a folder
# Input: list of image urls, name of the folder to save images in
# Output: None
def fetch_images(image_urls, folder):
    print('Fetching {} images... (The whole of selected column)'.format(len(image_urls)))
    for i, image_url in enumerate(image_urls):
        try:
            r = requests.get(image_url, allow_redirects=True)
            if r.status_code == 200:
                # save image
                extension = image_url.split('.')[-1]
                open(folder + '/' + str(i) + "." + extension, 'wb').write(r.content)
                if extension.lower() == 'heic':
                    print("🔧 running a module to fix a HEIC image")
                    # try to fix heic images
                    loaded_image = open(folder + '/' + str(i) + "." + extension, 'rb').read()
                    image = fix_heif_and_apple_trying_to_be_smart(loaded_image)
                    image.save(folder + '/' + str(i) + ".jpg", format="JPEG")
                    os.remove(folder + '/' + str(i) + "." + extension)
                print('✅ Fetched image {} of {}'.format(i, len(image_urls)))
            else:
                print('Status code {} for image {} of {}'.format(r.status_code, i, len(image_urls)))
        except:
            print('🚫 Failed fetching image {} of {}'.format(i, len(image_urls)))

        
    # read the number of files in the folder
    images = os.listdir(folder)
    print('Fetched {} images and saved them in {}.'.format(len(images), folder))

def crop_face(image, out_folder):
    img_cv = cv2.imread(image)
    if img_cv is None:
        print('🚫 Failed to read image {}'.format(image))
        return None        

    height, width, channels = img_cv.shape
    new_side = min(height, width)

    # Face recognition
    face_locations = face_recognition.face_locations(img_cv)
    if len(face_locations) == 0:
        print('🚫 No faces found in image {}'.format(image))
        return None
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
                
        face = img_cv[top:bottom, left:right]
        # save image to out_folder
        out_location = out_folder + '/' + image.split('/')[-1]
        cv2.imwrite(out_location, face)
    print('✅ Cropped image {}'.format(image))
    return out_location

def resize_image(image, width, height):
    img_cv = cv2.imread(image)
    if img_cv is None:
        print('🚫 Failed to read image {}'.format(image))
        return None
    img_cv = cv2.resize(img_cv, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imwrite(image, img_cv)
    print('✅ Resized image {}'.format(image))
    return image

def convert_to_webp(image):
    img = Image.open(image)
    img.save(image.split('.')[0] + '.webp', 'webp')
    os.remove(image)
    print('✅ Converted image to webp {}'.format(image))
    return image.split('.')[0] + '.webp'

def size_of_file(file):
    return os.stat(file).st_size