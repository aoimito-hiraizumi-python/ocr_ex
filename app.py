from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# method=["POST"]を忘れないように
@app.route("/upload", methods=["POST"])
def ocr():
    # リクエストファイルの読み込み
    ocr_files = request.files["uploadFile"]
    img = Image.open(ocr_files)
    # ocr_files.save("static/images/img.png")
    # ocr準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # ocr
    # img = Image.open("static/images/img.png")
    text = tool.image_to_string(
        img,
        lang="eng+jpn",
        builder=pyocr.builders.TextBuilder()
    )
    if text == "":
        text = "読み取りエラー"

    return render_template("index.html", text=text)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)



