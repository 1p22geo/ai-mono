from flask import Flask, request, redirect
from rag_set import query, load
from werkzeug.utils import secure_filename
import mimetypes
from datetime import datetime
import os


UPLOAD_FOLDER = './data/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET'])
def index():
    return redirect("/static/index.html", code=302)


@app.route('/api/query', methods=['POST'])
def api_query():
    json = request.json
    try:
        res = query(json['prompt'])
        context = []
        for doc in res['context']:
            context.append(doc.dict())
        return {"answer": res['answer'], "context": context}
    except:
        return {"answer": "An error occured. Make sure to upload some documents before chatting with them."}


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        raise "No file bruh"
    file = request.files['file']
    if file.filename == '':
        raise 'No selected file'
    if file:
        filename = datetime.now().isoformat() + \
            secure_filename(file.filename).split(
                ".")[0] + mimetypes.guess_extension(file.mimetype)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        load(filename)
    return redirect("/", code=302)


@app.route("/files", methods=['GET'])
def list_files():
    files = []
    for file in os.listdir("data/"):
        files.append(file)
    return files


if __name__ == "__main__":
    app.run()
