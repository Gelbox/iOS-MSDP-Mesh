import paramiko
from getpass import getpass

def configure_router(router_ip, username, password, config_commands):
    """
    Connects to a router via SSH and applies the given configuration commands.
    """
    try:
        print(f"Connecting to {router_ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(router_ip, username=username, password=password)
        
        # Start an interactive shell session
        remote_conn = ssh.invoke_shell()

        # Apply configuration commands
        for command in config_commands:
            remote_conn.send(command + '\n')

        print(f"Configuration applied successfully on {router_ip}.")
        ssh.close()
    except Exception as e:
        print(f"Failed to configure {router_ip}: {e}")

if __name__ == "__main__":
    # User inputs for management IPs and credentials
    management_ips = input("Enter router management IPs (comma-separated): ").split(',')
    username = input("Enter SSH username: ")
    password = getpass("Enter SSH password: ")

    # Base configuration commands for each router
    base_configurations = {
        "RP-1": [
            "interface GigabitEthernet0/1",
            " ip address 192.168.12.1 255.255.255.0",
            " no shutdown",
            "interface GigabitEthernet0/2",
            " ip address 192.168.13.1 255.255.255.0",
            " no shutdown",
            "interface GigabitEthernet0/3",
            " ip address 192.168.14.1 255.255.255.0",
            " no shutdown",
            "interface Loopback0",
            " ip address 10.100.1.1 255.255.255.255",
            "interface Loopback1",
            " ip address 10.100.254.1 255.255.255.255",
            " ip pim sparse-dense-mode",
            "router ospf 1",
            " router-id 1.1.1.1",
            " network 0.0.0.0 255.255.255.255 area 0",
            "router bgp 65001",
            " bgp router-id 1.1.1.1",
            " neighbor flicktronix peer-group",
            " neighbor flicktronix remote-as 65001",
            " neighbor flicktronix update-source Loopback0",
            " neighbor 10.100.1.2 peer-group flicktronix",
            " neighbor 10.100.1.3 peer-group flicktronix",
            " neighbor 10.100.1.4 peer-group flicktronix",
            " address-family ipv4 multicast",
            "  neighbor 10.100.1.2 activate",
            "  neighbor 10.100.1.3 activate",
            "  neighbor 10.100.1.4 activate",
            " exit-address-family",
            "ip pim send-rp-announce Loopback1 scope 20",
            "ip pim send-rp-discovery Loopback1 scope 20",
            "ip msdp peer 10.100.1.2 connect-source Loopback0",
            "ip msdp description 10.100.1.2 to RP-2",
            "ip msdp peer 10.100.1.3 connect-source Loopback0",
            "ip msdp description 10.100.1.3 to RP-3",
            "ip msdp peer 10.100.1.4 connect-source Loopback0",
            "ip msdp description 10.100.1.4 to RP-4",
            "ip msdp mesh-group flicktronix 10.100.1.2",
            "ip msdp mesh-group flicktronix 10.100.1.3",
            "ip msdp mesh-group flicktronix 10.100.1.4",
            "ip msdp cache-sa-state",
            "ip msdp originator-id Loopback0",
        ],
        # Repeat similar configurations for RP-2, RP-3, RP-4 with their respective adjustments.
    }

    # Iterate over each router and apply configurations
    for index, router_ip in enumerate(management_ips, start=1):
        rp_name = f"RP-{index}"
        config_commands = base_configurations.get(rp_name, [])
        configure_router(router_ip.strip(), username, password, config_commands)
