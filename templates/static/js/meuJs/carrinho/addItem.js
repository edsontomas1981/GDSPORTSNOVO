const addItem = (element) => {
    let id = element.dataset.id;
    let carrinho = localStorage.getItem('carrinho');
    
    if (carrinho) {
        carrinho = JSON.parse(carrinho); // Converte a string em um array
        // Verificar se o produto já existe no carrinho
        let produtoExistente = carrinho.find((produto) => produto.id === parseInt(id));

        if (produtoExistente) {
            // Se o produto já existe, aumentar a quantidade e adicionar o volume adicional
            produtoExistente.quantidade += 1;

            localStorage.setItem('carrinho', JSON.stringify(carrinho));

        }
    }
    location.reload();
}
