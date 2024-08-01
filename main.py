import os
from PIL import Image

input_folder = "Input"
output_folder = "Output"
scaleable_value = 2



if __name__ == '__main__':

    for file in os.listdir(input_folder):
        foo = Image.open(os.path.join(input_folder,file))  # My image is a 200x374 jpeg that is 102kb large
        height = foo.size[0]//scaleable_value
        width = foo.size[1]//scaleable_value
        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        img = foo.resize((height, width), Image.ANTIALIAS, )

        # img.save('image_scaled.jpg', quality=90)  # The saved downsized image size is 24.8kb
        img.save(os.path.join(output_folder, file), optimize=True, quality=90)  # The saved downsized image size is 22.9kb