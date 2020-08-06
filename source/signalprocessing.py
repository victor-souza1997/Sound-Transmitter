import numpy as np


class Signal():
	#def filter_IIR(self, fc, bandwith):
	def matrix_DFT(freq, N):
		for i in range(0,N):
			for j in range(0,N)
				M = np.exp(-.j*(2*np.pi/N)*j*i)
		return M

	def DFT(sig, freq):
		M = matrix_DFT(sig, freq)
		return S*M #transformation to frequency domain
