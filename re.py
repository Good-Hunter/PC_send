#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''a udp server example which send data to client.'''
import numpy as np
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999...'
da=''
flag=0

while True:
    # 接收数据:
	data, addr = s.recvfrom(720*4)#不需要调用listen()方法，而是直接接收来自任何客户端的数据
	print data
	lena = mpimg.imread(data) # 读取和代码处于同一目录下的 lena.png
	plt.imshow(lena) # 显示图片
	plt.axis('off') # 不显示坐标轴
	plt.show()


