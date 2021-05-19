import subprocess

a = str(input())
default = "8.8.8.8"

def do_query(target_dns, dns_record, type):
	dig_query = ["dig @" + target_dns + " "+ type + " " + dns_record + " +short"]
	s= subprocess.Popen(dig_query, shell=True, stdout=subprocess.PIPE).stdout
	output = s.readlines()
	return output


print("List of nameservers for "+a)

ns_record = do_query(default, a, "NS")
print(ns_record)

ns_record_ips = []

for i in ns_record:
	ns_ip = do_query(default, i.decode('utf-8').strip("\n"), "A")
	ns_ip = ns_ip[0].decode('utf-8').strip("\n")
	ns_record_ips.append(ns_ip)

print(ns_record_ips)


for i in ns_record_ips:
	print("\nQuerying Name server "+ i + "...............")
	mx_record = do_query(i, a, "MX")
	if len(mx_record) > 0:
		for i in mx_record:
			print(i.decode('utf-8').strip("\n"))
		break
