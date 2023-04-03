import serial

class XFM:
    def __init__(self, xfm):
        self.xfm = serial.Serial(f'{xfm}')

    def read_flow(self):
        self.xfm.write('f\r'.encode('ascii'))
        line = self.xfm.readline().decode('ascii')
        return line

    def read_volume(self):
        self.xfm.write('t,r\r'.encode('ascii'))
        line = self.xfm.readline().decode('ascii')
        return line

    def set_lcd_backlight(self, num):
        self.xfm.write(f'b,{num}\r'.encode('ascii'))
        line = self.xfm.readline().decode('ascii')
        line = line[3:-2]
        return line

    def reset_totalizer(self):
        self.xfm.write('t,z\r'.encode('ascii'))

    def enable_totalizer(self):
        self.xfm.write('t,e\r'.encode('ascii'))

    def disable_totalizer(self):
        self.xfm.write('t,d\r'.encode('ascii'))
        
    def limit_totalizer(self):
        self.xfm.write(f't,l,0\r'.encode('ascii'))

class CycleAnalyst:
    def __init__(self, cycle_analyst):
        self.cycle_analyst = serial.Serial(f'{cycle_analyst}')

    def read_values(self):
        line = self.cycle_analyst.readline().decode('ascii')
        values = line.split('\t')
        return values


if __name__ == '__main__':
    xfm1 = XFM('COM3')
    xfm1.limit_totalizer()


# ca = serial.Serial('COM4')

# while True:
#     ca_values = ca.read_values()
#     ah = ca_values[0]
#     volt = ca_values[1]
#     amp = ca_values[2]
#     speed = ca_values[3]
#     distance = ca_values[4]


#     print(xfm1.read_flow)
#     print(xfm1.read_volume)