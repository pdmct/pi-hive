import os
import sys_stats
import time
import pycurl, json
from urllib import urlencode


def on_receive(data):
        print data

STREAM_URL = "https://realtime.opensensors.io/v1/topics/%2Fusers%2Fpetermct%2Fcpu_temp?client-id="+os.environ['CLIENT_ID']+"&password="+os.environ['IO_PSWD']
headers = ["Content-Type: application/json","Accept: application/json","Authorization: api-key "+ os.environ['API_KEY']]

def postData():
        osConn = pycurl.Curl()
        osConn.setopt(osConn.URL, STREAM_URL)
        osConn.setopt(osConn.WRITEFUNCTION, on_receive)
        cpu_temp = sys_stats.getCPUtemperature()
        post_data = {}
        #post_data["data"] =  '"' + str(cpu_temp) + '"'
        post_data["data"] =  '{ "raw_value" : ' + str(cpu_temp) + ' }'

        osConn.setopt(osConn.HTTPHEADER, headers)
        osConn.setopt(osConn.POSTFIELDS, json.dumps(post_data))
        osConn.perform()
        osConn.close()


if __name__ == "__main__":

        while True:
                postData()
                time.sleep(5)

