#!/usr/local/bin/python3

import cgi
import os
import mysql
import mysql.connector
import json


def main():
    print("Content-Type: application/json")
    form = cgi.FieldStorage()
    term = form.getvalue('search_input')

    connection = mysql.connector.connect(user='amatias1', password='password', host='localhost',
                                         database='FinalProject')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT SpeciesName, DBObjectSymbol, DOtermName FROM DiseaseAllianceCombined WHERE DOtermName LIKE '%"+term+"%'")

    query_values = {'count': 0, 'values': list()}
    for (SpeciesName, DBObjectSymbol, DOtermName) in cursor:
                query_values['values'].append(
                    {'SpeciesName': SpeciesName, 'DBObjectSymbol': DBObjectSymbol, 'DOtermName': DOtermName})
                query_values['count'] += 1

    connection.close()

    print(json.dumps(query_values))

if __name__ == '__main__':
    main()
