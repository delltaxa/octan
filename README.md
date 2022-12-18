# octan - v1.0.02

Octan is an simple reverse shell manager

![image](https://user-images.githubusercontent.com/114283067/208232874-86fe3a57-1126-4ea1-ae52-b828e0d5938c.png)


# Installation

Script:
```
git clone https://github.com/delltaxa/octan
cd octan/
```

# Usage

To run Octan use
```
bash octan
```

You will land in a shell,
use the help command to see all available commands

The result will look like this

```
COMMAND                      | HELP_TEXT
----------------------------------
exploit <TARGET>        <nr> | Run tcp/listener
mkexploit <PUBLIC_ADDR> <r>  | Create simple reverse shell (exploit_.py)
show <>                 <nr> | display all incoming connections

```

## show

![image](https://user-images.githubusercontent.com/114283067/208232988-f0b121b1-d749-4a87-b18c-228e655340c5.png)


The Show command allows you to "sniff" all incoming
connections you can then decide what client you want to connect to

## mkexploit

![image](https://user-images.githubusercontent.com/114283067/208232945-1992dee5-a642-4e49-adb9-bb6ccd5c5f36.png)


mkexploit requires 1 argument and will create an simple reverse shell based on the
configured payload 

```
addr:port/seperator
```

The file it will create will be called "exploit_.py"
you can then configure that payload and obfuscate+compile it blabla bla.

## exploit

![image](https://user-images.githubusercontent.com/114283067/208233005-a009a0bf-ba18-4e5c-9677-939e1d30b939.png)


The exploit will run an tcp listener which will
accept all clients by default, but if you add an argument
(exploit 192.168.0.51) it will only accept the connection from one single client

# INFO

```
delltaxa/octan > delltaxa/ilander
```
