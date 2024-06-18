from flask import Flask, request, jsonify


app = Flask(__name__)

# Inicializa a lista de convidados
convidados = [
    {
        'id':1,
        'nome': 'Bruno Gomes de Sousa'
    },
    {
        'id': 2,
        'nome': 'Marina Silva'
    },
    {
        'id': 3,
        'nome': 'Lupin Gomes'
    }

]

@app.route('/convidados', methods=['GET'])
def get_convidados():
    return jsonify(convidados)

@app.route('/convidados', methods=['POST'])
def add_convidado():
    novo_convidado = request.get_json()
    convidados.append(novo_convidado)
    return jsonify(convidados[-1])

@app.route('/convidados/<int:index>', methods=['GET'])
def get_convidado(index):
    if index < len(convidados):
        return jsonify(convidados[index])
    else:
        return jsonify({'erro': 'Convidado não encontrado'}), 404

@app.route('/convidados/<int:index>', methods=['DELETE'])
def delete_convidado(index):
    if index < len(convidados):
        del convidados[index]
        return jsonify({'mensagem': 'Convidado deletado com sucesso'})
    else:
        return jsonify({'erro': 'Convidado não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)