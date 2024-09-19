from flask import Flask,flash ,render_template, request, redirect, url_for, session
from Usuario import Usuario
from Servico import Servico

usuario1= Usuario('Bruno Divino', 'BD', 'alohomora')
usuario2= Usuario('Camila Ferreira', 'Mila', 'paozinho')
usuario3= Usuario('Guilherme Louro', 'Cake', 'python_eh_vida')

usuarios = { usuario1.nickname : usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3  }

servico1 = Servico('cabelo',"20,00")

servicos = { servico1.nome : servico1
            }

app = Flask(__name__)
app.secret_key = 'sdaghbdujighasuidhasidjioasghdui'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registerClient')
def registerClient():
    return render_template('register.html')

# @app.route('/addfuncionario')
# def add_funcionario():
#     return 'Adicionar Funcionário'

@app.route('/dashboard')
def dashboard():
    if 'usuario_logado' not in session:
        return redirect(url_for('home'))
    
    usuario_logado = session.get('usuario_logado')
    return render_template('dashboard.html', usuario_logado=usuario_logado)


@app.route('/login', methods=['POST'])
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
        
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nickname = request.form['nickname']
        senha = request.form['senha']
        
        if nickname in usuarios:
            flash('Nome de usuário já existe!')
        else:
            novo_usuario = Usuario(email, nickname, senha)
            usuarios[nickname] = novo_usuario
            session['usuario_logado'] = novo_usuario.nickname
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('home'))
        
    return redirect(url_for('home'))

@app.route('/logout')
def logout():

    session.pop('usuario_logado', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
