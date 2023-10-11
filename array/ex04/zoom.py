from PIL import Image

from load_image import ft_load

def zoom(height: int, width: int, mode: str) -> Image:

    image = ft_load("../ex02/animal.jpeg")
    if not (isinstance(height, int) or isinstance(width, int) or isinstance(mode, str)):
        print("zoom error args")
        exit(2)

    center_x = image.width // 2
    center_y = image.height // 2
    x1 = center_x - (width // 2)
    y1 = center_y - (height // 2)
    x2 = x1 + width
    y2 = y1 + height

    zoomed = image.crop((x1, y1, x2, y2))
    zoomed = zoomed.convert(mode)

    shape = list(zoomed.size)
    shape.append(zoomed.mode)
    print("New shape of zoomed is:", shape)
    return zoomed
    

def main():
    zoom(400, 400, "L")

if __name__ == "__main__":
    main()