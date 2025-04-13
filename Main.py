from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'MiauMiauGatinGatin'

Lista_Tarefas = []

@app.route('/')
def index():
    # Verifica se a chave 'tarefas' existe na sessão, caso contrário, define uma lista vazia
    tarefas = session.get('tarefas', [])
    return render_template('index.html', tarefas=tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    tarefas = session.get('tarefas', [])

    if not tarefa or not tarefa.strip():
        flash('Digite uma tarefa!')
    elif len(tarefa) > 120:
        flash('Tarefa muito longa! Máximo de 120 caracteres.')
    else:
        # Verifica se a tarefa já existe
        nomes_existentes = [t['nome'].lower() for t in tarefas]
        if tarefa.lower() not in nomes_existentes:
            tarefas.append({'nome': tarefa, 'feito': False})  # Adiciona a tarefa
            session['tarefas'] = tarefas  # Atualiza a sessão com as novas tarefas
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
        # Atualiza o estado da tarefa (feita ou não)
        for t in tarefas:
            t['feito'] = t['nome'] in selecionadas

    session['tarefas'] = tarefas  # Atualiza a sessão com as novas mudanças
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
