# OperationalItems
A collection of frequently used scripts and playbooks. This collection contains both Python and Ansible scripts that have found various uses within my personal or professional roles. Variable files are not included in this repo.

## Python Scripts

Script              | Features | Purpose
:-------------         | ------------- | -------------
[icmpMonitor](https://github.com/NetworkNick-io/Operations/tree/main/ICMPmonitor) |  Basic ICMP monitoring script for use in small isolated environments. | Created for non-network administrators or power-users to improve situational awarness when other monitoring tools (SolarWinds, Nagios, etc.) are not available.

## Ansible Playbooks
Playbook              | Features | Purpose
:-------------         | ------------- | -------------
[backupConfiguration](https://github.com/NetworkNick-io/Operations/blob/main/backupConfig.yml) |  Backup the running-configuration of Cisco network devices. | Create backups of running-configuration files to improve RPO times in the event of device failure or replacement.
[changeEnable](127.0.0.1) | Changes the enable password on Cisco network devices. | Change the shared enable password when an employee leaves or transfers to another department or organization on a network which does not drop privledged users at the enable prompt on login.
[setupNTP](127.0.0.1) | Configures NTP with MD5 keys on Cisco network devices. | Configure the routers and switches for a newly deployed NTP server or for when new NTP keys have to be deployed.
[resolv.conf](127.0.0.1) | Configure /etc/resolv.conf on hosts to enable DNS services. | Enable central DNS configuration control and functionality within a statically configured enclave that lacks general DHCP services. 
