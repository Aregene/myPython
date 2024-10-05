from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    image_folder = 'static/images'
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images_data = [(url_for('static', filename=f'images/{image}'), 'https://baidu.com') for image in image_files]
    images_pages = [images_data[i:i+3] for i in range(0, len(images_data), 3)]
    
    # 确保页码在有效范围内
    if page < 1 or page > len(images_pages):
        return "Page not found", 404
    
    return render_template('index.html', images_page=images_pages[page-1], num_pages=len(images_pages), current_page=page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


