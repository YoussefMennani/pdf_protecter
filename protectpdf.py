
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='pdfprotect',
                                         user='root',
                                         password='')



    mycursor = connection.cursor()

    nom="huhu"
    id=1
    
    mycursor.execute("UPDATE utilisateur SET nom='%s' WHERE id = %s" % (nom, id)) 

    connection.commit()

    print(mycursor.rowcount, "record(s) affected")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        mycursor.close()
        connection.close()
        print("MySQL connection is closed")