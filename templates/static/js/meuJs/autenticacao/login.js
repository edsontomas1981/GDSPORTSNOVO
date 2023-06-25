let botaoEntrar = document.getElementById('entrar')
let btnAutentica = document.getElementById('btnAutentica')


const autentica = async (user, senha) => {
  
    let url = '/autenticacao/entrar/';
    let dados = { 'login': user.value, 'senha': senha.value };
    let conexao = new Conexao(url, dados);
    let request = await conexao.sendPostRequest();
  
  }


botaoEntrar.addEventListener('click',async (e)=>{
    let user = document.getElementById('login')
    let senha = document.getElementById('senha')
    await autentica(user,senha);
    e.preventDefault();
    location.reload(); // Recarrega a página
});

btnAutentica.addEventListener('click',async (e)=>{
    let user = document.getElementById('loginAutentica')
    let senha = document.getElementById('senhaAutentica')    
    await autentica(user,senha);
    e.preventDefault();
    location.reload(); // Recarrega a página
});

  
  
  