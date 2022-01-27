# OperationalItems
A collection of frequently used scripts and playbooks. This collection contains both Python and Ansible scripts that have found various uses within my personal or professional roles. Variable files are not included in this repo.

## Python Scripts

Script              | Features | Purpose
:-------------         | ------------- | -------------
[icmpMonitor](https://github.com/NetworkNick-io/Operations/tree/main/ICMPmonitor) |  Basic ICMP monitoring script for use in small isolated environments. | Created for non-network administrators or power-users to improve situational awarness when other monitoring tools (SolarWinds, Nagios, etc.) are not available.

## Ansible Playbooks
Playbook              | Features | Purpose | External Citation/Collaboration
:-------------         | ------------- | ------------- | -------------:
[backupConfiguration](https://github.com/NetworkNick-io/Operations/blob/main/backupConfig.yml) |  Backup the running-configuration of Cisco network devices. | Create backups of running-configuration files to improve RPO in the event of device failure or replacement when ran systemically with a product like Ansible Tower. | -
[changeEnable](https://github.com/NetworkNick-io/Operations/blob/main/changeEnable.yml) | Changes the enable password on Cisco network devices. | Change the shared enable password when an employee leaves or transfers to another department or organization on a network which does not drop privledged users at the enable prompt on login. | -
[setupNTP](https://github.com/NetworkNick-io/Operations/blob/main/setupNTP.yml) | Configures NTP with MD5 keys on Cisco network devices. | Configure the routers and switches for a newly deployed NTP server or for when new NTP keys have to be deployed. | -
[resolv.conf](https://github.com/NetworkNick-io/Operations/blob/main/resolvCONF.yml) | Configure /etc/resolv.conf on hosts to enable DNS services. | Enable central DNS configuration control and functionality within a statically configured enclave that lacks general DHCP services. | [cdschr1](https://github.com/cdschr1)
createLocalAdmin | Create a local administrator account on all Cisco network devices | Create or change the local fallback administrator account's password on all network devices. | -
