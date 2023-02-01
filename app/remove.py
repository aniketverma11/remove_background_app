from rembg import remove

def remove_background(source_image_path, destination_image_path):
    try:
        with open(source_image_path, 'rb') as i, open(destination_image_path, 'wb') as out:
            # read source image in binary format
            input = i.read()
            # apply remove function to remove background
            output = remove(input)
            # save the new image in destination path
            out.write(output)
        print("Image background removed successfully")
        return out
    except Exception as e:
        print(f"There is problem while processed -> {e}")

# source_image_path = "1674889722057.jpg"
# destination_image_path = "1674889722057.png"

# remove_background(source_image_path, destination_image_path)