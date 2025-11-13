#Telemetry parser skeleton

import serial, time, threading
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

# Replace 'COMx' with simulator port for now
SERIAL_PORT = 'COM5'
BAUD = 115200

def serial_reader(port, data_callback):
    with serial.Serial(port, BAUD, timeout=1) as ser:
        while True:
            line = ser.readline()
            if not line:
                time.sleep(0.01); continue
            try:
                text = line.decode('utf-8', errors='ignore').strip()
                # For now simulate: CSV "t,roll,pitch,yaw"
                parts = text.split(',')
                if len(parts) >= 4:
                    t, roll, pitch, yaw = map(float, parts[:4])
                    data_callback(t, roll, pitch, yaw)
            except Exception as e:
                print("parse error", e)

# Plotting
app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="Telemetry")
p1 = win.addPlot(title="Attitude")
p1.showGrid(x=True,y=True)
curve_roll = p1.plot(pen='r')
curve_pitch = p1.plot(pen='g')
curve_yaw = p1.plot(pen='b')
data = {'t': [], 'r': [], 'p': [], 'y': []}

def update_plot():
    if len(data['t'])>0:
        curve_roll.setData(data['t'], data['r'])
        curve_pitch.setData(data['t'], data['p'])
        curve_yaw.setData(data['t'], data['y'])

def callback(t, r, p, y):
    data['t'].append(t); data['r'].append(r); data['p'].append(p); data['y'].append(y)
    if len(data['t'])>500:
        for k in data: data[k].pop(0)

# Start a fake serial thread for now (simulate)
def fake_data_generator():
    t = 0.0
    while True:
        callback(t, 5*np.sin(0.5*t), 3*np.sin(0.3*t+0.1), 10*np.sin(0.2*t+0.3))
        t += 0.02
        time.sleep(0.02)

# Thread for simulation
import threading
threading.Thread(target=fake_data_generator, daemon=True).start()

timer = QtCore.QTimer()
timer.timeout.connect(update_plot)
timer.start(50)
QtGui.QApplication.instance().exec_()
