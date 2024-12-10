
# ASCII Art Generator

This project is a Flask-based web application that converts uploaded images into ASCII art. Users can upload an image, select the ASCII density, and customize the output width. The app also features a dynamic animated background and a modern user interface.

## Features

- Upload images and convert them to ASCII art.
- Choose from three ASCII density levels: High Detail, Medium Detail, and Low Detail.
- Customize the output width for the ASCII art.
- Animated falling ASCII effect as a background for enhanced visual appeal.
- Responsive design for various screen sizes.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ascii-art-generator.git
   cd ascii-art-generator
   ```

2. **Install dependencies:**

   Ensure you have Python 3.8+ installed. Use the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

4. **Access the application:**

   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Navigate to the homepage.
2. Upload an image by clicking the "Choose File" button.
3. Select the ASCII density:
   - High Detail
   - Medium Detail (default)
   - Low Detail
4. Specify the output width for the ASCII art.
5. Click the "Generate ASCII Art" button.
6. View and copy the generated ASCII art from the text area.

## File Structure

```
ascii-art-generator/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML template for the web interface
├── static/
│   └── fallingAscii.js    # JavaScript file for falling ASCII animation
├── uploads/               # Temporary folder for uploaded images
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Requirements

Below are the Python dependencies needed for this project (specified in `requirements.txt`):

- Flask
- Pillow

Install them with:

```bash
pip install -r requirements.txt
```

## Animated Background

The animated background is created using the `fallingAscii.js` script, which simulates falling ASCII characters. The animation is responsive and adjusts to the screen size.

## Notes

- Uploaded files are temporarily stored in the `uploads` directory and deleted immediately after processing.
- The ASCII art is generated using the PIL (Pillow) library by converting the image to grayscale and mapping pixel values to ASCII characters based on the selected density.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.
