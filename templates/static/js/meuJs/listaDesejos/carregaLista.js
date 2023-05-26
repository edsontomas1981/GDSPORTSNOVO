const carregaListaDesejos = async ()=>{
    let dados={}
    let url = '/lista_desejos/read_lista/'
    let conexao = new Conexao(url,dados)
    let listaProdutos = await conexao.sendPostRequest();
    widgetCurtidas(listaProdutos.produtos.length)
}