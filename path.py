from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = f"uploads/{uploaded_file.filename}"
            uploaded_file.save(file_path)  # Save the uploaded file to the server
            return render_template('result.html', file_path=file_path)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
