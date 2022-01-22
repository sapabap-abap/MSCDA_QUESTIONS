import sqlite3 as sql
from prettytable import  PrettyTable
from pathlib import Path

# final result list
final_result = []
#connect to db
dbfile = Path('student.db')
connection = sql.connect(dbfile)
#get cursor
cursor = connection.cursor()
cursor.execute(f'select student_id from student order by student_name;')
result = cursor.fetchall( )
result_list = []
for row in result:
    row = list(row)
    result_list.append(row)
result_list = sorted(result_list,key=lambda x:x[0])
for item in result_list:
    select_query = (
              "SELECT  student.student_name as name ,"
                       "result.course,"
			           "avg(result.points)"
			 " FROM result"
              " INNER JOIN student on student.student_id  = result.student_id"
              " WHERE result.student_id = {}"
              " GROUP BY result.course;").format(item[0] )
    cursor.execute(select_query)
    avg_list = cursor.fetchall()
    for row in avg_list:
        row = list(row)
        row[1]=row[1][:4]
        row[2] = '{0:.5f}'.format(row[2])
        final_result.append(row)
        final_result  = sorted(final_result, reverse = False,key=lambda x: (x[0].strip(),x[1].strip()))
#close connection
connection.close()

def print_list(list):
    t = PrettyTable()
    t.field_names = ["Name", "Subject", "avg(points)"]
    t.add_rows(list)
    print(t)

#display table
print_list(final_result)

