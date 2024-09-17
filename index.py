from flask import Flask,flash ,render_template, request, redirect, url_for, session
from Usuario import Usuario

usuario1= Usuario('Bruno Divino', 'BD', 'alohomora')
usuario2= Usuario('Camila Ferreira', 'Mila', 'paozinho')
usuario3= Usuario('Guilherme Louro', 'Cake', 'python_eh_vida')

usuarios = { usuario1.nickname : usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3  }

app = Flask(__name__)
app.secret_key = 'sdaghbdujighasuidhasidjioasghdui'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addfuncionario')
def add_funcionario():
    return 'Adicionar Funcionário'

@app.route('/dashboard')
def dashboard():
    if 'usuario_logado' not in session:
        return redirect(url_for('home'))
    
    usuario_logado = session.get('usuario_logado')
    return render_template('dashboard.html', usuario_logado=usuario_logado)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['usuario'] in usuarios:
            usuario = usuarios[request.form['usuario']]
            if request.form['senha'] == usuario.senha:
                session['usuario_logado'] = usuario.nickname
                flash(usuario.nickname + ' logado com sucesso!')
                return redirect(url_for('dashboard'))
           
        else:
            return redirect(url_for('home'))

@app.route('/logout')
def logout():

    session.pop('usuario_logado', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
