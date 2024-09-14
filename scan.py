import socket

IP = input("IP: ")
numPorts = 0
porcentaje = 0
for Port in range(0,65535):
        if Port % 5000 == 0:
                porcentaje = round(((100/13) * numPorts))
                print(str(porcentaje) + "% escaneado")
                numPorts += 1
        try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)
                        s.connect((str(IP), int(Port)))

                        print("ABIERTO (" + IP + ":" + str(Port) + ")")
        except:
                pass
