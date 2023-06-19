let htmlItemCarrinho = ''
let descricaoProdcarrinho = document.getElementById('itemListaCarrinho')
let totalPedido = document.getElementById('totalPedido')
let frete = document.getElementById('vlrFrete')

document.addEventListener('DOMContentLoaded',()=>{
    let carrinho = localStorage.getItem('carrinho');
    carrinho = JSON.parse(carrinho)
    carrinho.forEach(element => {
        console.log(element)
        htmlItemCarrinho += geraPedido(element)
    });
    descricaoProdcarrinho.innerHTML = htmlItemCarrinho
    let htmlFrete=geraFrete(0.00)
    frete.innerHTML = htmlFrete
    let htmlValor = geraTotalPedido(carrinho,0.00)
    totalPedido.innerHTML = htmlValor
})

const geraPedido=(produto)=>{

    return `<div class="order-col">
                <div class="product-img">
                    <img src="${produto.img}" alt="${produto.desc}" width="10%">
                </div>
                <div>
                    <div class="input-number">
                        <input type="number" value="${produto.quantidade}">
                        <span class="qty-up">+</span>
                        <span class="qty-down">-</span>
                    </div>
                </div>
            <div class="text-center">${produto.desc}</div>
                <div>R$ ${parseFloat(produto.preco)*parseFloat(produto.quantidade)}</div>
            </div>` 

}

const geraFrete = (vlrFrete)=>{
    return`<hr><strong>${parseFloat(vlrFrete)}</strong><hr>`
}

const geraTotalPedido =(carrinho,frete)=>{
    let totalGeral=0.00
    carrinho.forEach(produto => {
        totalGeral += parseFloat(produto.preco)*parseFloat(produto.quantidade)
    });
    totalGeral += frete
    return`<strong class="order-total">R$ ${totalGeral}</strong><hr>`

}

/*
<div class="product-widget">

    <div class="product-body">
      <h3 class="product-name"><a href="#">Palmeiras 2023</a></h3>
      <h4 class="product-price"><span class="qty">1x</span>R$89.90</h4>
    </div>
    <button class="delete" onclick="removeItemCarrinho(10)"><i class="fa fa-close"></i></button>
  </div>
*/


