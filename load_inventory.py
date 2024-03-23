# Author: Maheen Raza
from ansible_runner.interface import run_command
import yaml

with open("hosts.yml") as f: # open the inventory file "hosts.yml" in our directory
    inventory_file = yaml.full_load(f) # load the entire hosts file

for group, hosts in inventory_file.items():
    print(f"Group: {group}") # print out the group name
    for host, attrs in hosts.get('hosts', {}).items(): # find the hosts allocated to said group
        print(f"  Name: {host}, IP Address: {attrs.get('ansible_host')}") # print out the hosts and their IP addreses that belong to that specific group

result = run_command("ansible all:localhost -m ping") # using the run_command helper function in the ansible runner documentation to run the command that is given to ping all hosts
print("Results after pinging hosts:\n")
print(result) # printing the results when you ping the hosts