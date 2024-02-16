import subprocess

devices = ['vdb', 'vdc', 'vdd', 'vde', 'vdf', 'vdg', 'vdh'] # /dev/vda is the OS disk; /dev/vdi is partitioned as wal_db/wal_db-{}-wal and wal_db/wal_db-vdi-db

for dev in devices:
    cmd = [
        'ceph-volume',
        'lvm',
        'prepare',
        '--bluestore',
        '--data',
        f'/dev/{dev}',
        '--block.wal',
        f'wal_db/wal_db-{dev}-wal',
        '--block.db',
        f'wal_db/wal_db-{dev}-db'
    ]
    subprocess.run(cmd)