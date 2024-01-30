#!/usr/bin/python3
# coding:utf-8
from urllib.request import urlopen
import re
import sys


def is_ip(s):
    return len([i for i in s.split('.') if 0 <= int(i) <= 255]) == 4


def url(ip):
    uip = urlopen('http://wap.ip138.com/ip.asp?ip=%s' % ip)
    fip = uip.read().decode('utf-8')
    rip = re.compile(r"<br/><b>search result：(.*)</b><br/>")
    result = rip.findall(fip)
    print("%s\t %s" % (ip, result[0]))


def do(domain):
    url = urlopen('http://wap.ip138.com/ip.asp?ip=%s' % domain)
    f = url.read().decode('utf-8')
    r = re.compile(r'&gt; (.*)<br/><b>search result：(.*)</b><br/>')
    result = r.findall(f)
    for i in result:
        print("%s\t %s\t %s\t" % (domain, i[0], i[1]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter IP address or domain name (For example: 192.168.1.1 / www.baidu.com)")
        sys.exit()
    input_value = sys.argv[1]
    if not re.findall(r'(\d{1,3}\.){3}\d{1,3}', input_value):
        if re.findall(r'(\w+\.)?(\w+)(\.\D+){1,2}', input_value):
            domain = input_value
            do(domain)
        else:
            print("The entered IP address and domain name are in the wrong format.！")
    else:
        if is_ip(input_value):
            ip_address = input_value
            url(ip_address)
        else:
            print("IP The address is invalid, please re-enter!")
