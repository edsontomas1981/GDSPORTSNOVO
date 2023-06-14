const carregaListaDesejos = async ()=>{
    let dados_logado={}
    let url_logado = '/autenticacao/logado/'
    let conexao_logado = new Conexao(url_logado,dados_logado)
    let response = await conexao_logado.sendPostRequest();
    
    if (response.status==200){
        let dados={}
        let url = '/lista_desejos/read_lista/'
        let conexao = new Conexao(url,dados)
        let listaProdutos = await conexao.sendPostRequest();
        widgetCurtidas(listaProdutos.produtos.length)}
        else{
        widgetCurtidas(0)
        }
}