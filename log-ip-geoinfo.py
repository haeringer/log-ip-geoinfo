import argparse
import glob
import sys
import re
import subprocess

from ip2geotools.databases.noncommercial import MaxMindGeoLite2City

DB_PATH = 'databases/GeoLite2-City.mmdb'

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='?', default=None)
args = parser.parse_args()

if args.arg:
    filename = args.arg
else:
    print('Please enter log file path as argument.')
    sys.exit(1)


def open_file_and_return_as_set(filename):
    print('Importing file contents...')
    access_log = set()

    with open(filename, 'r') as f:
        for line in f:
            access_log.add(line)
    return access_log


def filter_for_ip_addresses(access_log):
    print('Filter for IP addresses...')
    ip_list = []

    for line in access_log:
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
        try:
            ip_list.append(ip[0])
        except Exception:
            pass
    return sorted(set(ip_list))


def query_geoip_database(ip_set):
    print('Query whois database with IP addresses', end='', flush=True)

    with open('output.txt', 'w') as file_:
        for entry in ip_set:
            try:
                response = MaxMindGeoLite2City.get(entry, db_path=DB_PATH)
                file_.write(response.to_json() + '\n')
                print('.', end='', flush=True)
            except Exception as e:
                print('Invalid: ' + str(e), end='', flush=True)


access_log = open_file_and_return_as_set(filename)
ip_set = filter_for_ip_addresses(access_log)
query_geoip_database(ip_set)
