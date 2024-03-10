import numpy as np
import matplotlib.pyplot as plt
import socket

host = "84.237.21.36"
port = 5152

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return
        data.extend(packet)
    return data

def extremum(img):
    extr = []
    for y in range(1, img.shape[0]-1):
        for x in range(1, img.shape[1]-1):
            if (img[y-1,x] < img[y,x] and img[y+1,x] < img[y,x] and img[y,x-1] < img[y,x] and img[y,x+1] < img[y,x]):
                extr.append([y, x])
    return extr

def distance(p1, p2):
    return round(np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2), 1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    for i in range(10):

        sock.send(b"get")
        bts = recvall(sock, 40002)
        
        im1 = np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0],bts[1])

        pos1 = np.unravel_index(np.argmax(im1), im1.shape)
        pos2 = np.unravel_index(np.argmin(im1), im1.shape)
        dist = distance(pos1, pos2)

        sock.send(f"{dist}".encode())
        print(sock.recv(20))

        sock.send(b"beat")
        beat = sock.recv(20)
        print(beat)

        plt.title(f"Экстремумы точек: {extremum(im1)} \n Расстояние между точками: {dist}")
        plt.imshow(im1)
        plt.show()