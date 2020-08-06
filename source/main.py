import matplotlib.pyplot as plt
from preprocessing import PreSignalProcress
import numpy as np
class Control():

    def __init__(self, s, bd, fa):
        self.bd = bd
        self.fa = fa
        self.data = s
    def creatString(self,sig):
        size = len(sig);
        sig_vector = []
        for i in range(0,size):
            for j in range(0, round(self.fa/self.bd)):
                if(sig[i]==1):
                    sig_vector.append(1)
                else:
                    sig_vector.append(0)
        return sig_vector

    def main(self):
        presignal = PreSignalProcress(self.fa,self.bd,self.data)
        self.data1,self.data2 = presignal.getSeparationData(self.data)
        self.signal1 = self.creatString(self.data1)
        self.signal2 = self.creatString(self.data2)
        self.signalm = presignal.modulation(self.signal1,self.signal2, 500, 200)
        plt.plot(self.signalm)
        #plt.plot(self.signal2)
        #plt.plot(self.signal1)
        print(self.data1, self.data2,self.data1+ self.data2)
        plt.plot(np.array(self.signal1)+np.array(self.signal2))
        plt.show()

if __name__ == "__main__":
    data = [0,0,0,0,1,1,1,0,0,0]
    c = Control(data,100,2000)
    c.main()
