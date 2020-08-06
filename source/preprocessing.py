
import numpy as np


class PreSignalProcress():
    def __init__(self,fa,bd,data):
        self.n = np.linspace(0,fa,fa/bd*len(data))
        self.bd = bd
        self.fa = fa
    def getSeparationData(self, data):
        self.data1 = data
        self.data2 = -(data - np.ones(len(data)))
        return np.array(self.data1), self.data2
    def modulation(self, signal1, signal2, fc1, fc2):
        return signal1*np.sin(fc1*2*self.n*np.pi)+signal2*np.sin(fc2*2*self.n*np.pi)
