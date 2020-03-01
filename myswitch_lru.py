from switchyard.lib.userlib import *

def main(net):
    print("Hub is starting up with these ports:")
    for port in net.ports():
        print("{}: ethernet address {}".format(port.name, port.ethaddr))

    while True:
        try:
            input_port,packet = net.recv_packet()
        except Shutdown:
            log_info ("Got shutdown signal; exiting")
            break
        except NoPackets:
            log_info ("No packets were available.")
            continue

        for port in net.ports():
            if port.name == input_port:
                continue
            elif port.name != input_port:
                net.send_packet(port.name, packet)
        
    net.shutdown()