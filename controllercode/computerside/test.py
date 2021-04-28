from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "04c6093b-0000-1000-8000-00805f9b34fb"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ])

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()

print("Accepted connection from ", client_info)

#this part will try to get something form the client
# you are missing this part - please see it's an endlees loop!!
try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        data = data.decode('UTF-8')
        print(data)
        #print(data[0:2])
        # if (data == "right"):
        #     print("right")
        # if (data == "left"):
        #     print("left")
        # if (data[0:2] == "up"):
        #     #print(data)
        #     for i in range(int(data[2:4])):
        #         print("up")
        #         #break
        # if (data[0:4] == "down"):
        #     #print(data)
        #     for i in range(int(data[4:6])):
        #         print("down")
        # #print(data, len(data))

# raise an exception if there was any error
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()