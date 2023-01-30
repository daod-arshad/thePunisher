import json

final = {"title":None,
	"meta":None,
	"HttpServer":None,
	"uncommonHeaders":None,
	"country":None,
	"xxssrotection":None,
	
	"port":None,
	"certificates":None,
	"heartbleed":None,
	
	"address":[],
	"domain":[],
	"name":[],
	"mname":[],
	"type":[],
	
	"emails":[],
	"hosts":[],
	
	"hostname":[],"text":[],
	"fqdn":[],
	
	"creation":None,
	"update":None,
	"expiry":None
	
		
	}



whatweb = open("whatweb.json","r")
data = json.load(whatweb)
print("What Web data")
print(data)
if data:
	final['title'] = data[1]['plugins']['Title']['string']
	print(data[1]['plugins']['Title']['string'])
	
	final['meta'] = data[1]['plugins']['MetaGenerator']["string"]
	print(data[1]['plugins']['MetaGenerator']["string"])
	
	final['httpserver'] = data[1]['plugins']['HTTPServer']["string"]
	print(data[1]['plugins']['HTTPServer']["string"])
	
	final['uncommonheaders'] = data[1]['plugins']['UncommonHeaders']['string']
	print(data[1]['plugins']['UncommonHeaders']['string'])
	
	final['country'] = data[1]['plugins']['Country']["string"]
	print(data[1]['plugins']['Country']["string"])
	
	final['xxssprotection'] = data[1]['plugins']['X-XSS-Protection']["string"]
	print(data[1]['plugins']['X-XSS-Protection']["string"])



ssl = open("ssl.json","r")
data = json.load(ssl)
print("\nSsl Data")
if "error" not in data["document"]:

	final['port'] = data["document"]["ssltest"]["@port"]
	print(data["document"]["ssltest"]["@port"])
	
	final['certificate'] = data["document"]["ssltest"]["certificates"]
	print(data["document"]["ssltest"]["certificates"])
	
	final['heartbleed'] = data["document"]["ssltest"]["heartbleed"]
	print(data["document"]["ssltest"]["heartbleed"])


try:
	srvrecords = open("srvrecords.json","r")
	data = json.load(srvrecords)
	print("\n Srv Data")
	for i in range(1,len(data)):
		try:
			print(data[i]['address'])
			final['address'].append(data[i]['address'])
		except:
			print()
		try:
			print(data[i]['domain'])
			final['domain'].append(data[i]['domain'])
		except:
			print()
		try:
			print(data[i]['mname'])
			final['mname'].append(data[i]['mname'])
		except:
			try:
				print(data[i]['name'])
				final['name'].append(data[i]['name'])
			except:
				print("No value")
				
		print(data[i]['type'])
		final['type'].append(data[i]['type'])
		print()
except:
	print()
	
harvester = open("harvester.json","r")
data = json.load(harvester)
if data['theHarvester'] != None:
	try:
		print(data['theHarvester']['email'])
		final['emails'] = data['theHarvester']['email']
		
	except:
		print()
	try:
		print(data['theHarvester']['host'])
		final['hosts'] = data['theHarvester']['host']
	except:
		print()

dnsenum = open("dnsenum.json","r")
data = json.load(dnsenum)
print("\nDnsEnum Output:\n")
try:
	print(data["root"]["magictree"]["testdata"]["host"]["hostname"])
	final['hostname'].append(data["root"]["magictree"]["testdata"]["host"]["hostname"])
	final['text'].append(data["root"]["magictree"]["testdata"]["host"]["#text"])
	
except:
	lst = data["root"]["magictree"]["testdata"]["host"]
	for obj in lst:
		print(obj["hostname"])
		print(obj["#text"])
		final['hostname'].append(obj['hostname'])
		final['text'].append(obj["#text"])
try:
	print()
	data["root"]["magictree"]["testdata"]["fqdn"]
	final['hostname'].append(data["root"]["magictree"]["testdata"]["fqdn"])
	
except:
	lst = data["root"]["magictree"]["testdata"]["fqdn"]
	for obj in lst:
		print(obj)
		final['fqdn'].append(obj)

whois = open("whois.txt","r")
lines = whois.readlines()
if len(lines)<8:
	print("No whois record")
else:
	print()
	print(lines[4])
	final['creation'] = lines[4]
	print(lines[5])
	final['update'] = lines[5]
	print(lines[6])
	final['expiry'] = lines[6]

print(final)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
