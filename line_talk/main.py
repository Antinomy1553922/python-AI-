from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os  #抓系統

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])  #抓取電腦的環境變數(設在render裡面)
handler = WebhookHandler(os.environ['CHANNEL_SECRET']) #抓取電腦的環境變數(設在render裡面)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/callback", methods=['POST'])  #如果網址傳回來是callback，就會執行這裡
def callback():
    signature = request.headers['X-Line-Signature']  #執行這裡，Line的說明書教的
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)   #訊息來會執行這裡
def handle_message(event):
    print(event.message.text)
    message = TextSendMessage(text="我在問你究竟是在說些什麼！")  #傳過來的文字
    line_bot_api.reply_message(event.reply_token, message)


#使用gunicorn main:app,並不會執行以下的程式
#if __name__ == "__main__":
#    print("Hello! World!")
#    app.run(host='0.0.0.0',port=5000)
