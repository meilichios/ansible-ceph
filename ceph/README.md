# ANSIBLE-CEPH deployment scripts

## Description
Installs CEPH via cephadm

## Files
* 01_wipe_lvm.yml
* 02_bluestore.yml
* 03_bootstrap.yml
* 04_bluestore-activate.yml

## Dependencies
### Remote Dependencies
* Linux cephorch300a 5.4.0-1026-kvm #27-Ubuntu SMP Wed Sep 30 23:41:22 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

## Installation
1. Configure / double check vars.yml
2. Wipe LVMs if needed
```ansible-playbook -u super -kK -i ../inventories/domains.ini 01_wipe_lvm.yml```
3. Create bluestore partitions if needed
```ansible-playbook -u super -kK -i ../inventories/domains.ini 02_bluestore.yml```
4. Bootstrap CEPH
```ansible-playbook -u super -kK -i ../inventories/domains.ini 03_bootstrap.yml```
5. Align OSD UUIDs in ceph/scripts/04_bluestore-activate.sh (see CEPH dashboard after step 4)
6. Activate OSDs
```ansible-playbook -u super -kK -i ../inventories/domains.ini 04_bluestore-activate.yml```

## Authors

* VDistefano
## License
This project is licensed under the MIT License