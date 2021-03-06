
plurals = {"INDEX": "INDEXES", "TABLE":"TABLES", "COLUMN": "COLUMNS"}

qtabs="""
    SELECT table_name from user_tables order by 1 
"""

qcols="""
    SELECT COLUMN_NAME, DATA_TYPE, DATA_LENGTH 
    from user_tab_columns COLUMN_ID where table_name = :1
"""

qindexes="""
    SELECT INDEX_NAME, INDEX_TYPE, UNIQUENESS, STATUS 
    from USER_INDEXES 
    where table_name = : 1 order by 1
"""

qviews="""
    SELECT VIEW_NAME from user_views
"""

qsequences="""
    SELECT SEQUENCE_NAME, MIN_VALUE, MAX_VALUE, CACHE_SIZE, LAST_NUMBER
    from USER_SEQUENCES
"""

ddlQuery="""
    SELECT TO_CHAR(SUBSTR(DBMS_METADATA.get_ddl(:1, :2),0,3999))
    FROM USER_%s 
    WHERE %s_NAME=:2
""" ##TYPE, NAME
