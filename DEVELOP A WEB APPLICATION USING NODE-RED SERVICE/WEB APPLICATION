import ibm_db


hostname="2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
uid="dzg81413"
pwd="dZ19uS8WcguF832s"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30756"
protocol="TCPIP"
cert="Certificate.crt"
dsn=(
     "DATABASE={0};"
     "HOSTNAME={1};"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "PWD={5};"
     ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to data base")
except:
    print("Unable to connect",ibm_db.conn_errormsg())
