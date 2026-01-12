from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    
    if request.method == "POST":
        url = request.form["url"]

        qr = qrcode.make(url)
        qr.save("static/qr.png")

        qr_image = "qr.png"

    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run(debug=True)
