from PIL import Image
import numpy as np
np.set_printoptions(linewidth=1024)

def black_and_white(input_path, output_path, pixel_size):
    # Open the image
    image = Image.open(input_path)

    # Get the size of the image
    width, height = image.size

    # Resize the image to a smaller size (pixelate)

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Calculate the average brightness of the image
    average_brightness = sum(grayscale_image.getdata()) / (image.width * image.height)

    # Set the threshold as a fraction of the average brightness
    threshold_fraction = 0.85  # You can adjust this fraction as needed
    threshold = int(average_brightness * threshold_fraction)

    # Create a binary (black and white) image by thresholding
    binary_image = grayscale_image.point(lambda p: p > threshold and 255)
    # small_image = binary_image.resize((width // pixel_size, height // pixel_size), resample=Image.NEAREST)
    small_image = binary_image.resize((250, 250), resample=Image.NEAREST)
    # Save the result
    small_image.save(output_path)

    image_array = np.array(small_image).astype(np.int16)
    print(type(image_array[0,0]))

    # Change all pixels with values of 255 to values of 1
    image_array[image_array == 255] = 1

    print(image_array)

    return image_array

# Example usage
pixel_size = 10
input_image_path = "2.jpg"
output_image_path = "avatar22.jpg"
black_and_white(input_image_path, output_image_path, pixel_size)