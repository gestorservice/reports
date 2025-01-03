from flask import Flask, render_template
from mysqlclient import mysqlclient
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos en Clever Cloud
app.config['MYSQL_HOST'] = 'b0cz6x9ivpg9ua0652et-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uiivhxgwuesw7ysh'
app.config['MYSQL_PASSWORD'] = 'htPUWO3XpmGyxg7JhIlT'
app.config['MYSQL_DB'] = 'b0cz6x9ivpg9ua0652et'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        # Conexión y consulta a la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM service")
        datos = cursor.fetchall()
        return render_template('index.html', datos=datos)
    except Exception as e:
        return f"Error de conexión: {str(e)}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
