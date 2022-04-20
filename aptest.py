import socket
def set_ap(ssid,password):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.bind('',8889)
    cmd_str = 'command'
    my_socket.sendto(cmd_str.encode('utf-8'),('192.168.10.1',8889))
    response, ip = my_socket.recvfrom(100)
    print('form %s,%s,'%(ip,response))
    cmd_str = 'ap %s: %s'% (ssid,password)
    print('sendign command %s'% cmd_str)
    my_socket.sendto(cmd_str.encode('utf-8'),('192.168.10.1',8889))
    response, ip = my_socket.recvfrom(100)
    print('from %s: %s' %(ip,response))
set_ap('Telstra7E1206','wwt6jrurm8')