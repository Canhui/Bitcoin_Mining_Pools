import sys
import json
import requests
import time
from pymongo import MongoClient
import commands


'''Database Configuration'''
conn = MongoClient('127.0.0.1', 27017)
db = conn.dbminingpool  
my_set = db.dbminingpoolset
my_set.drop() 


'''MiningPool() Function'''
def MiningPool(beginblockid, endblockid):
	counter = 0;
	for blockid in range(beginblockid, endblockid):
		try:
			url = 'https://chain.api.btc.com/v3/block/%s' % blockid
			webpage = requests.get(url)
			blockjson = json.loads(webpage.text)
			print blockjson['data']['extras']['pool_name']
			my_set.insert({"blockid":blockid, "miningpool":blockjson['data']['extras']['pool_name']})
		except:
			pass

		time.sleep(3);

		counter = counter + 1
		if counter > 50:
			counter = 0;
			try:
				(status, output) = commands.getstatusoutput("sudo mongoexport -d dbminingpool -c dbminingpoolset -f blockid,miningpool --csv -o miningpool.csv")
			except:
				pass
	try:
		(status, output) = commands.getstatusoutput("sudo mongoexport -d dbminingpool  -c dbminingpoolset -f blockid,miningpool --csv -o miningpool.csv")
	except:
		pass


'''Main() Function'''	
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Errors Inputs.\n";
	else:
		MiningPool(int(sys.argv[1]), int(sys.argv[2]))