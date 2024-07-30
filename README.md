**Bulk IP Checker**
====================

This project contains two Python scripts, `abuseipdb_check.py` and `ipwhois_check.py`, designed to perform bulk IP checks using AbuseIPDB and IPWhois APIs.

**Usage**
--------

To use these scripts, simply create a text file containing the IPs you want to check, one IP per line.

### AbuseIPDB Check

| File | Description |
|------|-------------|
| `abuseipdb_input.csv` | Input file containing IPs to check, one IP per line |
| `config.json` | Configuration file containing AbuseIPDB API key |

* Create a file named `abuseipdb_input.csv` with the IPs you want to check, one IP per line.
* Create a JSON file named `config.json` with the following format:
```json
{
    "api_key": "YOUR_ABUSEIPDB_API_KEY"
}
```
Replace `YOUR_ABUSEIPDB_API_KEY` with your actual AbuseIPDB API key.

Run `abuseipdb_check.py` to perform the bulk IP check.

### IPWhois Check

| File | Description |
|------|-------------|
| `whois_input.txt` | Input file containing IPs to check, one IP per line |

Create a file named `whois_input.txt` with the IPs you want to check, one IP per line.
Run `ipwhois_check.py` to perform the bulk IP check.

### Example Input Files

The input files should contain one IP per line, like this:

#### abuseipdb_input.csv / whois_input.txt:
```
1.1.1.1
2.2.2.2
3.3.3.3
```
