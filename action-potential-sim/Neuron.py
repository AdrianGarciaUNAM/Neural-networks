from random import randint

class Neuron:
    """An abstract model for a Neuron"""
    sodiumChannelOpen = False
    potasiumChannelOpen = False
    in_threshold = False
    potasiumMol = 70
    sodiumMol = 0
    voltage = sodiumMol - potasiumMol
    def __init__(self, shortName, potasiumChannels, sodiumChannels):
        self.shortName = shortName
        self.potasiumChannels = potasiumChannels
        self.sodiumChannels = sodiumChannels

    def is_resting(self):
        return self.voltage <= -60

    def calc_voltage(self):
        self.voltage = self.sodiumMol - self.potasiumMol

    def get_voltage(self):
        return self.voltage

    def in_peak_voltage(self):
        return self.voltage >= 40

    def react(self, stimulus):
        if stimulus + self.voltage >= -55:
            self.in_threshold = True

    def notice(self):
        print "--- {}'s voltage': {}".format(self.shortName, self.voltage)

    def interact(self):
        if self.in_threshold and not self.sodiumChannelOpen:
            print "| / | - Opening sodium channels"
            self.sodiumChannelOpen = True
        if self.sodiumChannelOpen and not self.potasiumChannelOpen:
            print "|o| - Getting sodium"
            for i in range(0, self.sodiumChannels):
                self.sodiumMol = self.sodiumMol + 1
                self.calc_voltage()
                if self.voltage > 40:
                    print "PEAK!: {}V".format(self.voltage)
                    break
        if self.in_peak_voltage():
            print "| / | - Opening potasium channels and closing sodium channels"
            self.potasiumChannelOpen = True
            self.sodiumChannelOpen = False
            self.in_threshold = False
        if self.potasiumChannelOpen and not self.sodiumChannelOpen:
            print "|o| - Getting potasium"
            for i in range(0, self.potasiumChannels):
                self.potasiumMol = self.potasiumMol + 1
                self.calc_voltage()
                if self.voltage < -55:
                    self.in_threshold = False
                    break
