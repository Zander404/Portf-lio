from flask import Flask, render_template

app = Flask(__name__)

 
# criar a 1º pagina do site 
# @app.route('/') O '@app' é para indicar o nome do arquivo, se o nome do projeto fosse myapp ficaria "@myapp.router"
# o Simbolo "@" é um decorretor, atribui uma nova funcionalidade para a função, muito usado no flask  
#Router -> 

#Home Page  
@app.route('/')
def homepage():
    return 'Esse é o meu primeiro site carro'

#Pagina de Contatos 
@app.route('/contatos')
def contatos():
    return render_template("contato.html")

#Pagina de Usuários
@app.route("/usuarios/<nome_usuario>") #<> diz para o flask oq for escrito depois da "/" sera o nome do usuário
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True) #adicionar 'debug=True' no app.run para poder
    # fazer as alterações do site sem ter que recompilr o codigo 
    

#servidor do Heroku
