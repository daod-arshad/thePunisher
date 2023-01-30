import os, sys
import json
import xmltodict

def convertToJson(filename):
    with open(filename+".xml") as xml_file:     
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        json_data = json.dumps(data_dict)
    with open(filename+".json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()


#if len(sys.argv)>=2:
#	print()
#	print("Invalid hostname, Please make sure that the specified hostname is correct.")
#	print()

#else:
target = sys.argv[1]
#print("The target is: "+target)
	
#Tool number 1: The Harvester
print("Starting TheHarvester")
os.system("theHarvester -l 50 -b google -d "+target+" -f harvester > /dev/null")
convertToJson("harvester")
os.system("rm harvester.xml")

#Tool number 2: Host
	
	
	
#Tool number 3: Dnsrecon
print("Starting Dnsrecon")
os.system("dnsrecon -d "+target+" -j "+os.getcwd()+"/srvrecords.json > /dev/null")


#Tool number 4: whois
print("Starting whois")
os.system("whois "+target+" > whois.txt")
whois = open("whois.txt","r")
lines = whois.readlines()
if len(lines)<8:
	print("No whois record")
else:
	print()
	print(lines[4])
	print(lines[5])
	print(lines[6])
	
	
#Tool number 5: dnsenum
print("Starting dnsenum")
os.system(" dnsenum "+target+" -o dnsenum.xml > /dev/null")
xml = open("dnsenum.xml","r")
lst = xml.readlines()
lst.insert(1,"<root>")

#print(lst[len(lst) - 1][len(lst[len(lst)-1])-1:-23:-1])

if lst[len(lst) - 1][len(lst[len(lst)-1])-1:-24:-1] != '>eertcigam/<>atadtset/<':
	print('appending')
	lst.append("</testdata></magictree>")
lst.append('</root>')
xml.close()
xml = open("dnsenum.xml","w")
for lines in lst:
	xml.write(lines)
xml.close()

convertToJson("dnsenum")
os.system("rm dnsenum.xml")
try:
	os.system("rm nu.edu.pk_ips.txt")
except:
	print()

#Tool number 6: dmitry
print("starting dmitry")
os.system("dmitry -e "+target+" > dmitry.txt")

#Tool number 7: whatweb
print("Starting whatweb")
os.system("whatweb -a 1 "+target+" --log-json=whatweb.json > /dev/null")

#Tool number 8: sslscan
print("Starting sslscan")
os.system("sslscan --xml=ssl.xml "+target+" > /dev/null")
convertToJson("ssl")
os.system("rm ssl.xml")


os.system("python3 final.py")





	





















 

