let imagem = document.getElementById('imagem')
let container = document.getElementById('container')
var loading = document.getElementById("loading");

window.addEventListener('load', async ()=>{
    let url = '/home/categoria/'
    const urlParams = new URLSearchParams(window.location.search);
    const idMenu = urlParams.get('idMenu');
    let dados={'idMenu':idMenu}
    let conexao = new Conexao(url,dados)
    let html=""
    let result= await conexao.sendPostRequest()
    console.log(result)
    result.status.forEach(element => {
        html+=geraHtml(element)
    });
    // Adicionando o HTML gerado na div container
    container.innerHTML = html;
})

const geraHtml = (dados)=>{
        // Gerando o HTML a partir do resultado da requisição
        return `
        <div class="col-md-4 col-xs-6 produtos" id="${dados.id}" onclick="carregaProduto(this)">
            <div class="product">
                <div class="product-img">
                    <img src="${dados.capa}" alt="">
                    <div class="product-label">
                    </div>
                </div>
                <div class="product-body">
                    <p class="product-category">${dados.categoria_fk.categoria}</p>
                    <h3 class="product-name"><a href="#">${dados.descricao}</a></h3>
                    <h4 class="product-price">R$ ${dados.preco}</h4>
                    <div class="product-rating">
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                        <i class="fa fa-star"></i>
                    </div>
                    <div class="product-btns">
                        <button class="add-to-wishlist"><i class="fa fa-heart-o"></i><span class="tooltipp">Curtir</span></button>
                        <button class="quick-view"><a href="/home/produto/"><i class="fa fa-eye"></i></a><span class="tooltipp">Ver mais.</span></button>
                    </div>
                </div>
                <div class="add-to-cart">
                    <button class="add-to-cart-btn"><i class="fa fa-shopping-cart"></i> Adicionar ao carrinho</button>
                </div>
            </div>
        </div>
        `;
}

function toggleAside() {
    var aside = document.getElementById("aside");
    if (aside.style.display === "none") {
      aside.style.display = "block";
    } else {
      aside.style.display = "none";
    }
  }

container.addEventListener("readystatechange", function() {
    if (container.readyState === "complete") {
        loading.style.display = "none";
    } else {
        loading.style.display = "block";
    }
});

const carregaProduto=(e)=>{
    let url = `/home/produto/?idProduto=${e.id}`;
    window.location.href = url;
}