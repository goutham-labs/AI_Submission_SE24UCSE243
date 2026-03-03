import random
import string
import time
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter


IMG_WIDTH = 240
IMG_HEIGHT = 110
TEXT_SIZE = 6


def create_random_code(size=TEXT_SIZE):
    """Creates a random alphanumeric CAPTCHA string."""
    pool = string.ascii_letters + string.digits
    code = ""
    for _ in range(size):
        code += random.choice(pool)
    return code.upper()


def draw_disturbance(draw_obj):
    """Adds random disturbance (lines + pixels) to image."""

    # Draw random crossing lines
    for _ in range(7):
        x1 = random.randint(0, IMG_WIDTH)
        y1 = random.randint(0, IMG_HEIGHT)
        x2 = random.randint(0, IMG_WIDTH)
        y2 = random.randint(0, IMG_HEIGHT)
        draw_obj.line((x1, y1, x2, y2), fill=(120, 120, 120), width=2)

    # Scatter random pixels
    for _ in range(150):
        px = random.randint(0, IMG_WIDTH - 1)
        py = random.randint(0, IMG_HEIGHT - 1)
        draw_obj.point((px, py), fill=(0, 0, 0))


def build_captcha_image(code_text):
    """Generates and saves CAPTCHA image."""

    img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), (255, 255, 255))
    canvas = ImageDraw.Draw(img)

    try:
        font_style = ImageFont.truetype("arial.ttf", 36)
    except:
        font_style = ImageFont.load_default()

    # Place characters with random offsets
    spacing = IMG_WIDTH // (len(code_text) + 1)
    for index, letter in enumerate(code_text):
        xpos = spacing * (index + 1) + random.randint(-8, 8)
        ypos = random.randint(20, 50)
        canvas.text((xpos, ypos), letter, fill=(0, 0, 0), font=font_style)

    draw_disturbance(canvas)

    img = img.filter(ImageFilter.SMOOTH_MORE)

    file_name = "generated_captcha.png"
    img.save(file_name)
    return file_name


def open_image(file_path):
    """Opens image automatically based on OS."""
    if os.name == "nt":  # Windows
        os.system(f'"{file_path}"')
    elif os.name == "posix":
        os.system(f'xdg-open "{file_path}" 2>/dev/null')


def run_captcha_system():
    print("\n===== CAPTCHA AUTHENTICATION SYSTEM =====\n")

    secret_code = create_random_code()
    image_path = build_captcha_image(secret_code)

    print("CAPTCHA image generated. Please check the opened image.")
    open_image(image_path)

    start = time.time()
    answer = input("Type the characters shown in the image: ")

    # Check expiry (90 seconds)
    elapsed = time.time() - start
    if elapsed > 90:
        print("Time expired! Please try again.")
        return

    if answer.strip().upper() == secret_code:
        print("Verification Successful!")
    else:
        print("Wrong CAPTCHA entered.")


if __name__ == "__main__":
    run_captcha_system()
