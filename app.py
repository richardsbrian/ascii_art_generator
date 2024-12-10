from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

density_options = {
    "High Detail": "Ñ@#W$9876543210?!abc;:+=-,._                    ",
    "Medium Detail": "@%#*+=-:. ",
    "Low Detail": "#*:. "
}

def image_to_ascii(image_path, density="Medium Detail", output_width=100):
    img = Image.open(image_path).convert("L")
    aspect_ratio = img.height / img.width
    new_height = int(output_width * aspect_ratio * 0.55)
    resized_img = img.resize((output_width, new_height))
    density_string = density_options.get(density, density_options["Medium Detail"])
    density_length = len(density_string)

    ascii_art = ""
    for y in range(resized_img.height):
        for x in range(resized_img.width):
            pixel_value = resized_img.getpixel((x, y))
            ascii_art += density_string[pixel_value * (density_length - 1) // 255]
        ascii_art += "\n"
    return ascii_art

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Get density and generate ASCII art
    density = request.form.get('density', 'Medium Detail')
    output_width = int(request.form.get('width', 100))
    ascii_art = image_to_ascii(file_path, density, output_width)

    # Clean up uploaded file
    os.remove(file_path)

    return ascii_art

if __name__ == "__main__":
    app.run(debug=True)
