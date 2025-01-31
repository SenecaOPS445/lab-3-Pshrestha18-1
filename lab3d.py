#!/usr/bin/env python3

import subprocess

def free_space():
    # Run the command to get free space on the root directory
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, shell=True)
    stdout, _ = p.communicate()
    
    # Decode from bytes to string and strip new line characters
    return stdout.decode('utf-8').strip()