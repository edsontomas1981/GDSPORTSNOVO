let capa = document.getElementById('imgProduto')

window.addEventListener('DOMContentLoaded', async ()=>{

})
document.addEventListener('DOMContentLoaded', async ()=> {

    let url = '/produtos/read_produtos/'
    const urlParams = new URLSearchParams(window.location.search);
    const idProduto = urlParams.get('idProduto');
    let dados={'idProduto':idProduto}
    let conexao = new Conexao(url,dados)
    let result= await conexao.sendPostRequest()
    carregaDadosProduto(result);

    new Splide('.splide', {
        type   : 'loop',
        direction: 'ttb',
        height   : '37rem',
        width: true,
        perPage: 4,
        // Adiciona o componente Thumbnail
        thumbnails: true,
        // Define o tamanho das miniaturas
        fixedWidth: 120,
        fixedHeight: 80,
        gap: 10,
        arrowPosition: 'left',
        autoScroll: {
            speed: 1,
          },
      }).mount()
  });
  
  
const carregaDadosProduto=(result)=>{
    let nomeProduto = document.getElementById('nomeProduto')
    let precoProduto = document.getElementById('precoProduto')
    let estoque = document.getElementById('estoqueProduto')
    let descProduto = document.getElementById('descProduto')
    let imgProdutoSlide = document.getElementById('imgProdutoSlide')
    capa.setAttribute('src', result.produto.capa);
    nomeProduto.textContent=result.produto.descricao
    precoProduto.textContent='R$ '+ result.produto.preco
    let htmCarrossel =`<li class="splide__slide">
                        <img src="${result.produto.capa}" 
                        onclick="alteraImagem(this)" 
                        style="height: 100%;padding: 1px;"></li>`

    console.log(result)
    if (result.produto.qtde>0){
        estoque.textContent='Em estoque'
    }else{
        estoque.textContent='Esgotado'
    }
    descProduto.textContent=result.produto.descricao


    result.imagens.forEach(element => {
        htmCarrossel+=carrosselHtml(element) 
    });
    imgProdutoSlide.innerHTML=htmCarrossel
    console.log(htmCarrossel)
}

const carrosselHtml = (imagens)=>{
    return `
            <li class="splide__slide"><img src="${imagens.imagem_url}" onclick="alteraImagem(this)" style="height: 100%;padding: 1px;"></li>
        `
}

const alteraImagem=(imagem) =>{
    capa.setAttribute('src', imagem.src);
}

const imagem = document.querySelector('.imagem');
imagem.addEventListener('mouseover', () => {
  imagem.style.transform = 'scale(1.2)';
});
imagem.addEventListener('mouseout', () => {
  imagem.style.transform = 'none';
});
