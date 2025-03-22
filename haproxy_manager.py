#!/usr/bin/env python3
import sys
import subprocess
import re

CONFIG_PATH = "/etc/haproxy/haproxy.cfg"
TEMPLATE = """
# PORT FORWARD {src_port} -> {dst_host}:{dst_port}
frontend front_{src_port}
    bind *:{src_port}
    mode tcp
    default_backend back_{src_port}

backend back_{src_port}
    mode tcp
    server {dst_host} {dst_host}:{dst_port} check
"""

def validate_port(port):
    try:
        return 1 <= int(port) <= 65535
    except ValueError:
        return False

def validate_host(host):
    pattern = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$'
    return re.match(pattern, host) is not None

def add_forward_rule(src_port, dst_host, dst_port):
    config = TEMPLATE.format(
        src_port=src_port,
        dst_host=dst_host,
        dst_port=dst_port
    )
    
    with open(CONFIG_PATH, "a") as f:
        f.write(config)
    
    subprocess.run([
        "sudo", "systemctl", "reload", "haproxy"
    ])

def main():
    print("\nHAProxy Port Forward Manager")
    print("============================")
    
    while True:
        src_port = input("\nEnter the incoming port (1-65535): ").strip()
        if not validate_port(src_port):
            print("Error: Invalid port")
            continue
            
        dst_host = input("Enter the destination IP or hostname: ").strip()
        if not validate_host(dst_host):
            print("Error: Invalid hostname")
            continue
            
        dst_port = input("Enter the destination port (1-65535): ").strip()
        if not validate_port(dst_port):
            print("Error: Invalid port")
            continue

        try:
            add_forward_rule(src_port, dst_host, dst_port)
            print(f"\nSuccess: Rule {src_port} -> {dst_host}:{dst_port} added!")
        except Exception as e:
            print(f"Error: {str(e)}")
        
        if input("\nAdd another rule? (y/N): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
