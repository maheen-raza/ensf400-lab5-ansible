# Author: Maheen Raza
import ansible_runner

hello_playbook = "/workspaces/ensf400-lab5-ansible/hello.yml" # defining our directory for our playbook

host_inventory_file = "/workspaces/ensf400-lab5-ansible/hosts.yml" # defining our directory for our host inventory file

runner = ansible_runner.run(playbook=hello_playbook, inventory=host_inventory_file) # using the ansible_runner.interface.run() helper function to run our playbook with our defined inventory host file

print("Status:", runner.stats) # using the Runner.stats function to print out the playbook status from Ansible in the form of a python dictionary
# using the Runner.events function to print out the playbook and host events as python dictionary objects
print("Events:")
for event in runner.events:
    print(event["event"])
