let htmlItemCarrinho = ''
let descricaoProdcarrinho = document.getElementById('itemListaCarrinho')
let totalPedido = document.getElementById('totalPedido')
let frete = document.getElementById('vlrFrete')
let tabelaCarrinho = document.getElementById('tabelaCarrinho')

let htmlTabela = `
            <div class="cart-list hide-on-mobile">
                <thead>
                    <tr>
                        <th class="hide-on-mobile"></th>    
                        <th class="hide-on-mobile"></th>    
                        <th>Produto</th>
                        <th>Quantidade</th>    
                        <th>Valor unitario R$</th>
                        <th>Valor Total</th>
                    </tr>
                  </thead>`

document.addEventListener('DOMContentLoaded',()=>{
    let carrinho = localStorage.getItem('carrinho');
    carrinho = JSON.parse(carrinho)
    if (carrinho){
    carrinho.forEach(element => {
        console.log(element)
        htmlTabela+=geraPedido(element)
    });

    htmlTabela+=`<tr>
                    <td colspan="3" align="right">
                        <h4>Total</h4>
                    </td>
                    <td colspan="3">
                        <h4> R$ ${geraTotalPedido(carrinho,0.00)}</h4>
                    </td>
                 </tr>`

    tabelaCarrinho.innerHTML = htmlTabela}
})

const geraPedido=(produto)=>{
    return     `<tr>
                    <td colspan="2" class="hide-on-mobile">
                        <div class="product-widget">
                            <div class="product-img ">
                                <img src="${produto.img}" alt="${produto.desc}" style="width: 100%;">
                                <button class="delete" onclick="removeItemCarrinho(9)">
                                <i class="fa fa-close"></i>
                            </button>
                            </div>
                        </div>
                    </td>
                    <td>
                        <div class="product-body">
                            <h5 class="product-name alinhaTabela"><a href="#">${produto.desc}</a></h5>
                        </div>
                    </td>
                    <td>
                        <div class="product-body">
                        <div class="header-search">

                        <div class="btn-toolbar" role="toolbar" aria-label="...">
                            <div class="btn-group" role="group" aria-label="..."><button type="button" class="btn btn-default">-</button></div>
                            <div class="btn-group" role="group" aria-label="..."><a href="#" class="btn btn-default">${produto.quantidade}</a></div>
                            <div class="btn-group" role="group" aria-label="..."><button type="button" class="btn btn-default">+</button></div>
                        </div>                        
                    </td>
                    <td>
                        <div class="product-body">
                            <h5 class="product-price alinhaTabela" ><span class="qty">${(produto.preco).toFixed(2)}</h5>
                        </div>
                    </td>                                           
                    <td>
                        <div class="product-body">
                            <h5 class="product-price alinhaTabela"><span class="qty">${(produto.preco*produto.quantidade).toFixed(2)}</h5>
                        </div>
                    </td>                     

                </tr>
            </div>`//fecha uma div iniciado na linha 8
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
    return parseFloat(totalGeral).toFixed(2)

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


