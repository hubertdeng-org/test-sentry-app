from flask import Flask
import sentry_sdk

app = Flask(__name__)

sentry_sdk.init(
    dsn="https://fcb09c140c634aa581724271daa9f1b3@o1383316.ingest.sentry.io/6727714",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

@app.route("/")
def index():
    return "Hello World", 200

@app.route("/error")
def error():
    return "Error", 400

@app.route("/exception")
def division_by_zero():
    division_by_zero = 1 / 0
    return "Should Not Return", 200

@app.route("/sentry-exception")
def sentry_exception():
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)
    return "Sentry Exception", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)