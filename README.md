# iOS-MSDP-Mesh
# Anycast RP Configuration Script

This Python script automates the configuration of routers for an Anycast RP setup, including MSDP peering and PIM configurations. The script connects to the routers via SSH and applies the necessary commands based on user-provided inputs.

## Features
- Configures loopback interfaces for RP and MSDP.
- Sets up inter-router interfaces with an assigned IP schema.
- Configures OSPF and BGP router IDs.
- Establishes MSDP peering among routers.
- Activates multicast configurations including Auto-RP.

## Prerequisites
1. **Python Environment**: Ensure Python 3.6+ is installed.
2. **Dependencies**: Install the `paramiko` library for SSH connections.
   ```bash
   pip install paramiko
   ```
3. **Router Access**:
   - SSH must be enabled on all target routers.
   - Credentials (username and password) with sufficient privileges.

## Usage
1. **Run the Script**:
   Execute the script in a terminal:
   ```bash
   python MSDP-Mesh-Cisco-iOS.py
   ```
2. **Input Details**:
   - Enter the management IPs of the routers (comma-separated).
   - Provide the SSH username and password when prompted.
3. **Configuration Process**:
   - The script connects to each router sequentially and applies the required configuration commands.

## Input Example
```plaintext
Enter router management IPs (comma-separated): 192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4
Enter SSH username: admin
Enter SSH password: ******
```

## Script Workflow
1. The script prompts the user for the management IPs, username, and password.
2. It iterates through the list of IPs, connecting to each router via SSH.
3. Predefined configurations are applied based on the router's role in the Anycast RP setup.
4. A status message confirms whether the configuration was successfully applied.

## Customization
- **Configurations**: Adjust the configuration templates for each router within the `base_configurations` dictionary.
- **Logging**: Add logging mechanisms for detailed operation records.

## Notes
- Ensure that all routers are reachable via SSH from the machine running this script.
- Double-check the IP schema and router-specific configurations before deployment.

## Troubleshooting
- If the script fails to connect:
  - Verify SSH credentials and IP reachability.
  - Check that the `paramiko` library is correctly installed.
- For partial configurations:
  - Re-run the script for affected routers.
  - Verify access and troubleshoot connectivity issues.
