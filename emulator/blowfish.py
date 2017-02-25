# -*- coding: utf-8 -*-
import os.path
import struct
import ctypes
import copy
from . import encoder_consts

class blowfish(object):
	"""docstring for blowfish"""
	def __init__(self):
		self.__N__ = 16
		self.__P__ = []
		self.__S__ = copy.deepcopy(encoder_consts.PI_S_BOXES[:])
		for num, i in enumerate(self.__S__):
			for sub_num,ele in enumerate(i):
				self.__S__[num][sub_num] = self.__to_clong__(self.__swap32__(self.__S__[num][sub_num]))

	def __swap32__(self, i):
		return struct.unpack("<I", struct.pack(">I", i))[0]	

	def __to_clong__(self, v):
		return ctypes.c_long(v).value
	
	def __F__(self, x):
		a = x >> 24 & 0x00FF
		b = x >> 16 & 0x00FF
		c = x >> 8 & 0x00FF
		d = x & 0x00FF

		# on 64-bit systems there is an error without '& 0xFFFFFFFF'
		y = (self.__S__[0][a] + self.__S__[1][b]) & 0xFFFFFFFF
		y = y ^ self.__S__[2][c]	& 0xFFFFFFFF
		y = (y + self.__S__[3][d]) & 0xFFFFFFFF
		return self.__to_clong__(y)

	def blowfish_encipher(self, xl, xr):
		for i in range(0, self.__N__):
			xl = xl ^ self.__P__[i]
			xr = self.__F__(xl) ^ xr
			xl,xr = xr,xl

		xl,xr = xr,xl
		xr = xr ^ self.__P__[self.__N__]
		xl = xl ^ self.__P__[self.__N__ + 1]
		return xl, xr

	def blowfish_decipher(self, xl, xr):
		for i in range(self.__N__+1, 1, -1):
			xl = xl ^ self.__P__[i]
			xr = self.__F__(xl) ^ xr
			xl,xr = xr,xl

		xl,xr = xr,xl
		xr = xr ^ self.__P__[1]
		xl = xl ^ self.__P__[0]
		return self.__to_clong__(xl), self.__to_clong__(xr)

	def initialize(self, key):
		j = 0
		for i in range(0, self.__N__+2):
			data = 0x00000000
			for k in range(0, 4):
				data = data << 8
				x = key[j] & 0x000000FF
				data = data | x
				data = ctypes.c_long(data).value
				j = j+1
				if j >= len(key):
					j = 0
				p = self.__swap32__(encoder_consts.PI_P_ARRAY[i])
				v = self.__to_clong__(p ^ data)
			self.__P__.append(v)

		datal = 0x00000000
		datar = 0x00000000

		for i in range(0, self.__N__+2, 2):
			datal, datar = self.blowfish_encipher(datal, datar)
			self.__P__[i] = datal
			self.__P__[i + 1] = datar

		for i in range(0,4):
			for j in range(0, 256, 2):
				datal, datar = self.blowfish_encipher(datal, datar)
				self.__S__[i][j] = datal
				self.__S__[i][j + 1] = datar