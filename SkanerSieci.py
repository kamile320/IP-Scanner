import subprocess
file = open('wynik.txt', 'a')

def ping_ip(ip):
    result = subprocess.Popen((['ping', ip, '-n', '1']), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = result.communicate()
    if b'bytes=32' in output:
        return " Działa"
    elif b'Destination host unreachable.' in output:
        return " Brak Odpowiedzi"
    elif error:
        return " Błąd DNS"
    else:
        return " Nieznany"

addr = input("Podaj pierwsze 3 części adresu IP (np.: 192.168.0.): ")
a = input("Podaj początek zakresu skanowania (1-255):")
b = input("Podaj koniec zakresu skanowania (1-255):")
try:
    for ip in range(int(a),int(b)+1):
        ip = str(addr)+str(ip)
        ip = ip.strip('\n')
        response = ping_ip(ip)
        result = ('%s,%s \n' % (ip, response))
        print(result)
        file.write(result)
except:
    print(':( Błąd')

end = input("Wciśnij x aby zakończyć ")
if end == 'x':
    file.close()
    exit()
else:
    file.close()