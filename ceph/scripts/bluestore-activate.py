import subprocess
import json

# fetches osd id and uuid from ceph osd dump
def get_osd_uuids():
    command = "ceph osd dump --format=json"
    result = subprocess.run([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    osd_data = json.loads(result.stdout)
    osd_info = [[osd['osd'], osd['uuid']] for osd in osd_data['osds']]
    return osd_info

# activates bluestore volumes
def activate_volumes():
    osd_info = get_osd_uuids()
    for osd in osd_info:
        osd_id, osd_uuid = osd
        command = f"ceph-volume lvm activate --bluestore {osd_id} {osd_uuid}"
        subprocess.run([command], shell=True)

activate_volumes()