import time
from serial import Serial
from serial import SerialException

## specify your serial port here !!!
com_port = '/dev/ttyUSB0'
    # for Ubuntu: use '/dev/ttyUSB0' or '/dev/ttyACM0'

baudrate = 38400
timeout = 1.0
try:
    ser = Serial( port=com_port, baudrate=baudrate, timeout=timeout,
                  bytesize=8, parity='N', stopbits=1 )
except SerialException as ex:
    print ex
    sys.exit(-1)
start_time = int(round(time.time() * 1000))
state_LED  = [0, 0, 0]
time_LED   = [int(round(time.time() * 1000)), int(round(time.time() * 1000)), int(round(time.time() * 1000))]

try:
    index = 0
    while 1:
        # basic test
        # ser.write("1L0:")
        # time.sleep(0.5)
        # ser.write("1L1:")
        # time.sleep(0.5)
        # ser.write("2L0:")
        # time.sleep(0.5)
        # ser.write("2L1:")
        # time.sleep(0.5)
        # ser.write("3L0:")
        # time.sleep(0.5)
        # ser.write("3L1:")
        # time.sleep(0.5)
        if(int(round(time.time() * 1000)) - start_time > 10):
            start_time = int(round(time.time() * 1000))
            if(int(round(time.time() * 1000)) - time_LED[index] > 2000 and int(round(time.time() * 1000)) - time_LED[index] < 4000):
                state_LED[index] = 1
            elif(int(round(time.time() * 1000)) - time_LED[index] < 2000):
                state_LED[index] = 0
            else:
                time_LED[index] = int(round(time.time() * 1000))
            ser.write(str(index+1)+"L"+str(state_LED[index])+":")
            # time.sleep(0.01)
            # print str(i+1)+str(state_LED[i])+":"
            if index == 2:
                index = 0
            else:
                index += 1

except KeyboardInterrupt as ex:
    print 'Terminated...'
finally:
    sys.exit(0)
