from PIL import Image
import os

ASCII_CHARS = " .:-=+*#%@"
CHAR_LEN = len(ASCII_CHARS)

def convert_and_save_ascii(image_path, output_folder='asciiFrames', width=80, height=40):
    try:
        img = Image.open(image_path).resize((width, height)).convert("L")
        pixels = img.getdata()
        ascii_str = "".join(ASCII_CHARS[pixel * CHAR_LEN // 256] for pixel in pixels)

        lines = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
        ascii_art = "\n".join(lines)

        base_name = os.path.basename(image_path).replace(".png", ".txt")
        ascii_path = os.path.join(output_folder, base_name)
        os.makedirs(output_folder, exist_ok=True)

        with open(ascii_path, "w", encoding="utf-8") as f:
            f.write(ascii_art)

    except Exception as e:
        print(f"[ERROR] Failed to convert {image_path}: {e}")
