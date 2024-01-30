==========

##This project is a python script used in daily work

###1. ssh_thread.py is a script for batch execution of commands. It supports direct execution of ssh commands and file transfer, and supports multi-threading.

Instructions for use are as follows:

-h,-H,--help help page
    -C, --cmd execution command mode
    -M, --command execute command mode
    -S, --sendfile transfer file mode
    -L, --localpath local file path
    -R, --remotepath remote server path

    IP list format:

    IP address Username Password Port
    192.168.1.1 root 123456 22

  e.g.
          Batch execution command format: -C "IP list" -M 'Executed command'
          Batch transfer files: -S "IP list" -L "local file path" -R "remote file path"
    Error log file: $PWD/ssh_errors.log

###2. check_ping.py detects ping in multiple processes and gets the value

By default, 4 processes are enabled. You need to put the hosts.txt IP list file into the same directory. The IP list is one per line. Domain names and IPs are supported.

###3. check_ip138.py Detects the IP (domain name) location through ip138

Usage: python check_ip138.py 192.168.1.1

###4. vps_baidu.py Use baidupan to back up VPS

pip install baidupan

Reference: http://solos.github.io/baidupan/

		使用方法: python check_ip138.py  192.168.1.1
	
	
	
	
###4. vps_baidu.py  使用baidupan备份VPS

		pip install baidupan
	
参考：http://solos.github.io/baidupan/