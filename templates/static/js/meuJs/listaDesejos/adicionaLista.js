const addListaDesejos=(e)=>{
    let produtoId = e.dataset.id;
    let dados={'produtoId':produtoId}
    let url = '/lista_desejos/'
    let conexao = new Conexao(url,dados)
    conexao.sendPostRequest();
    e.preventDefault();
}