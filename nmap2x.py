import subprocess
import sys

# to take IP as input through command line
target = sys.argv[1]

# runnig naabu to get open ports
initial = subprocess.run(
    ["naabu", "-host", target, "-silent"],
    capture_output=True,
    text=True
)

if initial.stderr:
    print("Error:", initial.stderr)
    sys.exit()

open_ports = []
# storing the ports that are open
for line in initial.stdout.splitlines():
    open_ports.append(line.split(":")[1])
# if no ports were open
if not open_ports:
    print("No open ports found.")
    sys.exit()

ports = ",".join(open_ports)

# running nmap with filtered open ports
final = subprocess.run(
    ["nmap", "-sV", "-sS", "-p", ports, target],
    capture_output=True,
    text=True
)

print(final.stdout)

if final.stderr:
    print("Error:", final.stderr)
