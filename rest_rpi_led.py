import json
from flask import Flask, request, jsonify
from gpiozero import LED


class Led():
    def __init__(self):
        self.color = "none"
        self.status = "off"
        BlueLED.off()
        GreenLED.off()
        RedLED.off()

    def blue(self):
        self.color = "blue"
        self.status = "on"
        BlueLED.on()
        GreenLED.off()
        RedLED.off()

    def green(self):
        self.color = "green"
        self.status = "on"
        BlueLED.off()
        GreenLED.on()
        RedLED.off()

    def red(self):
        self.color = "red"
        self.status = "on"
        BlueLED.off()
        GreenLED.off()
        RedLED.on()

    def off(self):
        self.color = "none"
        self.status = "off"
        BlueLED.off()
        GreenLED.off()
        RedLED.off()

BlueLED = LED(6)
GreenLED = LED(7)
RedLED = LED(8)
led = Led()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def simple_test():
    return jsonify({'status':'success'})

@app.route('/led', methods=['GET'])
def get_led_color():
    return jsonify({'led': color})

@app.route('/led', methods=['POST'])
def update_led():
    color = json.loads(request.data)

    return jsonify(record)
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)