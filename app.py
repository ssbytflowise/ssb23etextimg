from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get image file from form
        image_file = request.files['image']
        image = Image.open(image_file)

        # Get text attributes from form
        text = request.form['text']
        size = int(request.form['size'])
        color = tuple(map(int, request.form['color'].split(',')))
        position = tuple(map(int, request.form['position'].split(',')))

        # Set up drawing context
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size)

        # Add text to image
        draw.text(position, text, font=font, fill=color)

        # Save the edited image to a byte stream
        byte_stream = io.BytesIO()
        image.save(byte_stream, format='PNG')
        byte_stream.seek(0)

        return send_file(byte_stream, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
