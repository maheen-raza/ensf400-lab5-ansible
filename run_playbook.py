from ansible_runner import run

cmd = run(
    private_data_dir='./', 
    playbook='hello.yml', 
    inventory='hosts.yml',  
)
print(cmd.events)
