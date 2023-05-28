# import argparse
# from PIL import Image

# # Create an argument parser to accept the image file path as an argument
# parser = argparse.ArgumentParser(description='Display the resolution and DPI of an image')
# parser.add_argument('image_file', type=str, help='path to the image file')
# args = parser.parse_args()

# # Open the image file and get its size and DPI
# with Image.open(args.image_file) as img:
#     size = img.size
#     dpi = img.info.get('dpi', (72, 72))

# # Print the image resolution and DPI on the terminal
# print(f"Image size: {size}")
# print(f"Image DPI: {dpi}" )


from PIL import Image

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        dpi = img.info.get('dpi')
        if dpi:
            print(f"Image size: {width} x {height} pixels")
            print(f"Resolution: {dpi[0]} x {dpi[1]} dpi")
            mm_per_px = 25.4 / dpi[0] # assuming 1 inch = 25.4 mm
            print(f"1 pixel = {mm_per_px:.3f} mm")
        else:
            print("Error: Image DPI not found.")

# example usage
get_image_resolution('data/a01-000u (1).png')
get_image_resolution('../newArchive/data/20230130144112_001.jpg')
