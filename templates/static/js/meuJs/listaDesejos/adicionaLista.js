const addListaDesejos=async (e)=>{
    let produtoId = e.dataset.id;
    let dados={'produtoId':produtoId}
    let url = '/lista_desejos/'
    let conexao = new Conexao(url,dados)
    let listaProdutos = await conexao.sendPostRequest();
    console.log(listaProdutos)
}