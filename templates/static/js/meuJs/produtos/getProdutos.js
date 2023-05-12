

window.addEventListener('DOMContentLoaded', async ()=>{
    let url = '/produtos/read_produtos/'
    const urlParams = new URLSearchParams(window.location.search);
    const idProduto = urlParams.get('idProduto');
    let dados={'idProduto':idProduto}
    let conexao = new Conexao(url,dados)
    let htmlProduto=""
    let result= await conexao.sendPostRequest()
    carregaDadosProduto(result);
})

const carregaDadosProduto=(result)=>{
    let capa = document.getElementById('imgProduto')
    let nomeProduto = document.getElementById('nomeProduto')
    let precoProduto = document.getElementById('precoProduto')
    let estoque = document.getElementById('estoqueProduto')
    let descProduto = document.getElementById('descProduto')
    // let carrossel = document.getElementById('carousel')
    console.log(result)
    capa.setAttribute('src', result.produto.capa);
    nomeProduto.textContent=result.produto.descricao
    precoProduto.textContent='R$ '+ result.produto.preco
    if (result.produto.qtde>0){
        estoque.textContent='Em estoque'
    }else{
        estoque.textContent='Esgotado'
    }
    descProduto.textContent=result.produto.descricao
    let htmCarrossel =""
    result.imagens.forEach(element => {
        htmCarrossel+=carrosselHtml(element)    
    });
    // carrossel.innerHTML=htmCarrossel
}

const carrosselHtml = (imagens)=>{
    return `<div class="carousel-item active col-md-6">
                <img src="${imagens.imagem_url}" class="d-block w-100" alt="Imagem 1" style="width: 100%; padding:1px;">
            </div>
            <div class="carousel-item active col-md-6">
                <img src="${imagens.imagem_url}" class="d-block w-100" alt="Imagem 1" style="width: 100%; padding:1px;">
            </div>
            <div class="carousel-item active col-md-6">
                <img src="${imagens.imagem_url}" class="d-block w-100" alt="Imagem 1" style="width: 100%; padding:1px;">
            </div>            
            `
}