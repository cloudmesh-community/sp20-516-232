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

### Print key list:
```bash
(ENV3) ashok@Ashoks-MacBook-Pro ~ % cms key list                        
+---------+---------+-------------------------------------------------+----------------+
| Name    | Type    | Fingerprint                                     | Comment        |
+---------+---------+-------------------------------------------------+----------------+
| asingam | ssh-rsa | ac:eb:37:cf:0d:40:be:2e:18:0e:9a:57:cc:1d:53:ad | asingam@iu.edu |
+---------+---------+-------------------------------------------------+----------------+
Timer: 0.0000s (key list)
```
### Print security group list:

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
### Cloudmesh boot VM

```
(ENV3) ashok@Ashoks-MacBook-Pro ~ % cms vm boot            

# ----------------------------------------------------------------------
# Create Server
# ----------------------------------------------------------------------

    Cloud:    chameleon
    Name:     asingam-vm-7
    User:     cc
    IP:       129.114.27.25
    Image:    CC-Ubuntu18.04
    Size:     m1.medium
    Network:  e01ee12e-fd22-4b21-a050-d3e015f42bb1
    Public:   True
    Key:      ashok1
    Location: None
    Timeout:  360
    Secgroup: default
    Group:    cloudmesh
    Groups:   ['cloudmesh']

WARNING: secgroup default already exists in cloud. skipping.
{'OS-DCF:diskConfig': 'MANUAL',
 'OS-EXT-AZ:availability_zone': '',
 'OS-EXT-SRV-ATTR:host': None,
 'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
 'OS-EXT-SRV-ATTR:instance_name': '',
 'OS-EXT-STS:power_state': 0,
 'OS-EXT-STS:task_state': 'scheduling',
 'OS-EXT-STS:vm_state': 'building',
 'OS-SRV-USG:launched_at': None,
 'OS-SRV-USG:terminated_at': None,
 'accessIPv4': '',
 'accessIPv6': '',
 'addresses': {},
 'adminPass': 'Rz6HLHuWqxZX',
 'az': '',
 'block_device_mapping': {},
 'cloud': 'defaults',
 'cm': {'cloud': 'chameleon',
        'created': '2020-02-21T02:27:20Z UTC',
        'driver': 'openstack',
        'kind': 'vm',
        'name': 'asingam-vm-7',
        'status': 'BUILD',
        'updated': '2020-02-21 02:27:25.685278'},
 'config_drive': '',
 'created': '2020-02-21T02:27:20Z',
 'created_at': '2020-02-21T02:27:20Z',
 'description': None,
 'disk_config': 'MANUAL',
 'flavor': {'id': '3'},
 'has_config_drive': False,
 'host': None,
 'hostId': '',
 'host_id': '',
 'hostname': None,
 'hypervisor_hostname': None,
 'id': '70319490-cc30-442b-8db3-f92423b67334',
 'image': Munch({'id': '938a7209-9235-451d-8903-cef30cba2ba9'}),
 'instance_name': '',
 'interface_ip': '',
 'ip_public': '',
 'kernel_id': None,
 'key_name': 'ashok1',
 'launch_index': None,
 'launched_at': None,
 'location': {'cloud': 'defaults',
              'project': {'domain_id': None,
                          'domain_name': None,
                          'id': '7767f9aac3c143de8b1f0e6acc70f159',
                          'name': 'cloudmesh'},
              'region_name': 'KVM@TACC',
              'zone': ''},
 'metadata': {},
 'name': 'asingam-vm-7',
 'networks': {},
 'os-extended-volumes:volumes_attached': [],
 'personality': None,
 'power_state': 0,
 'private_v4': '',
 'progress': 0,
 'project_id': '7767f9aac3c143de8b1f0e6acc70f159',
 'properties': {'OS-DCF:diskConfig': 'MANUAL',
                'OS-EXT-AZ:availability_zone': '',
                'OS-EXT-SRV-ATTR:host': None,
                'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
                'OS-EXT-SRV-ATTR:instance_name': '',
                'OS-EXT-STS:power_state': 0,
                'OS-EXT-STS:task_state': 'scheduling',
                'OS-EXT-STS:vm_state': 'building',
                'OS-SRV-USG:launched_at': None,
                'OS-SRV-USG:terminated_at': None,
                'os-extended-volumes:volumes_attached': []},
 'public_v4': '',
 'public_v6': '',
 'ramdisk_id': None,
 'region': 'KVM@TACC',
 'reservation_id': None,
 'root_device_name': None,
 'scheduler_hints': None,
 'security_groups': [],
 'server_groups': None,
 'status': 'BUILD',
 'tags': None,
 'task_state': 'scheduling',
 'tenant_id': '7767f9aac3c143de8b1f0e6acc70f159',
 'terminated_at': None,
 'updated': '2020-02-21T02:27:20Z',
 'user': 'cc',
 'user_data': None,
 'user_id': 'f706e90a101048c2a3f94525a16db197',
 'vm_state': 'building',
 'volumes': []}

# ----------------------------------------------------------------------
# created
# ----------------------------------------------------------------------
# 232:create ./cm/cloudmesh-cloud/cloudmesh/compute/vm/Provider.py
# ----------------------------------------------------------------------
# [{'OS-DCF:diskConfig': 'MANUAL',
#   'OS-EXT-AZ:availability_zone': '',
#   'OS-EXT-SRV-ATTR:host': None,
#   'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
#   'OS-EXT-SRV-ATTR:instance_name': '',
#   'OS-EXT-STS:power_state': 0,
#   'OS-EXT-STS:task_state': 'scheduling',
#   'OS-EXT-STS:vm_state': 'building',
#   'OS-SRV-USG:launched_at': None,
#   'OS-SRV-USG:terminated_at': None,
#   '_id': ObjectId('5e4f3ff20ae671bf12328114'),
#   'accessIPv4': '',
#   'accessIPv6': '',
#   'addresses': {},
#   'adminPass': 'Rz6HLHuWqxZX',
#   'az': '',
#   'block_device_mapping': {},
#   'cloud': 'defaults',
#   'cm': {'cloud': 'chameleon',
#          'collection': 'chameleon-vm',
#          'created': '2020-02-21 02:26:58.597148',
#          'creation_time': '27.00',
#          'group': 'cloudmesh',
#          'kind': 'vm',
#          'modified': '2020-02-21 02:27:27.102412',
#          'name': 'asingam-vm-7',
#          'status': 'available'},
#   'config_drive': '',
#   'created': '2020-02-21T02:27:20Z',
#   'created_at': '2020-02-21T02:27:20Z',
#   'description': None,
#   'disk_config': 'MANUAL',
#   'flavor': {'id': '3'},
#   'has_config_drive': False,
#   'host': None,
#   'hostId': '',
#   'host_id': '',
#   'hostname': None,
#   'hypervisor_hostname': None,
#   'id': '70319490-cc30-442b-8db3-f92423b67334',
#   'image': Munch({'id': '938a7209-9235-451d-8903-cef30cba2ba9'}),
#   'instance_name': '',
#   'interface_ip': '',
#   'ip_public': '',
#   'kernel_id': None,
#   'key_name': 'ashok1',
#   'launch_index': None,
#   'launched_at': None,
#   'location': {'cloud': 'defaults',
#                'project': {'domain_id': None,
#                            'domain_name': None,
#                            'id': '7767f9aac3c143de8b1f0e6acc70f159',
#                            'name': 'cloudmesh'},
#                'region_name': 'KVM@TACC',
#                'zone': ''},
#   'metadata': "{'cm': {'kind': 'vm', 'name': 'asingam-vm-7', 'group': "
#               "'cloudmesh', 'cloud': 'chameleon', 'status': 'booting', "
#               "'collection': 'chameleon-vm', 'created': '2020-02-21 "
#               "02:26:58.597148', 'modified': '2020-02-21 02:26:58.597148', "
#               "'creation_time': '27.00'}, 'image': 'CC-Ubuntu18.04', 'size': "
#               "'m1.medium'}",
#   'name': 'asingam-vm-7',
#   'networks': {},
#   'os-extended-volumes:volumes_attached': [],
#   'personality': None,
#   'power_state': 0,
#   'private_v4': '',
#   'progress': 0,
#   'project_id': '7767f9aac3c143de8b1f0e6acc70f159',
#   'properties': {'OS-DCF:diskConfig': 'MANUAL',
#                  'OS-EXT-AZ:availability_zone': '',
#                  'OS-EXT-SRV-ATTR:host': None,
#                  'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
#                  'OS-EXT-SRV-ATTR:instance_name': '',
#                  'OS-EXT-STS:power_state': 0,
#                  'OS-EXT-STS:task_state': 'scheduling',
#                  'OS-EXT-STS:vm_state': 'building',
#                  'OS-SRV-USG:launched_at': None,
#                  'OS-SRV-USG:terminated_at': None,
#                  'os-extended-volumes:volumes_attached': []},
#   'public_v4': '',
#   'public_v6': '',
#   'ramdisk_id': None,
#   'region': 'KVM@TACC',
#   'reservation_id': None,
#   'root_device_name': None,
#   'scheduler_hints': None,
#   'security_groups': [],
#   'server_groups': None,
#   'status': 'BUILD',
#   'tags': None,
#   'task_state': 'scheduling',
#   'tenant_id': '7767f9aac3c143de8b1f0e6acc70f159',
#   'terminated_at': None,
#   'updated': '2020-02-21T02:27:20Z',
#   'user': 'cc',
#   'user_data': None,
#   'user_id': 'f706e90a101048c2a3f94525a16db197',
#   'vm_state': 'building',
#   'volumes': []}]
# ----------------------------------------------------------------------

Cloudmesh Database Update |################################| 25/25
Cloudmesh Database Update |################################| 1/1
Timer: 31.0000s (vm boot)
```
