from bluetooth import *
import pyautogui

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ])

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()

print("Accepted connection from ", client_info)

#this part will try to get something form the client
# you are missing this part - please see it's an endlees loop!!
print("resolution of the monitor: ", pyautogui.size())
a, b = pyautogui.size()
print("location of the cursor now: ", pyautogui.position())
try:
    while True:
        x, y = pyautogui.position()
        # print(x, y)
        rawdata = client_sock.recv(1024)
        if len(rawdata) == 0: break
        rawdata = rawdata.decode('UTF-8')
        rawdata = rawdata.split()
        for data in rawdata:
            print(data)
            #print(data[0:2])
            if (data == "right"):
                x, y = pyautogui.position()
                pyautogui.moveTo(min(x+10, a), y, 0)
            if (data == "left"):
                x, y = pyautogui.position()
                pyautogui.moveTo(max(x-10, 0), y, 0)
            if (data[0:2] == "up"):
                x, y = pyautogui.position()
                #print(data)
                pyautogui.moveTo(x, min(0, y-10), 0)
                #break
            if (data[0:4] == "down"):
                x, y = pyautogui.position()
                pyautogui.moveTo(x, max(b, y+10), 0)

# raise an exception if there was any error
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()