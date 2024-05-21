import os
from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import tempfile
from thumbnail import CreateThumbnail

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def krooz():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img = CreateThumbnail(file,request.form['text-val'],int(request.form['num-val']))
            img_io = BytesIO()  
            img.save(img_io, 'PNG')
            img_io.seek(0)

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            img.save(temp_file, 'PNG')
            temp_file.close()
            
            # Get the filename
            filename = os.path.basename(temp_file.name)
            
            # Redirect to a route that displays the image
            return redirect(url_for('image', filename=filename))

            # return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')
    return render_template("index.html")

@app.route('/image/<filename>')
def image(filename):
    return send_file(os.path.join(tempfile.gettempdir(), filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
