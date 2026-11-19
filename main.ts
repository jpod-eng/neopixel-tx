let color = 0
basic.forever(function on_forever() {
    
    radio.sendNumber(color)
    pins.i2cReadNumber(0, NumberFormat.Int8LE, false)
    basic.pause(100)
    color += 1
})
