from PIL import Image


def decode_image_message(image_path):
    """
    Decodes a message from a black and white image.
    :param image_path: The path to the image file.
    :return: The decoded message.
    """
    # Load the image and get the pixel data
    with Image.open(image_path).convert("RGB") as img:
        pixels = img.load()
        if pixels is None:
            print("Failed to load image")
            return ""
        # Extract the rows from the pixel data
        rows = []
        for row in range(img.height):
            row_pixels = []
            for col in range(img.width):
                # Check if the pixel is black
                if pixels[col, row][0] == 0:
                    # Append the row number to the current row's pixels
                    row_pixels.append(row)
            # Append the current row's pixels to the rows list
            rows.append(row_pixels)
        # Convert the row numbers to characters and concatenate them
        message = "".join([chr(row_num) for row in rows for row_num in row])
    return message


if __name__ == "__main__":
    print(decode_image_message("resources/code.png"))
