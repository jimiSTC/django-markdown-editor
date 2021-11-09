import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:stc-tess-db1' 
database = 'impresario' 
username = os.getenv("pyusername")
password = os.getenv("pyuser_db_pass")


#customer_no = '1119449'

#Sample select query
"""
cursor.execute("SELECT top 10 * from T_CUSTOMER where customer_no = %s ;" % customer_no) 
row = cursor.fetchone() 
while row: 
    print(row)
    row = cursor.fetchone()


def CustDet( cust_no):
    cursor.execute("SELECT top 10 * from T_CUSTOMER where customer_no = %s ;" % cust_no) 
    print(cursor)
    row = cursor.fetchone() 
    return row

def CustDet( cust_no):
    cursor.execute("SELECT top 10 * from T_CUSTOMER" ) 

    row = cursor.fetchall() 

    return row

def CustDet( cust_no):
    cursor.execute("SELECT top 10 * from T_CUSTOMER where customer_no = " + str(cust_no) ) 

    row = list(cursor.fetchall())

    return row
print( CustDet(customer_no))


def EmailLog():
    cursor.execute("SELECT loe.*, ord.customer_no FROM [impresario].[dbo].[T_LOG_ORDER_EMAIL] loe inner join impresario.dbo.T_ORDER ord on ord.order_no = loe.order_no where format_no  in (46, 47) and email_dt > getdate()-360 order by email_dt desc"  ) 
    emailResults = list(cursor.fetchall())
    return emailResults
"""

def Dashi2():
    #print("test.....................dashi")
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("EXEC [dbo].[LRP_STC_INTRANET_SALES_TODAY]")
    dashi2Results = list(cursor.fetchall())
    print(dashi2Results)
    #dashi2Resultsform = [dashi2Results]
    #dashi2Results[0][4][5] = round((dashi2Results[0][4][5]),2 )
    #dashi2Resultsform = dashi2Resultsform [0][ '%.2f' % elem for elem in dashi2Results ]
    #print(round((dashi2Resultsform[0][3][5]),2))
    cursor.close()
    cnxn.close()
    return dashi2Results


def Donation():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("EXEC [dbo].[LRP_STC_DONATIONS_TODAY]")
    dashiDonation = list(cursor.fetchall())
    print(dashiDonation)
    cursor.close()
    cnxn.close()
    return dashiDonation

