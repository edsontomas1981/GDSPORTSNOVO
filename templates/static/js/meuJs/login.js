let email = document.getElementById('email')
let senha = document.getElementById('password')

let botaoEntrar = document.getElementById('entrar')

botaoEntrar.addEventListener('click', async (e)=>{
    let url = '/autenticacao/login/'
    let dados = {'login':email.value,'senha':senha.value}
    let conexao = new Conexao(url,dados)
    let result= await conexao.sendPostRequest()
    e.preventDefault();
});

