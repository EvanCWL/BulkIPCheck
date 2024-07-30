import csv
import requests
import json
import os
import time
import math
import urllib3

def bulk_check(csv_path, api_key, export_path):
    try:
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            total_rows = sum(1 for row in csv_reader)
            file.seek(0)

            with open(export_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["ipAddress", "abuseConfidenceScore", "isp", "domain", "countryCode", "totalReports", "lastReportedAt"])
                for i, row in enumerate(csv_reader):
                    ip = row[0]

                    response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}", headers={'Accept': 'application/json', 'Key': api_key}, verify=False)

                    if response.status_code == 200:
                        data = response.json()["data"]
                        csv_writer.writerow([data["ipAddress"], data["abuseConfidenceScore"], data["isp"], data["domain"], data["countryCode"], data["totalReports"], data["lastReportedAt"]])
                    else:
                        print(f"{ip} is not a valid IP! {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    with open('.\config.json') as f:
        config = json.load(f)
    input = r'.\abuseipdb_input.csv'
    api_key = config['api_key']
    output = r'.\abuseipdb_output.csv'
    bulk_check(input, api_key, output)

if __name__ == "__main__":
    main()