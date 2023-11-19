import can

class controller:
    def __init__(self):
        self.throtle = 0 # [-1, 1] 
        self.steer = 0 # [-1, 1]
        self.can_interface = can.interface.Bus(channel='can0', bustype='socketcan')
    
    def set_speed(self):
        pass