import csv
import gzip


def creatingCSV(row):
	fobj = open("metadata2CSV.csv", "a")
	try:
		productId = row["asin"]
		category = row["salesRank"].keys()[0]
		writer = csv.writer(fobj)
		writer.writerow(( productId, category))
	except:
		pass
	finally:
		fobj.close()


def parse(path): 
	g = gzip.open(path, 'r') 
	for l in g: 
		yield (eval(l)) 
 

if __name__ == "__main__":
	
	for row in parse("metadata.json.gz"): 
		creatingCSV(row)