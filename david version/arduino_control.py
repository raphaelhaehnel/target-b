from pyfirmata import Arduino, util
import time


def oscillate(pin1, pin2, time_const):
    time.sleep(time_const)
    pin1.write(1)
    pin2.write(0)
    time.sleep(time_const)
    pin1.write(0)
    pin2.write(1)


def arduinoLoop(leftMagnet, rightMagnet):
    while (True):
        # digital, pin0, output
        # print(Tvl.read())
        oscillate(leftMagnet, rightMagnet, 0.5)


def startArduino():
    board = Arduino('COM5')
    iterator = util.Iterator(board)
    iterator.start()
    leftMagnet = board.get_pin('d:13:o')
    rightMagnet = board.get_pin('d:12:o')
    arduinoLoop(leftMagnet, rightMagnet)






# board.digital[12].write(1)
# output = board.digital[8].read()
# print(output)
