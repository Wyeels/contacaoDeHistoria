from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'Wes123ley'

def conectar_db():
    conectar = sqlite3.connect('notas.db')
    return conectar

def criar_tabela():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            turma TEXT NOT NULL,
            nome TEXT NOT NULL,
            nota INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notasvisitante (
            notavis INTEGER
        )
    ''')
    conectar.commit()
    conectar.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notaalu', methods=['POST'])
def adicionar_nota():
    if request.method == 'POST':
        turma = request.form['turma']
        nome = request.form['nome']
        nota = request.form['nota']

    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute(
        'INSERT INTO notas (turma, nome, nota) VALUES (?, ?, ?)', (turma, nome, nota) 
    )
    conectar.commit()
    conectar.close()
    flash('Sua nota foi registrada com sucesso!')
    return redirect(url_for('index'))

@app.route('/visitante')
def convidado():
    return render_template('convidado.html')

@app.route('/notavisitante', methods=['POST'])
def nota_visitante():
    if request.method == 'POST':
        notavis = request.form['notavis']
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute(
        'INSERT INTO notasvisitante (notavis) VALUES (?)', (notavis,)
    )
    conectar.commit()
    conectar.close()
    flash('Sua nota foi registrada com sucesso!')
    return redirect(url_for('convidado'))
    
@app.route('/redgit')
def redirecionar_git():
    return redirect('https://github.com/wyeels')

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True, host="0.0.0.0", port=5000)