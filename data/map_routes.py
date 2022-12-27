import json
import os

def main():
    dic = {}
    cwd = os.getcwd()
    fileNames = os.listdir(cwd + '/yangon_bus_routes')
    
    
    for fileName in fileNames:
        f = open(cwd + '/yangon_bus_routes/' + fileName);
        data = json.load(f)
        dic[fileName.replace('.json', '')] = data
    
    
    # json_object = json.dumps(dic, indent=4)
    with open("yangon_bus_routes.json", "w") as outfile:
        json.dump(dic, outfile)
main()
