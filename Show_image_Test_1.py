from PIL import Image

def show_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"에러: {e}")

image_path = "C:/Users/1027a/OneDrive/사진/스크린샷/스크린샷 2024-01-22 161442.png"
show_image(image_path)
