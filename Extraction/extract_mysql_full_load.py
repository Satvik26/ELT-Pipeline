import pymysql
import csv
import boto3
import configparser

# load the MySQL database credentials values

parser = configparser.ConfigParser()
parser.read("pipeline.conf")

hostname = parser.get("mysql_config","hostname")
port = parser.get("mysql_config","port")
username = parser.get("mysql_config","username")
dbname = parser.get("mysql_config","database")
password = parser.get("mysql_config","password")

# load the aws_boto_credentials values
access_key = parser.get("aws_boto_credentials","access_key")
secret_key = parser.get("aws_boto_credentials","secret_key")
bucket_name = parser.get("aws_boto_credentials","bucket_name")

#Connection with the MySQL instance

try:
    cur = None
    conn = None
    conn = pymysql.connect(host = hostname, user = username, password = password, db = dbname, port = int(port))
    print("MySQL connection established")

    m_query = "SELECT * FROM Orders;"
    local_filename = "order_extract.csv"

    cur = conn.cursor()
    cur.execute(m_query)

    results = cur.fetchall()
    print(results)
    with open(local_filename,'w') as fp:
       csv_w = csv.writer(fp)
       csv_w.writerow(('OrderId','OrderStatus','LastUpdated'))
       csv_w.writerows(results)

except Exception as e:
    print(f"Error connecting to the MySQL databas/n{e}")

finally: 
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()


# Connection with S3 Bucket
try:
    s3 = boto3.client('s3',aws_access_key_id = access_key, aws_secret_access_key = secret_key)
    #Fetching csv file
    s3_file = local_filename
    s3.upload_file(local_filename, bucket_name, s3_file)
except Exception as e:
    print(e)


    





