import json
from flask import Flask, request, jsonify
from gpiozero import LED
from time import sleep


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
    return jsonify({'led': {'color':str(led.color),'status':str(led.status)}})

@app.route('/led', methods=['PUT'])
def update_led():
    try:
        data = request.get_json()
        color = data.get("color")
        if color.lower() == "red":
            led.red()
        elif color.lower() == "green":
            led.green()
        elif color.lower() == "blue"
            led.blue()
        elif color.lower() == "off"
            led.off()
        else:
            return jsonify({"options":"'red', 'green', 'blue', 'off'"})
    except:
        return jsonify({"status":"failed to change LED color"})
    
    return jsonify({"color":color.lower()})
    


if __name__ == '__main__':
    led.red()
    sleep(1)
    led.green()
    sleep(1)
    led.blue()
    sleep(1)
    led.off()
    app.run(host="0.0.0.0", port=5000, debug=True)