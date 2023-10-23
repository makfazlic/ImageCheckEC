import argparse
import os
import tqdm as tqdm
import warnings

# Helper functions
import helper

# Ignore warnings (Because I like to live dangerously, and they are extremely annoying. Sue me.)
warnings.filterwarnings("ignore")


# Create the parser for selecting the mode to run
parser = argparse.ArgumentParser(description='Face and logo detection, cropping and resizing. Please specify either folder or csv file with images.')

parser.add_argument('-m', '--mode', type=str, help='train or test', required=True, choices=['face', 'logo'])
parser.add_argument('-f', '--folder', type=str, help='path to folder with images')
parser.add_argument('-c', '--csv', type=str, help='path to csv file with images')
parser.add_argument('-i', '--csv_index', type=int, help='index of column with image urls')
parser.add_argument('-s', '--size', type=int, help='width and height of output images', default=512)

args = parser.parse_args()

# Mode and size set from the beginning
mode = args.mode
width_in = height_in = args.size

# Check if both folder and csv are not specified
if args.folder == None and args.csv == None:
    parser.print_help()
    print("IMPORTANT: Please specify either folder (-f) or csv file (-c) with images as input")
    exit()

# Check if both folder and csv are specified simultaneously
if args.folder and args.csv:
    parser.print_help()
    print("IMPORTANT: Please specify either folder (-f) or csv file (-c) with images as input. Not both!")
    exit()

# Check if the csv is specified but the index of column with image urls is not
if args.csv != None and args.csv_index == None:
    parser.print_help()
    print("IMPORTANT: Please specify the index of column with image urls (-i) when using csv file as input")
    exit()


if args.csv != None:
    csv_index = int(args.csv_index)
    image_urls = helper.extract_from_csv(args.csv, csv_index)
    # fetch images from urls
    folder = 'temp'
    if not os.path.exists(folder):
        os.makedirs("./" + folder)
    else:
        print(f'Temp folder "{folder}" already exists. Should we remove it?')
        if input('y/n: ') == 'y':
            # remove all files from the folder
            for file in os.listdir(folder):
                os.remove(folder + '/' + file)
            os.rmdir(folder)
            os.makedirs("./" + folder)
        else:
            print('Please rename or delete the folder and try again.')
            exit()
    helper.fetch_images(image_urls, folder)
else:
    folder = args.folder
    

# Create setup IO for image load and save
images = os.listdir(folder)
folder_name = folder.split('/')[-1]
out_folder = folder_name + '_' + mode + '_' + str(width_in) + 'x' + str(height_in)
if not os.path.exists(out_folder):
    os.makedirs("./" + out_folder)
else:
    print(f'Output folder "{out_folder}" already exists. Should we remove it?')
    if input('y/n: ') == 'y':
        # remove all files from the folder
        for file in os.listdir(out_folder):
            os.remove(out_folder + '/' + file)
        os.rmdir(out_folder)
        os.makedirs("./" + out_folder)
    else:
        print('Please rename or delete the folder and try again.')
        exit()

# Face crop
if mode == 'face':
    print('RUNNING FACE MODE ON {} IMAGES'.format(len(images)))
    print()
    images_completed = 0
    init_size = 0
    final_size = 0
    for i, image in enumerate(images):
        print("START {} ------------ (image {})".format(str(i), image))

        # Get the initial size of the image
        init_size += os.path.getsize(folder + '/' + image)

        # Crop the image
        cropped = helper.crop_face(folder + '/' + image, out_folder)
        if cropped is None:
            print()
            continue
        
        # Resize the image
        resized = helper.resize_image(cropped, width_in, height_in)
        if resized is None:
            os.remove(cropped)
            print()
            continue

        # Convert to webp
        webp = helper.convert_to_webp(resized)

        # Get the final size of the image
        final_size += os.path.getsize(webp)
        images_completed += 1

        print("END {} (image {})".format(str(i), image))  
        print()
        

    print('COMPLETED FACE MODE ON {} IMAGES'.format(images_completed))
    print('Initial size: {} MB'.format(round(init_size / 1024 / 1024, 2)))
    print('Final size: {} MB'.format(round(final_size / 1024 / 1024, 2)))
    change = abs(((final_size - init_size) / init_size) * 100)
    print('🏆 Total size saved: {} MB ({}%)'.format(round((init_size - final_size) / 1024 / 1024, 2), round(change, 2)))
    if images_completed != len(images):
        print('Some images were not processed. Check the output folder!!!')


# Logo detection
if mode == 'logo':
    print('Running logo mode on {} images'.format(len(images)))
    for i, image in enumerate(images):
        print("START {} ------------ (image {})".format(str(i), image))
        # Crop the image
        resized = helper.resize_image(folder + '/' + image, width_in, height_in)
        if resized is None:
            print()
            continue

        transparent = helper.remove_bg(resized, out_folder)
        if transparent is None:
            print()
            continue




        
        print("END {} (image {})".format(str(i), image))
    
