#!/usr/local/bin/python3

import cgi
import os
import mysql
import mysql.connector
import json


def main():
    form = cgi.FieldStorage()
    term = form.getvalue('search_input')

    if form.getvalue('query'):
        query = form.getvalue('query')
    else:
        query = "Doesn't Exist"

    connection = mysql.connector.connect(user='amatias1', password='password', host='localhost',
                                         database='amatias1')
    cursor = connection.cursor()

    if query in ['gene_term', 'protein_term']:
        if query == 'gene_term':
            query = """
                  SELECT SpeciesName, DBObjectSymbol, DOtermName
                      FROM DiseaseAllianceCombined
                      WHERE DOtermName LIKE %s
            """
            cursor.execute(query, ('%' + term + '%',))

            query_values = {'count': 0, 'values': []}
            for (SpeciesName, DBObjectSymbol, DOtermName) in cursor:
                query_values['values'].append(
                    {'SpeciesName': SpeciesName, 'DBObjectSymbol': DBObjectSymbol, 'DOtermName': DOtermName})
                query_values['count'] += 1

    connection.close()

    print("Content-Type: application/json")
    print()
    print(json.dumps(query_values))

if __name__ == '__main__':
    main()
