import sys
import socket
import time

usage = "python3 portscan.py TARGET START_PORT END_PORT"

if(len(sys.argv) !=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error : ")
    sys.exit()



start_port = int(sys.argv[2])
end_port = inr(sys.argv[3])

