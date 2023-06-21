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


const carregaPaginaPedidos = ()=>{
    let carrinho = localStorage.getItem('carrinho');
    carrinho = JSON.parse(carrinho)
    if (carrinho){
    carrinho.forEach(element => {
            htmlTabela+=geraPedido(element)
    });

    htmlTabela+=`<tr>
                    <td colspan="5" align="right">
                        <h4>Total</h4>
                    </td>
                    <td colspan="2">
                        <h4> R$ ${geraTotalPedido(carrinho,0.00)}</h4>
                    </td>
                 </tr>`
    tabelaCarrinho.innerHTML = htmlTabela}
}

document.addEventListener('DOMContentLoaded',()=>{
    var loader = document.getElementById('loader');
    loader.style.display = 'none';
    carregaPaginaPedidos();
})

const geraPedido=(produto)=>{
    return     `<tr>
                    <td colspan="2" class="hide-on-mobile">
                        <div class="product-widget">
                            <div class="product-img ">
                                <img src="${produto.img}" alt="${produto.desc}" style="width: 100%;">
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
                                <div class="btn-group" role="group" aria-label="...">
                                    <a href="#" class="btn btn-default" data-id="${produto.id}" onclick="delItem(this)">-</a>
                                </div>
                                <div class="btn-group" role="group" aria-label="...">
                                    <a href="#" class="btn btn-default">${produto.quantidade}</a>
                                </div>
                                <div class="btn-group" role="group" aria-label="...">
                                    <a href="#" class="btn btn-default" data-id="${produto.id}" onclick="addItem(this)">+</a>
                                </div>
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

function exibirLoader() {
    var loader = document.getElementById('loader');
    loader.style.display = 'block';
  }

function atualizarPagina() {
    // Exibir div de carregamento
    exibirLoader();
  
    // Aguardar um pequeno intervalo de tempo antes de recarregar a página (apenas para fins de exemplo)
    setTimeout(function() {
      // Recarregar a página
      location.reload();
    }, 2000); // Tempo de espera de 2 segundos (para fins de exemplo)
  }
  

