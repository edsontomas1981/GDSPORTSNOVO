const updateWidgetCarrinho = ()=>{
	alert('carrinho')
	let carrinho = document.getElementById('carrinho')
	carrinho.innerHTML = `<i class="fa fa-shopping-cart"></i>
						  <span>Carrinho</span>
						  <div class="qty" id="qtdeCarrinho">5</div>`
}