import subprocess

def run_command(command):
    return subprocess.getoutput(command).splitlines()

volume_groups = run_command("vgdisplay | grep 'VG Name' | awk '{print $3}'")
physical_volumes = run_command("pvdisplay | grep 'PV Name' | awk '{print $3}'")

for g in volume_groups:
    subprocess.run(["vgremove", "--force", g])

for i in physical_volumes:
    subprocess.run(["pvremove", "--force", i])