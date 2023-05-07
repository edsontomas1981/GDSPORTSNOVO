let email = document.getElementById('user')
let firstName = document.getElementById('nome')
let cadastroSenha = document.getElementById('cadastroSenha')
let confirmacaoSenha = document.getElementById('confirmacaoSenha')
let btnCadastrar = document.getElementById('cadastrar')
let formulario = document.getElementById('formCadastro')

btnCadastrar.addEventListener('click',(e)=>{
    if (validaForm(formulario)){
        if (validarEmail(email.value)){
            let url = '/autenticacao/cadastrar/';
            
            let dados = {'login':email.value,'firstName':firstName.value,
                        'cadastroSenha':cadastroSenha.value,'confirmacaoSenha':confirmacaoSenha.value,};
            
                        let conexao = new Conexao(url,dados);
            conexao.sendPostRequest();
        }else{
            alert("Email inválido")
        }
    }else{
        alert('Inválido')
    }
    e.preventDefault();
})

email.addEventListener('keypress',(e)=>{
    if(!validarEmail(email.value)){
        email.classList.add("invalid");
    }else{
        email.classList.remove("invalid");
    }

})