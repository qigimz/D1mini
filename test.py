import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

your_ESSID ="ctxx"
your_password ="CTXX2021"
sta_if.connect(your ESSID, your password)
 
 n = 0
 while not sta_if.isconnected():
     n+=1
     print("time = %d"%n)

print('net connet:\n IP address:%s\n  netmask:%s\n gatewya:%s\n DNS:%s\n'%sta_if.ifconfig())
