import re
 
# Input TXT file path
log_file_path = r"C:\Users\Mani\Desktop\example.txt"
 
# Output file path
output_file_path = r"C:\Users\Mani\Desktop\source_ips_with_traffic.txt"
 
# Target destination IP
target_dstip = "167.103.71.130"
 
# Dictionary to store srcip and its sent/received bytes
ip_traffic = {}
 
# Read and process each line
with open(log_file_path, 'r', encoding='utf-8') as file:
for log_line in file:
match = re.search(r'srcip=(\S+).*?dstip=(\S+).*?sentbyte=(\d+).*?rcvdbyte=(\d+)', log_line)
if match:
src_ip, dst_ip, sent_byte, rcvd_byte = match.groups()
if dst_ip == target_dstip and int(sent_byte) > 0:
if src_ip not in ip_traffic:
ip_traffic[src_ip] = {'sent': 0, 'rcvd': 0}
ip_traffic[src_ip]['sent'] += int(sent_byte)
ip_traffic[src_ip]['rcvd'] += int(rcvd_byte)
 
# Write results to output file
with open(output_file_path, 'w') as out_file:
for ip, traffic in sorted(ip_traffic.items()):
out_file.write(f"{ip} : Sent = {traffic['sent']} bytes, Received = {traffic['rcvd']} bytes\n")
 
# Print results
print(f"Source IPs communicating with {target_dstip}:")
for ip, traffic in sorted(ip_traffic.items()):
print(f"{ip} : Sent = {traffic['sent']} bytes, Received = {traffic['rcvd']} bytes")
 
 
 
 
 #####################################sent#######################################################
 

 
import re
 
# Input TXT file path
log_file_path = r"C:\Users\Mani\Desktop\example.txt"
 
# Output file path
output_file_path = r"C:\Users\Mani\Desktop\source_ips_with_bytes.txt"
 
# Target destination IP
target_dstip = "167.103.71.130"
 
# Dictionary to store srcip and sentbyte
ip_sentbytes = {}
 
# Read and process each line
with open(log_file_path, 'r', encoding='utf-8') as file:
for log_line in file:
match = re.search(r'srcip=(\S+).*?dstip=(\S+).*?sentbyte=(\d+)', log_line)
if match:
src_ip, dst_ip, sent_byte = match.groups()
if dst_ip == target_dstip and int(sent_byte) > 0:
ip_sentbytes[src_ip] = ip_sentbytes.get(src_ip, 0) + int(sent_byte)
 
# Write results to output file
with open(output_file_path, 'w') as out_file:
for ip, bytes_sent in sorted(ip_sentbytes.items()):
out_file.write(f"{ip} : {bytes_sent} bytes\n")
 
# Print results
print(f"Source IPs sending data to {target_dstip}:")
for ip, bytes_sent in sorted(ip_sentbytes.items()):
print(f"{ip} : {bytes_sent} bytes")
