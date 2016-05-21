import socket
import select
import subprocess

video_port = 5555
buffer_size = 8000

video_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
video_socket.connect(('192.168.1.1', video_port))
video_socket.setblocking(0)
print "connected"
cmdline = ['ffplay', '-framedrop', '-']
player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

while True:
    inputready, outputready, exceptready = select.select([video_socket],[],[])
    for i in inputready:
        if i==video_socket:
            data=""
            while 1:
                try:
                    data = video_socket.recv(buffer_size)
                except IOError:
                    break
            player.stdin.write(data)
video_socket.close()
print "end"