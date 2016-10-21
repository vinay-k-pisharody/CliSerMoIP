# CliSerMoIP
CliSerMoip is a messenger that functions over the LAN using Socket Communication. It incorporates a Client-Server Architecture
on each node it runs on. It is currently restricted communication between two nodes/computers.

CliSerMoIP achieves the Client-Server architecture by spawning a new thread for a Client and a Server on each node it is running on.

Description for files:

###CliSerMoIP.py

As written earlier, the code spawns a thread for the server and the client. Hence, it includes the classes
ServerThread and ClientThread are created.

The server in turn spawns a new thread for receiving data from the client. Hence, the class ReceiverThread is created.

####Note:

Use 'CTRL+C' to terminate the program at any given point. It will terminate the application on both ends.

The Server Thread is capable of finding its IP address in the given network with the help of the function getip(). 
The Client Thread however has to include the address of the corresponding server it is trying to connect to. Hence, the string 
in the variable host has to be updated accordingly and hard coded onto each machine individually.
