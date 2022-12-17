# octan

...


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
The Show command allows you to "sniff" all incoming
connections you can then decide what client you want to connect to

## mkexploit

mkexploit requires 1 argument and will create an simple reverse shell based on the
configured payload 

```
addr:port/seperator
```

The file it will create will be called "exploit_.py"
you can then configure that payload and obfuscate+compile it blabla bla.

## exploit

The exploit will run an tcp listener which will
accept all clients by default, but if you add an argument
(exploit 192.168.0.51) it will only accept the connection from one single client

# INFO

```
delltaxa/octan > delltaxa/ilander
```
