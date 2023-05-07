let user = document.getElementById('login')
let senha = document.getElementById('senha')

let botaoEntrar = document.getElementById('entrar')

botaoEntrar.addEventListener('click',(e)=>{
    let url = '/autenticacao/entrar/';
    let dados = {'login':user.value,'senha':senha.value};
    let conexao = new Conexao(url,dados);
    conexao.sendPostRequest();
    e.preventDefault();
})
