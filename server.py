from flask import Flask, render_template, request, jsonify
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('werkzeug').setLevel(logging.ERROR)


# initial state
state = {
    "eyes": "left", 
    "eyebrows": "normal",
    "say" : "",
    "tshirt" : "insomnihack",
    "trousers" : "blue"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/state")
def get_state():
    return jsonify(state)

@app.route("/action", methods=["POST"])
def action():
    action = request.form.get("action")
    logging.debug(f"action(): {action}")
    if action in ["left", "up", "right", "down"]:
        state["eyes"] = action
    elif action in [ "normal", "nasty" ]:
        state["eyebrows" ] = action
    elif action in [ "blackalps", "grehack", "insomnihack", "nsec", "pst", "radare", "vb"]:
        state["tshirt"] = action
    elif action in [ "blue", "brown" ]:
        state["trousers"] = action
    return "ok"

@app.route("/say", methods=["POST"])
def say():
    message = request.form.get("message", "").strip()

    if len(message) > 50:
        message = message[:50] # avoid long messages
    logging.debug(f"Say {message}")
    state["say"] = message
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
