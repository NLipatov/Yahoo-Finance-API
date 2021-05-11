import ibm_db
import pandas
import ibm_db_dbi
import pprint

#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "dashdb-txn-sbox-yp-lon02-13.services.eu-gb.bluemix.net" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "bgj57941"        # e.g. "abc12345"
dsn_pwd = "xpqn4zxkhk@cczw5"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
#print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print("Unable to connect: ", ibm_db.conn_errormsg() )
server = ibm_db.server_info(conn)

#print ("DBMS_NAME: ", server.DBMS_NAME)
#print ("DBMS_VER:  ", server.DBMS_VER)
#print ("DB_NAME:   ", server.DB_NAME)
client = ibm_db.client_info(conn)


#print ("DRIVER_NAME:          ", client.DRIVER_NAME)
#print ("DRIVER_VER:           ", client.DRIVER_VER)
#print ("DATA_SOURCE_NAME:     ", client.DATA_SOURCE_NAME)
#print ("DRIVER_ODBC_VER:      ", client.DRIVER_ODBC_VER)
#print ("ODBC_VER:             ", client.ODBC_VER)
#print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
#print ("APPL_CODEPAGE:        ", client.APPL_CODEPAGE)
#print ("CONN_CODEPAGE:        ", client.CONN_CODEPAGE)


# def SQLq(Query):
#     pconn = ibm_db_dbi.Connection(conn)
#     try:
#         df = pandas.read_sql("""%s""" % (Query), pconn)
#     except:
#         print('ERROR at SQLq function')
#         ibm_db.close( conn )
#         print( '\n\n\nClosing Connection Now' )
def cc():
    ibm_db.close(conn)
    print( '\n\n\nClosing Connection Now' )
#
#
# print(SQLq("""insert into IP
#     (RECORDID, USD_VALUE, RUB_VALUE, DATE_AND_TIME)
#     Values
#     (1, 2, 3, 4)"""))
def command(statement):
    # pconn = ibm_db_dbi.Connection(conn)
    stmnt = ibm_db.exec_immediate(conn, statement)
    try:
        print("ВЫВОД СИСТЕМЫ IBM: " + str(ibm_db.fetch_both(stmnt)))
    except:
        print("Успешно или вывод не может быть получен.")
    cc()
def LastRowInIP():
    sql = "SELECT COUNT(RecordID) FROM ip"
    stmt = ibm_db.prepare(conn, sql,{ibm_db.SQL_ATTR_CURSOR_TYPE: ibm_db.SQL_CURSOR_KEYSET_DRIVEN})
    result = ibm_db.execute(stmt)
    row = ibm_db.fetch_assoc(stmt)
    if row.get('1') == None:
        return 0
    else:
        return row.get('1')
    cc()


# command("""insert into IP
#     (RECORDID, USD_VALUE, RUB_VALUE, DATE_AND_TIME)
#     Values
#     (4, 2, 3, 4)""")

