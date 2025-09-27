import subprocess

def get_status():
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    return result.stdout

def get_diff(file=None):
    cmd = ["git", "diff"]
    if file:
        cmd.append(file)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def get_branches():
    result = subprocess.run(["git", "branch"], capture_output=True, text=True)
    return result.stdout.splitlines()
