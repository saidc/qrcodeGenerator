from flask import Flask, request, render_template, jsonify
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    text = request.form['text']

    # Crear un objeto BytesIO para almacenar la imagen en memoria
    img_buffer = BytesIO()

    # Generar el código QR en memoria sin guardar en disco
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_buffer, format="PNG")

    # Obtener los datos de la imagen en base64
    img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    return img_data

if __name__ == '__main__':
    app.run(debug=True)
