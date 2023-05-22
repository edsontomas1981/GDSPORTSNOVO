let listaWidgetCarrinho = document.getElementById('widgetCarrinho');
let listaCarrinho = "";
let totalCarrinho = 0.00;
let widgetTotalCarrinho = document.getElementById('totalCarrinho');
let qtdeCarrinho = 0;

const updateWidgetCarrinho = () => {
  let itensCarrinho = JSON.parse(localStorage.getItem('carrinho'));
  let widgetCarrinho = document.getElementById('carrinho');
  listaCarrinho = "";
  qtdeCarrinho = 0;
  totalCarrinho = 0;
  listaWidgetCarrinho.innerHTML = listaCarrinho;

  if (itensCarrinho && itensCarrinho.length > 0) {
    widgetCarrinho.innerHTML = `<i class="fa fa-shopping-cart"></i>
      <span>Carrinho</span>
      <div class="qty" id="qtdeCarrinho">${itensCarrinho.length}</div>`;

    itensCarrinho.forEach(element => {
      listaCarrinho += listaItemsWidget(element);
      qtdeCarrinho += element.quantidade;
      totalCarrinho += element.quantidade * parseFloat(element.preco);
    });

    listaWidgetCarrinho.innerHTML = listaCarrinho;
    valorCarrinho(totalCarrinho, qtdeCarrinho);
  } else {
    widgetCarrinho.innerHTML = `<i class="fa fa-shopping-cart"></i>
      							 <span>Carrinho</span>`;
  }
};

const listaItemsWidget = (produto) => {
  return `<div class="product-widget">
    <div class="product-img">
      <img src="${produto.img}" alt="">
    </div>
    <div class="product-body">
      <h3 class="product-name"><a href="#">${produto.desc}</a></h3>
      <h4 class="product-price"><span class="qty">${produto.quantidade}x</span>R$${produto.preco.toFixed(2)}</h4>
    </div>
    <button class="delete" data-produto="${JSON.stringify(produto)}" onclick="removeItemCarrinho(this)"><i class="fa fa-close"></i></button>
  </div>`;
};

const valorCarrinho = (total, qtde) => {
  widgetTotalCarrinho.innerHTML = `<small>${qtde} Item(s) selecionados</small>
    <h5>SUBTOTAL: R$ ${total.toFixed(2)}</h5>`;
};

const removeItemCarrinho = (botao) => {
  let produto = JSON.parse(botao.dataset.produto);
  console.log(produto)
  // Aqui você pode adicionar a lógica para remover o item do carrinho, como atualizar o localStorage ou enviar uma solicitação ao servidor.

  // Exemplo: Remover o item do localStorage
//   let itensCarrinho = JSON.parse(localStorage.getItem('carrinho'));
//   let indice = itensCarrinho.findIndex(item => item.desc === produto.desc);
//   if (indice !== -1) {
//     itensCarrinho.splice(indice, 1);
//     localStorage.setItem('carrinho', JSON.stringify(itensCarrinho));
//   }

//   updateWidgetCarrinho(); // Atualizar o widget do carrinho após remover o item
};
