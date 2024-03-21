import ansible_runner
import yaml

with open("hosts.yml") as f: # open the inventory file "hosts.yml" in our directory
    inventory_file = yaml.full_load(f) # load the entire inventory file

for group, hosts in inventory_file.items():
    print(f"Group: {group}") # print out the group name
    for host, attrs in hosts.get('hosts', {}).items(): # find the hosts allocated to said group
        print(f"  Name: {host}, IP Address: {attrs.get('ansible_host')}") # print out the hosts and their IP addreses that belong to that specific group