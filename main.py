color=0

def on_forever():
    global color
    radio.send_number(color)
    pins.i2c_read_number(0, NumberFormat.INT8_LE, False)
    basic.pause(100)
    color+=1

basic.forever(on_forever)
