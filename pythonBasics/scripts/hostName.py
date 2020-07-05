from socket import gethostbyname
from socket import gethostname

print('Host IP checker')
domain = input('Put domain name here: ')
ipAddress = gethostbyname(domain)
print('IP address is: ' + ipAddress)

hostname = gethostname()
ipAddress = gethostbyname(hostname)
print('Your IP address is: ' + ipAddress)