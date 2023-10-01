# Headquarters
```
enable
erase startup-config

configure terminal
interface GigabitEthernet0/0
ip address 195.100.16.1 255.255.248.0
no shutdown

interface Serial0/0/0
ip address 195.100.28.65 255.255.255.252
no shutdown
interface Serial0/0/1
ip address 195.100.28.69 255.255.255.252
no shutdown
interface Serial0/1/0
ip address 195.100.28.73 255.255.255.252
no shutdown
interface Serial0/1/1
ip address 195.100.28.77 255.255.255.252
no shutdown
exit

ip route 195.100.0.0 255.255.240.0 195.100.28.66
ip route 195.100.28.0 255.255.255.224 195.100.28.70
ip route 195.100.24.0 255.255.252.0 195.100.28.74
ip route 195.100.28.32 255.255.255.224 195.100.28.78
exit

copy running-config startup-config

```


# Lobby
```
enable
erase startup-config

configure terminal
interface GigabitEthernet0/0
ip address 195.100.0.1 255.255.240.0
ip helper-address 195.100.16.252
no shutdown

interface Serial0/0/0
ip address 195.100.28.66 255.255.255.252
no shutdown
interface Serial0/2/0
ip address 195.100.28.81 255.255.255.252
no shutdown
interface Serial0/2/1
ip address 195.100.28.85 255.255.255.252
no shutdown
interface Serial0/3/0
ip address 195.100.28.89 255.255.255.252
no shutdown
exit

ip route 195.100.16.0 255.255.248.0 195.100.28.65
ip route 195.100.28.0 255.255.255.224 195.100.28.65
ip route 195.100.24.0 255.255.252.0 195.100.28.65
ip route 195.100.28.32 255.255.255.224 195.100.28.65

router rip
version 2
no auto-summary
network 195.100.0.0
network 195.100.28.80
network 195.100.28.84
network 195.100.28.88
no auto-summary
exit
exit

copy running-config startup-config

```



# Mercenery
```
enable
erase startup-config

configure terminal
interface GigabitEthernet0/0
ip address 195.100.28.1 255.255.255.224
ip helper-address 195.100.16.252
no shutdown

interface Serial0/0/1
ip address 195.100.28.70 255.255.255.252
no shutdown
interface Serial0/2/0
ip address 195.100.28.82 255.255.255.252
no shutdown
interface Serial0/2/1
ip address 195.100.28.93 255.255.255.252
no shutdown
interface Serial0/3/0
ip address 195.100.28.101 255.255.255.252
no shutdown
exit

ip route 195.100.16.0 255.255.248.0 195.100.28.69
ip route 195.100.0.0 255.255.240.0 195.100.28.69
ip route 195.100.24.0 255.255.252.0 195.100.28.69
ip route 195.100.28.32 255.255.255.224 195.100.28.69

router rip
version 2
no auto-summary
network 195.100.28.0
network 195.100.28.80
network 195.100.28.100
network 195.100.28.92
no auto-summary
exit
exit

copy running-config startup-config

```



# Intelligence
```
enable
erase startup-config

configure terminal
interface GigabitEthernet0/0
ip address 195.100.24.1 255.255.252.0
ip helper-address 195.100.16.252
no shutdown

interface Serial0/1/0
ip address 195.100.28.74 255.255.255.252
no shutdown
interface Serial0/2/1
ip address 195.100.28.86 255.255.255.252
no shutdown
interface Serial0/3/0
ip address 195.100.28.102 255.255.255.252
no shutdown
interface Serial0/3/1
ip address 195.100.28.97 255.255.255.252
no shutdown
exit

ip route 195.100.16.0 255.255.248.0 195.100.28.73
ip route 195.100.0.0 255.255.240.0 195.100.28.73
ip route 195.100.28.0 255.255.255.224 195.100.28.73
ip route 195.100.28.32 255.255.255.224 195.100.28.73

router rip
version 2
no auto-summary
network 195.100.24.0
network 195.100.28.84
network 195.100.28.100
network 195.100.28.96
no auto-summary
exit
exit

copy running-config startup-config

```


# Undertaking
```
enable
erase startup-config

configure terminal
interface GigabitEthernet0/0
ip address 195.100.28.33 255.255.255.224
ip helper-address 195.100.16.252
no shutdown
exit

interface Serial0/1/1
ip address 195.100.28.78 255.255.255.252
no shutdown
interface Serial0/3/0
ip address 195.100.28.90 255.255.255.252
no shutdown
interface Serial0/2/1
ip address 195.100.28.94 255.255.255.252
no shutdown
interface Serial0/3/1
ip address 195.100.28.98 255.255.255.252
no shutdown
exit

ip route 195.100.16.0 255.255.248.0 195.100.28.77
ip route 195.100.0.0 255.255.240.0 195.100.28.77
ip route 195.100.28.0 255.255.255.224 195.100.28.77
ip route 195.100.24.0 255.255.252.0 195.100.28.77

router rip
version 2
no auto-summary
network 195.100.28.32
network 195.100.28.88
network 195.100.28.92
network 195.100.28.96
no auto-summary
exit
exit

copy running-config startup-config

```


