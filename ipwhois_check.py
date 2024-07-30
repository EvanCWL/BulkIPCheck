from ipwhois import IPWhois
import json
from collections import defaultdict
 
# method to get country and owner of IP
def get_info_ip(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_whois()
        country = result['asn_country_code']
        owner = result['asn_description']
        city = result['nets'][0]['city'] if result['nets'] and 'city' in result['nets'][0] else "Unknown City"
        return country, owner, city
    except Exception as e:
        return f"Error: {e}", None, None
 
with open('whois_input.txt', 'r') as file:
    ip_addresses = [line.strip() for line in file]
 
country_ip_mapping = defaultdict(list)

for ip in ip_addresses:
    country, owner, city = get_info_ip(ip)
    
    # Provide default values if any field is null or if an error occurred
    country = country if country else "Unknown Country"
    owner = owner if owner else "Unknown Owner"
    city = city if city else "Unknown City"
    
    entry = {"ip": ip, "owner": owner, "city": city}
    country_ip_mapping[country].append(entry)
 
with open('whois_output.txt','w') as f:
    print(json.dumps(country_ip_mapping, indent=4), file=f)
print(json.dumps(country_ip_mapping, indent=4))