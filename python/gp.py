import subprocess

# Replace "your_command_here" with the actual command you want to run in the cmd.
cmd_command = "git add ."
cmd_command1 = " git commit -a -m \"python testing\" "
cmd_command2 = "git push -u origin"
def deploy():
    
    completed_process = subprocess.run(cmd_command, shell=True, check=True, text=True)

    if completed_process:
        print("FIRST process completed")
    else:
        print(" FIRST NOT COMPLETED!!!!")

    completed_process1 = subprocess.run(cmd_command1, shell=True, check=True, text=True)
    
    if completed_process1:
            print("SECOND process completed")
    else:
        print(" SECOND NOT COMPLETED!!!!")
            
    completed_process2 = subprocess.run(cmd_command2, shell=True, check=True, text=True)
    if completed_process2:
        print("THIRD process completed")

    else:

        print(" THIRD NOT COMPLETED!!!!")

try:
    deploy()
    print("Command output:")
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error message: {e.stderr}")
