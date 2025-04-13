from flask import Flask,render_template, request, redirect,flash

app = Flask(__name__)
app.secret_key = 'MiauMiauGatinGatin'
Lista_Tarefas = []



@app.route('/')
def index():
    return render_template('index.html', tarefas = Lista_Tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    if tarefa:
        # Verifica se já existe uma tarefa com o mesmo nome (ignorando maiúsculas/minúsculas)
        nomes_existentes = [t['nome'].lower() for t in Lista_Tarefas]
        if tarefa.lower() not in nomes_existentes:
            Lista_Tarefas.append({'nome': tarefa, 'feito': False})
        else:
            flash('Essa Tarefa já existe!')
    return redirect('/')


@app.route('/tarefas', methods=['POST'])
def tarefas():
    acao = request.form.get('acao')  # Vai ser 'excluir' se clicar no botão
    selecionadas = request.form.getlist('tarefas_selecionadas')

    global Lista_Tarefas


    if acao == 'excluir':
        Lista_Tarefas = [
            tarefa for tarefa in Lista_Tarefas
            if tarefa['nome'] not in selecionadas
        ]
    else:
        # Submissão veio de checkbox (não tem 'acao')
        for tarefa in Lista_Tarefas:
            tarefa['feito'] = tarefa['nome'] in selecionadas

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)