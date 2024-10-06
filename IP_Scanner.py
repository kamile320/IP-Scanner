import subprocess
file = open('output.txt', 'a')

def ping_ip(ip):
    result = subprocess.Popen((['ping', ip, '-n', '1']), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = result.communicate()
    if b'bytes=32' in output:
        return " Up"
    elif b'Destination host unreachable.' in output:
        return " No response"
    elif error:
        return " DNS Error"
    else:
        return " Unknown"

addr = input("Enter first 3 parts of IP Address (eg. 192.168.0.): ")
a = input("Enter start of scanning range (1-255): ")
b = input("Enter end of scanning range (1-255): ")
try:
    for ip in range(int(a),int(b)+1):
        ip = str(addr)+str(ip)
        ip = ip.strip('\n')
        response = ping_ip(ip)
        result = ('%s,%s \n' % (ip, response))
        print(result)
        file.write(result)
except:
    print(':( Err')

end = input("Press x to quit ")
if end == 'x':
    file.close()
    exit()
else:
    file.close()