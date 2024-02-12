from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/saito", methods=["POST"])
def saito():
    data = request.json
    name = data.get("name", "")
    keywords = ["斎", "藤", "貴", "大"]
    for keyword in keywords:
        if keyword in name:
            return jsonify({"result": "斎藤貴大は茨城県出身でカレーが好きな20代男性です。今後のアップデートにより、もっと細かい情報を流出することも可能です"})
        else:
            return jsonify({"result": "あなたには教えられません"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)


