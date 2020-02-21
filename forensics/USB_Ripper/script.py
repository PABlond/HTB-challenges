import multiprocessing
import urllib3
import json
import requests
import extract
import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Compare:
    def __init(self):
        self.manufacts = []
        self.manufacts_s = []
        self.serials = []
        self.serials_s = []
        self.result = None

    def extract_json(self):
        json_filename = "auth.json"
        with open(json_filename) as json_file:
            data = json.load(json_file)
        self.manufacts = data["manufact"]
        self.serials = data["serial"]

    def extract_file(self, filename) -> str:
        with open(filename, "r") as f:
            lines = [x.replace("\n", "") for x in f.readlines()]
        return lines

    def extract_syslog(self):
        self.manufacts_s = self.extract_file(
            filename=config.manufacturer_filename)
        self.serials_s = self.extract_file(filename=config.serial_filename)

    def process_manufact(self, manufact):
        if not manufact in self.manufacts:
            crack_hash(hashvalue=manufact)

    def process_serial(self, serial):
        if not serial in self.serials:
            crack_hash(hashvalue=serial)

    def run(self):
        self.result = ""
        treads_n = multiprocessing.cpu_count()
        p = multiprocessing.Pool(treads_n)
        print("[] Looking for unexpect manufacturer ...")
        p.map(self.process_manufact, self.manufacts_s)
        print("[] Looking for unexpect serials ...")
        p.map(self.process_serial, self.serials_s)
        p.close()


def crack_hash(hashvalue):
    """
    This is not a real crack function !
    We will just make a GET request to "nitrxgen" API
    """
    url = "https://www.nitrxgen.net/md5db/{}"
    r = requests.get(url.format(hashvalue), verify=False)
    if len(r.text) > 0:
        print("\033[4m Flag is: HTB{" + r.text + "} \033[0m")
    else:
        print('Flag not found')


def main():
    print('[] Extracting data from syslog ...')
    extract.run()
    c = Compare()
    c.extract_json()
    c.extract_syslog()
    c.run()

if __name__ == '__main__':
    main()
