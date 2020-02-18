# Assignment: Start vms in chamelon cloud,  Ashok Singam sp20-516-232

## Start a vm in chameleon cloud vi horizon, log in, and run the commands

```bash
cc@232-ashok-02:~$ date
Sun Feb 16 19:09:15 UTC 2020
cc@232-ashok-02:~$ uname -a
Linux 232-ashok-02 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
cc@232-ashok-02:~$ hostname
232-ashok-02
cc@232-ashok-02:~$ whoami
cc
cc@232-ashok-02:~$ date
Sun Feb 16 19:09:32 UTC 2020
cc@232-ashok-02:~$ 
```

## Start a vm with cloudmesh and run the commands

```bash
(ENV3) ashok@Ashoks-MacBook-Pro ~ % cms key list                        
+---------+---------+-------------------------------------------------+----------------+
| Name    | Type    | Fingerprint                                     | Comment        |
+---------+---------+-------------------------------------------------+----------------+
| asingam | ssh-rsa | ac:eb:37:cf:0d:40:be:2e:18:0e:9a:57:cc:1d:53:ad | asingam@iu.edu |
+---------+---------+-------------------------------------------------+----------------+
Timer: 0.0000s (key list)
```
Print security group list:

```bash
(ENV3) ashok@Ashoks-MacBook-Pro ~ % cms sec group list --cloud=chameleon
cloud chameleon
+--------------------------------------+------+-----------+-----------+----------------+----------------+----------+-----------+--------------------------------------+
| Name                                 | Tags | Direction | Ethertype | Port range max | Port range min | Protocol | Range     | Remote group id                      |
+--------------------------------------+------+-----------+-----------+----------------+----------------+----------+-----------+--------------------------------------+
| 9fa3d223-762c-445e-8be1-575f3cb410d7 | []   | egress    | IPv6      |                |                |          |           |                                      |
| 9fa3d223-762c-445e-8be1-575f3cb410d7 | []   | egress    | IPv4      |                |                |          |           |                                      |
| default                              | []   | egress    | IPv4      |                |                |          |           |                                      |
| default                              | []   | ingress   | IPv4      | 443            | 443            | tcp      | 0.0.0.0/0 |                                      |
| default                              | []   | ingress   | IPv4      | 22             | 22             | tcp      | 0.0.0.0/0 |                                      |
| default                              | []   | ingress   | IPv4      |                |                | icmp     | 0.0.0.0/0 |                                      |
| default                              | []   | egress    | IPv6      |                |                |          |           |                                      |
| default                              | []   | ingress   | IPv4      | 80             | 80             | tcp      | 0.0.0.0/0 |                                      |
| default                              | []   | ingress   | IPv6      |                |                |          |           | 3220c5c7-d5f7-4941-bd6f-56516d762504 |
| default                              | []   | ingress   | IPv4      |                |                |          |           | 3220c5c7-d5f7-4941-bd6f-56516d762504 |
| flask                                | []   | ingress   | IPv4      | 443            | 443            | tcp      | 0.0.0.0/0 |                                      |
| flask                                | []   | ingress   | IPv4      | 80             | 80             | tcp      | 0.0.0.0/0 |                                      |
| flask                                | []   | ingress   | IPv4      | 22             | 22             | tcp      | 0.0.0.0/0 |                                      |
| flask                                | []   | egress    | IPv6      |                |                |          |           |                                      |
| flask                                | []   | ingress   | IPv4      | 8000           | 8000           | tcp      | 0.0.0.0/0 |                                      |
| flask                                | []   | ingress   | IPv4      |                |                | icmp     | 0.0.0.0/0 |                                      |
| flask                                | []   | egress    | IPv4      |                |                |          |           |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      | 22             | 22             | tcp      | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      | 5000           | 5000           | tcp      | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      | 389            | 389            | tcp      | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      | 80             | 80             | tcp      | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | egress    | IPv6      |                |                |          |           |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      |                |                | icmp     | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | ingress   | IPv4      | 443            | 443            | tcp      | 0.0.0.0/0 |                                      |
| sp20-516-security-group              | []   | egress    | IPv4      |                |                |          |           |                                      |
+--------------------------------------+------+-----------+-----------+----------------+----------------+----------+-----------+--------------------------------------+
Timer: 1.0000s (sec group list --cloud=chameleon)
```
