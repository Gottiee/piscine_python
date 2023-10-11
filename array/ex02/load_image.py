from PIL import Image

def ft_load(path: str) -> list:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    print("Image {image}:".format(image=path), image.format)
    shape = list(image.size)
    shape.append(image.mode)
    print("The shape of image is:", shape)
    pixels = list(image.getdata())
    return [list(pixel) for pixel in pixels]