from zoom import zoom
from PIL import Image

def rotate(height: int, width: int, mode: str) -> None:
    if not (isinstance(height, int) or isinstance(width, int) or isinstance(mode, str)):
        print("zoom error args")
        exit(2)
    image = zoom(height, width, mode)
    


def main():
    rotate(400, 400, "L")

if __name__ == "__main__":
    main()
