let btnComprar = document.getElementById('comprar')


btnComprar.addEventListener('click',async (e)=>{
    let itensCarrinho = JSON.parse(localStorage.getItem('carrinho'));
    let dados={'dados':itensCarrinho}
    let url = '/pedidos/'
    let conexao = new Conexao(url,dados)
    let response = await conexao.sendPostRequest();
    e.preventDefault()
})