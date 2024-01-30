#!/usr/bin/python3
#coding:utf-8
import datetime
import multiprocessing
import os
import re
import subprocess
import sys


def pinger(ip):
    cmd = 'ping -c 2 %s' % (ip.strip())
    ret = subprocess.getoutput(cmd)
    loss_re = re.compile(r"received, (.*) packet loss")
    packet_loss = loss_re.findall(ret)[0]
    rtt_re = re.compile(r"rtt min/avg/max/mdev = (.*) ")
    rtts = rtt_re.findall(ret)
    rtt = rtts[0].split('/')
    rtt_min = rtt[0]
    rtt_avg = rtt[1]
    rtt_max = rtt[2]
    print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (ip, packet_loss, rtt_min, rtt_max, rtt_avg))


if __name__ == "__main__":
    if not os.path.exists("hosts.txt"):
        print("hosts.txt - File does not exist, please try again")
        sys.exit(1)

    now = datetime.datetime.now()
    file = open('hosts.txt', 'r')
    pool = multiprocessing.Pool(processes=4)
    result = []
    print("######## %s ###########" % now)
    print("IPADDRSS\t\t\tLOSS\t\tMIN\t\tMAX\t\tAVG")
    for i in file.readlines():
        if len(i) == 1 or i.startswith("#"):
            continue
        result.append(pool.apply_async(pinger, (i.strip(),)))

    pool.close()
    pool.join()
