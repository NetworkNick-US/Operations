# OperationalItems
A collection of frequently used scripts and playbooks. This collection contains both Python and Ansible scripts that have found various uses within my personal or professional roles. Variable files are not included in this repo.

## Python Scripts

Script              | Features | Purpose
:-------------         | ------------- | -------------
[icmpMonitor](https://github.com/NetworkNick-io/Operations/tree/main/ICMPmonitor) |  Basic ICMP monitoring script for use in small isolated environments. | Created for non-network administrators or power-users to improve situational awarness when other monitoring tools (SolarWinds, Nagios, etc.) are not available.
[hashPW](https://github.com/NetworkNick-US/Operations/blob/main/hashPW.py) | Basic script to hash passwords (MD5) for use on Cisco IOS and IOS XE Ansible playbooks. | Supporting file to produce an MD5 hash for the fallback admin password for [createLocalAdmin](127.0.0.1).
processSourcer | Script which gets the results of lsof to help identify which user or process is responsible for the traffic in question. Ran from the CLI and output piped into a file for easy searching later. | Traffic flows were being dropped by upstream network access controls while no users were signed into the machine in question. Due to the upstream provider having loud dropping (client system notified), tools such as lsof and netstat did hold information pertinent to the data flow for any significant period of time.


## Ansible Playbooks
| Playbook              | Features | Purpose | External Citation/Collaboration |
:-------------         | ------------- | ------------- | -------------:
| [backupConfiguration](https://github.com/NetworkNick-io/Operations/blob/main/backupConfig.yml) |  Backup the running-configuration of Cisco network devices. | Create backups of running-configuration files to improve RPO in the event of device failure or replacement when ran systemically with a product like Ansible Tower. | - |
| [changeEnable](https://github.com/NetworkNick-io/Operations/blob/main/changeEnable.yml) | Changes the enable password on Cisco network devices. | Change the shared enable password when an employee leaves or transfers to another department or organization on a network which does not drop privledged users at the enable prompt on login. | - |
| [setupNTP](https://github.com/NetworkNick-io/Operations/blob/main/setupNTP.yml) | Configures NTP with MD5 keys on Cisco network devices. | Configure the routers and switches for a newly deployed NTP server or for when new NTP keys have to be deployed. | - |
| [resolv.conf](https://github.com/NetworkNick-io/Operations/blob/main/resolvCONF.yml) | Configure /etc/resolv.conf on hosts to enable DNS services. | Enable central DNS configuration control and functionality within a statically configured enclave that lacks general DHCP services. | [cdschr1](https://github.com/cdschr1) |
| [createLocalAdmin](https://github.com/NetworkNick-US/Operations/blob/main/createAdmin.yml) | Create a local administrator account on all Cisco network devices | Create or change the local fallback administrator account's password on all network devices. | - |
| [removeLocalAdmin](https://github.com/NetworkNick-US/Operations/blob/main/removeLocalAdmin.yml) | Remove local accounts on Cisco network devices | Removes local accounts of previously authorized users who no longer need or are granted access and saves the confiugration. | - |


## Requirements
[RFC 1925](https://datatracker.ietf.org/doc/html/rfc1925)
