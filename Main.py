from flask import Flask,render_template, request, redirect,flash,session

app = Flask(__name__)
app.secret_key = 'MiauMiauGatinGatin'
Lista_Tarefas = []



@app.route('/')
def index():
    tarefas = session.get('tarefas', [])
    return render_template('index.html', tarefas = Lista_Tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    tarefas = session.get('tarefas', [])

    if tarefa:
        nomes_existentes = [t['nome'].lower() for t in tarefas]
        if tarefa.lower() not in nomes_existentes:
            tarefas.append({'nome': tarefa, 'feito': False})
            session['tarefas'] = tarefas
        else:
            flash('Essa Tarefa já existe!')
    return redirect('/')


@app.route('/tarefas', methods=['POST'])
def tarefas():
    acao = request.form.get('acao')
    selecionadas = request.form.getlist('tarefas_selecionadas')

    tarefas = session.get('tarefas', [])

    if acao == 'excluir':
        tarefas = [t for t in tarefas if t['nome'] not in selecionadas]
    else:
        for t in tarefas:
            t['feito'] = t['nome'] in selecionadas

    session['tarefas'] = tarefas
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)