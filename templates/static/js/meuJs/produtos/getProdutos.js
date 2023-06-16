let capa = document.getElementById('imgProduto')

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
        thumbnails: true,
        fixedWidth: 120,
        fixedHeight: 80,
        gap: 1,
        arrowPosition: 'left',
        autoScroll: {
            speed: 1,
          },
      }).mount()
  });
  
  
const carregaDadosProduto=(result)=>{
    btnProdAddCarrinho(result.produto)
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
}

const carrosselHtml = (imagens)=>{
    return `<li class="splide__slide"><img src="${imagens.imagem_url}" 
        onclick="alteraImagem(this)" style="height: 100%;padding: 1px;"></li>`
        }

const btnProdAddCarrinho = (produto)=>{
    alert(1)
    let btnAddProd = document.getElementById('btnProdAddCarrinho')

    let htmlBtnAddCarrinho=  `
        <div class="qty-label">
        Quantidade
        <div class="input-number">
            <input type="number" value="1">
            <span class="qty-up">+</span>
            <span class="qty-down">-</span>
        </div>
        </div>
        <button class="add-to-cart-btn" id="btnProd${produto.id}" onclick="adicionarAoCarrinho(this)" 
                    data-capa="${produto.capa}" data-id="${produto.id}" data-descricao="${produto.descricao}" 
                    data-preco="${produto.preco}"><i class="fa fa-shopping-cart">
                    </i> Adicionar ao carrinho</button>
        `
    btnAddProd.innerHTML = htmlBtnAddCarrinho
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
