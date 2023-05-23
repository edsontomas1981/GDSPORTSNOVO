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
  valorCarrinho(totalCarrinho, qtdeCarrinho);
};

const listaItemsWidget = (produto) => {
  return `<div class="product-widget">
    <div class="product-img">
      <img src="${produto.img}" alt="${produto.desc}">
    </div>
    <div class="product-body">
      <h3 class="product-name"><a href="#">${produto.desc}</a></h3>
      <h4 class="product-price"><span class="qty">${parseInt(produto.quantidade)}x</span>R$${parseFloat(produto.preco).toFixed(2)}</h4>
    </div>
    <button class="delete" onclick="removeItemCarrinho(${produto.id})"><i class="fa fa-close"></i></button>
  </div>`;
};

const valorCarrinho = (total, qtde) => {
  widgetTotalCarrinho.innerHTML = `<small>${qtde} Item(s) selecionados</small>
    <h5>SUBTOTAL: R$ ${total.toFixed(2)}</h5>`;
};

const removeItemCarrinho = (idProduto) => {
  let itensCarrinho = JSON.parse(localStorage.getItem('carrinho')); // Obtém os itens do carrinho do localStorage

  // Verifica se itensCarrinho é uma matriz válida
  if (!Array.isArray(itensCarrinho)) {
    return;
  }

  // Encontra o índice do item com o ID correspondente no carrinho
  const indice = itensCarrinho.findIndex(item => item.id === idProduto);

  // Verifica se o item foi encontrado
  if (indice !== -1) {
    itensCarrinho.splice(indice, 1); // Remove o item do carrinho usando o índice

    // Atualiza o localStorage com os itens do carrinho atualizados
    localStorage.setItem('carrinho', JSON.stringify(itensCarrinho));

    // Atualiza o widget do carrinho
    updateWidgetCarrinho();
  }
};


