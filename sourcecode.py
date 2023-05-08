#!/usr/local/bin/python3
import cgi
import json
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    """DiseaseAllianceCombined"""
    query = "SELECT * FROM DiseaseAllianceCombined"

    if not query:
        query = "Doesn't Exist"

    connection = mysql.connector.connect(user='amatias1', password='password', host='localhost',
                                         database='amatias1')
    cursor = connection.cursor()

    query_values = {'count': 0, 'values': list()}

    if query in ['gene_term', 'protein_term']:
        if query == 'gene_term':
            query = """
                  SELECT SpeciesName, DBObjectSymbol, DOtermName
                      FROM DiseaseAllianceCombined
                      WHERE DOtermName LIKE %s
            """
            cursor.execute(query, ('%' + term + '%',))

            for (SpeciesName, DBObjectSymbol, DOtermName) in cursor:
                query_values['values'].append(
                    {'SpeciesName': SpeciesName, 'DBObjectSymbol': DBObjectSymbol, 'DOtermName': DOtermName})
                query_values['count'] += 1

    connection.close()
    return jsonify(query_values)


if __name__ == '__main__':
    app.run(debug=True)
