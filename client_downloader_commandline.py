#!/usr/bin/python3
import sys
import socket

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverName = "localhost"  # change to deplyment server IP
    serverPort = 12000
    clientSocket.connect( (serverName, serverPort) )
    print("Successfully connect to the server " + serverName + ": " + str(serverPort) + ".")
except:
    print("Unable to connect to the server. Exit.")
    sys.exit()

while True:
    account = input("Input your account: ")
    password = input("Input your password: ")
    msg = account + ":" + password

    try:
        clientSocket.send(msg.encode())
        res = clientSocket.recv(1024)
    except socket.timeout:
        print("Connection timeout. Please try again.")
        continue
    except (OSError, BrokenPipeError):
        print("Lose connection to the server. Exit.")
        clientSocket.close()
        sys.exit()
    except AttributeError:
        print("No connection to the server. Exit.")
        clientSocket.close()
        sys.exit()
    except Exception as e:
        print("Error:", e)
    
    if len(res) == 0:
        print("Lose connection to the server. Exit.")
        clientSocket.close()
        sys.exit()
    
    if res.decode() == "logged in":
        break
    print("Invalid account or incorrect password. Please try again.")

while True:
    print("Please choose from the following options:\n"
          "    1. type 'download', add a space, and then copy and paste the code generated from THS\n"
          "    2. type 'exit' to exit")
    command = input("Your command: ")
    processed_command = command.split(" ")
    if not processed_command:
        continue
    elif processed_command[0] == 'download' and len(processed_command) > 1:
        msg = " ".join(processed_command[1:])
        try:
            clientSocket.send(msg.encode())
            # TODO recevie the file from the server and download
            # TODO exceed quota limit situation
            res = clientSocket.recv(1024)
            print(res.decode())
        except socket.timeout:
            print("Connection timeout. Please try again.")
            continue
        except (OSError, BrokenPipeError):
            print("Lose connection to the server. Exit.")
            clientSocket.close()
            sys.exit()
        except AttributeError:
            print("No connection to the server. Exit.")
            clientSocket.close()
            sys.exit()
        except Exception as e:
            print("Error:", e)
        
        if len(res) == 0:
            print("Lose connection to the server. Exit.")
            clientSocket.close()
            sys.exit()

        print("Successfully downloaded!\n")
        
    elif processed_command[0] == 'exit':
        
        try:
            clientSocket.send('exit'.encode())
        except socket.timeout:
            print("Connection timeout. Please try again.")
            continue
        except (OSError, BrokenPipeError):
            print("Lose connection to the server. Exit.")
            clientSocket.close()
            sys.exit()
        except AttributeError:
            print("No connection to the server. Exit.")
            clientSocket.close()
            sys.exit()
        except Exception as e:
            print("Error:", e)

        print("Bye bye.\n")
        clientSocket.close()
        break
    else:
        print("Invalid command.\n")
