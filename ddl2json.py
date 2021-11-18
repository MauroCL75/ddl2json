#!/usr/bin/python3

import sys
import json
import cx_Oracle
from q import *

dsn = sys.argv[1]
db = cx_Oracle.connect(dsn)
cursor = db.cursor()
cursor2 = db.cursor()

def getTabs():
    '''Get tables'''
    tabs = []
    cursor.execute(qtabs)
    for data in cursor:
        tabs.append(data[0])
    return tabs

def getCols(atab):
    '''get Cols from atab'''
    cols = []
    cursor.execute(qcols, [atab])
    for data in cursor:
        dcol = {"name": data[0], "type": data[1], "length": data[2]}
        cols.append(dcol)
    return cols

def getIndexes(atab):
    indexes = []
    cursor.execute(qindexes, [atab])
    for data in cursor:
        didx = {"name": data[0], "type": data[1], 
            "unique": data[2], "status": data[3], "ddl": ""}
        cursor2.execute(ddlQuery%(plurals['INDEX'], 'INDEX'), ["INDEX", data[0]])
        for outdata in cursor2:
            out = outdata[0]
            didx["ddl"] = out
        indexes.append(didx)
    return indexes

def getDDL(name, aType):
    ddl = ""
    aType = aType.upper()
    cursor.execute(ddlQuery%(plurals[aType], aType), [aType, name])
    for outdata in cursor:
        ddl = outdata[0]
    return ddl

def main():
    '''main'''
    tables = []
    indexes = []
    tabs = getTabs()
    for tab in tabs:
        atab = {"table": tab}
        atab["columns"] = getCols(tab)
        atab["ddl"] = getDDL(tab, "TABLE")
        tables.append(atab)
        idxs = getIndexes(tab)
        atab["index"] = idxs
    out = json.dumps(tables, sort_keys=True, indent=4)
    print(out)
        

if __name__ == "__main__":
    main()
