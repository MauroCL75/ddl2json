#!/usr/bin/python3
import sys
import json

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

json1 = json.load(f1)
json2 = json.load(f2)

f1.close()
f2.close()

def getTables(jdata):
    tables = []
    for data in jdata:
        tables.append(data["table"])
    tables.sort()
    return tables

def getColumns(atable, jdata):
    columns = []
    #for data in 
    for data in jdata:
        if data["table"] == atable:
            cols = data["columns"]
            for col in cols:
                columns.append("%s_%s_%s"%(col["name"], col["type"], col["length"]))
    columns.sort()
    #print(atable, columns)
    return columns

def getIndexes(atable, jdata):
    indexes = []
    for data in jdata:
        if data["table"] == atable:
            idxs = data["index"]
            for idx in idxs:
                indexes.append(idx["name"])
    return indexes

def showDDL(aType, aSet, jData):
    aType = aType.upper()
    for jElem in jData:
        if aType == "INDEX":
            for idx in jElem[aType.lower()]:
                if idx["name"] in aSet:
                    print("--DDL %s"%(idx["name"]))
                    print(idx["ddl"])
                    print("--END DDL")
                    print()
    

def main():
    table1 = getTables(json1)
    table2 = getTables(json2)

    if table1 != table2:
        print("Missing table(s):")
        diff1 = set(table2) - set(table1)
        diff2 = set(table1) - set(table2)
        print("%s: %s| %s: %s"%(sys.argv[1], diff1, sys.argv[2], diff2))
    
    for tab in table2:
        if tab in table1:
            #print(tab)
            col1 = getColumns(tab, json1)
            col2 = getColumns(tab, json2)
            idx1 = getIndexes(tab, json1)
            idx2 = getIndexes(tab, json2)
            #print(tab, col1)
            #print(tab, col2)
            if col1 != col2:
                print("Missing column(s) on %s: "%(tab))
                diff2 = set(col2) - set(col1)
                diff1 = set(col1) - set(col2)
                print("%s: %s| %s: %s"%(sys.argv[1], diff1, sys.argv[2], diff2))
            if idx1 != idx2:
                print("Missing index(es) on %s: "%(tab))
                diff2 = set(idx2) - set(idx1)
                diff1 = set(idx1) - set(idx2)
                print("%s: %s| %s: %s"%(sys.argv[2], diff1, sys.argv[1], diff2))
                showDDL("index", diff1, json1)
                showDDL("index", diff2, json2)

if __name__ == "__main__":
    main()
