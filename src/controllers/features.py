from app import app


@app.route("/", methods=['POST'])
def add():
    app.linebot.prompt()
    return 'OK'  # required for linebot-api webhook
