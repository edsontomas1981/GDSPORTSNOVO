window.addEventListener('DOMContentLoaded',async ()=>{
    let url = '/autenticacao/logado/'
    let dados = {}
    let conexao = new Conexao(url,dados)
    let result = await conexao.sendPostRequest()
    if(result.status == 200){
        window.location.href = '/checkout/pagar/'; // Redireciona para outra_pagina.html se o usuário estiver logado

    }else{
        alert('usuario nao logado')
    }
});