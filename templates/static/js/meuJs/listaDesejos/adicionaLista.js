const addListaDesejos=async (e)=>{
    let dados_logado={}
    let url_logado = '/autenticacao/logado/'
    let conexao_logado = new Conexao(url_logado,dados_logado)
    let response = await conexao_logado.sendPostRequest();
    
    if (response.status==200){
        let produtoId = e.dataset.id;
        let dados={'produtoId':produtoId}
        let url = '/lista_desejos/'
        let conexao = new Conexao(url,dados)
        let listaProdutos = await conexao.sendPostRequest();
        carregaListaDesejos()
    }
}