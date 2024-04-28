from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Datos de ejemplo para los productos de PC
productos_pc = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Monitor", "precio": 200},
    {"nombre": "Teclado", "precio": 50},
    {"nombre": "Mouse", "precio": 20},
    {"nombre": "Impresora", "precio": 150}
]

# Nombres de gente de Inglaterra
usuarios_inglaterra = [
    {"nombre": "John", "apellido": "Smith"},
    {"nombre": "Emily", "apellido": "Jones"},
    {"nombre": "William", "apellido": "Brown"},
    {"nombre": "Sophie", "apellido": "Taylor"},
    {"nombre": "James", "apellido": "Wilson"}
]

# Nombres de gente de Suecia
clientes_suecia = [
    {"nombre": "Erik", "apellido": "Larsson"},
    {"nombre": "Anna", "apellido": "Andersson"},
    {"nombre": "Karl", "apellido": "Johansson"},
    {"nombre": "Hanna", "apellido": "Nilsson"},
    {"nombre": "Olle", "apellido": "Pettersson"}
]

# Ruta para la página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))  # Redirige a index si ya ha iniciado sesión
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'root' and password == 'admin1':
            session['username'] = username
            return redirect(url_for('index'))  # Redirige a index si la autenticación es exitosa
        else:
            error = 'Usuario o contraseña incorrectos'
            return render_template('login.html', error=error)
    return render_template('login.html', error=None)

# Ruta para cerrar sesión
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Ruta para la página principal
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

# Ruta para mostrar los productos
@app.route('/productos')
def mostrar_productos():
    if 'username' in session:
        return render_template('productos.html', productos=productos_pc)
    return redirect(url_for('login'))

# Ruta para mostrar los usuarios
@app.route('/usuarios')
def mostrar_usuarios():
    if 'username' in session:
        return render_template('usuarios.html', usuarios=usuarios_inglaterra)
    return redirect(url_for('login'))

# Ruta para mostrar los clientes
@app.route('/clientes')
def mostrar_clientes():
    if 'username' in session:
        return render_template('clientes.html', clientes=clientes_suecia)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
