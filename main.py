# from pyfirmata import Arduino, SERVO, util
# import pyfirmata
import serial
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

# amp1 = 0

plt.style.use('_mpl-gallery')

# port = "COM11"
# sp = 10
# board = Arduino(port)
# board.digital[sp].mode = SERVO


# def calc():
#     global amp1
#     ntp = True
#     for i in range(32):
#         emg1 = anl.read()
#         if emg1 == None:
#             ntp = False
#             break
#         emg1*=255
#         znach = np.array(emg1)
#         sleep(1/128)
#     if ntp:
#         amp1 = 0.3*amp1 + 0.7*(max(znach) - min(znach))
#     print(int(amp1//1))


# def rotateServo(sp, angle):
#     board.digital[sp].write(angle)
#     sleep(0.015)
#
#
# anl = board.get_pin('a:0:i')
# #anl2 = board.get_pin('a:1:i')
#
# it = pyfirmata.util.Iterator(board)
# it.start()

maxtime = 1000

ser = serial.Serial('COM11',9600)


for i in range(maxtime):
    # calc()
    data = str(ser.readline())[2:]
    data = data[:len(data)-5].split(", ")
    for i in range(len(data)):
        data[i] = int(data[i])


    sleep(0.5)
    print(data)

fig, ax = plt.subplots()
vp = ax.violinplot(data, maxtime, widths=2,
                   showmeans=False, showmedians=False, showextrema=False)
for body in vp['bodies']:
    body.set_alpha(0.9)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()