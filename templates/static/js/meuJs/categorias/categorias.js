let imagem = document.getElementById('imagem');
let container = document.getElementById('container');
let loading = document.getElementById("loading");
let filtroCategorias = document.getElementById("filtroCategorias");
let imagensCarregadas = 0;
let totalImagens = 0;
let currentPage = 1;
const itemsPerPage =6; // Define quantos itens você deseja exibir por página

window.addEventListener('load', async () => {
    const loadingOverlay = document.getElementById("loading-overlay");
    loadingOverlay.style.display = "none";

    let url = '/home/categoria/';
    const urlParams = new URLSearchParams(window.location.search);
    const idMenu = urlParams.get('idMenu');
    let carrinho = localStorage.getItem('carrinho')
    let dados = { 'idMenu': idMenu,carrinho};
    let conexao = new Conexao(url, dados);
    let result = await conexao.sendPostRequest();
    let teste = buscarPorSubcategoria(result,[10,11])
    console.log(teste)


    let totalPages = Math.ceil(result.status.length / itemsPerPage); // Calcula o número total de páginas
    renderizaPagina(currentPage, result.status); // Renderiza a página atual

    carregaFiltroSubcategorias(result.subcategorias,result);
    carregaFiltroMarcas(result.marcas,result);

        // Função para renderizar uma página específica
        function renderizaPagina(page, data) {
            let startIndex = (page - 1) * itemsPerPage;
            let endIndex = startIndex + itemsPerPage;
            let pageData = data.slice(startIndex, endIndex);
            let html = "";
            pageData.forEach(element => {
                html += geraHtml(element);
            });
            container.innerHTML = html;
        }
    
        // Função para atualizar a página
        function updatePage() {
            renderizaPagina(currentPage, result.status);
        }
    
        // Função para atualizar os controles de paginação
        function updatePaginationControls() {
            // Lógica para habilitar/desabilitar os botões de página anterior/próxima
            if (currentPage === 1) {
                document.getElementById("previousPageBtn").disabled = true;
            } else {
                document.getElementById("previousPageBtn").disabled = false;
            }
            if (currentPage === totalPages) {
                document.getElementById("nextPageBtn").disabled = true;
            } else {
                document.getElementById("nextPageBtn").disabled = false;
            }
        }    
    
        // Função para ir para a página anterior
        window.goToPreviousPage = function () {
            if (currentPage > 1) {
                currentPage--;
                updatePage();
                updatePaginationControls();
            }
        }
    
        // Função para ir para a próxima página
        window.goToNextPage = function () {
            if (currentPage < totalPages) {
                currentPage++;
                updatePage();
                updatePaginationControls();
            }
        }    
    
        renderizaControlesPaginacao();
    
        // Função para renderizar os controles de paginação com números de página
        function renderizaControlesPaginacao() {
            let paginationControls = document.getElementById("paginationControls");
            let html = `
                <a id="previousPageBtn" onclick="goToPreviousPage()" style="padding:20px;"><i class="fa fa-arrow-left" aria-hidden="true"></i></a>
            `;
    
            // Adiciona os números das páginas
            for (let i = 1; i <= totalPages; i++) {
                if (i === currentPage) {
                    html += `<a class="pageNumber" onclick="goToPage(${ i })" style="padding:10px; cursor:pointer;">${ i }</a>`;
                } else {
                    html += `<a class="pageNumber" onclick="goToPage(${ i })" style="padding:20px;cursor:pointer;">${ i }</a>`;                }
            }
    
            html += `
                <a id="nextPageBtn" onclick="goToNextPage()" style="padding:20px;"><i class="fa fa-arrow-right" aria-hidden="true"></i></a>
            `;
            paginationControls.innerHTML = html;
            updatePaginationControls();
        }
    
        // Função para ir para uma página específica
        window.goToPage = function (page) {
            if (page >= 1 && page <= totalPages) {
                currentPage = page;
                updatePage();
                updatePaginationControls();
            } else if (page === 0) {
                currentPage = 1;
                updatePage();
                updatePaginationControls();
            }
        }


        
});

const carregaFiltroSubcategorias=(subcategorias,result)=>{
    html=''
    console.log(subcategorias)
    subcategorias.forEach(element => {
        html+=`<div class="input-checkbox">
                    <input type="checkbox" onclick="filtrarProdutos(${result})" id="subcategoria${element.id}">
                        <label for="subcategoria${element.id}">
                        <span></span>
                        ${element.descricao}
                        <small>(${element.total_registros})</small>
                    </label>    
                </div>`
        });
    filtroCategorias.innerHTML = html;
}

const carregaFiltroMarcas=(marcas,result)=>{
    let filtroMarcas = document.getElementById('filtroMarcas')
    html=''
    console.log(marcas)
    marcas.forEach(element => {
    html+= `<div class="input-checkbox">
                <input type="checkbox" onclick="filtrarProdutos()" id="marca${element.id}">
                <label for="marca${element.id}">
                    <span></span>
                    ${element.marca}
                    <small>(${element.total_registros})</small>
                </label>
            </div>
    `
    });
    filtroMarcas.innerHTML = html;
}

const geraHtml = (dados)=>{
        // Gerando o HTML a partir do resultado da requisição
        return `
        <div class="col-md-4 col-xs-6 produtos">
            <div class="product">
                <div class="product-img">
                    <img src="${dados.capa}" alt="" id="${dados.id}" onclick="carregaProduto(this)">
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
                        <button class="quick-view"><a href="/home/produto/?idProduto=${dados.id}"><i class="fa fa-eye"></i></a><span class="tooltipp">Ver mais.</span></button>
                    </div>
                </div>
                <div class="add-to-cart">
                    <button class="add-to-cart-btn btnAdicionaCarrinho" id="btnProd${dados.id}" onclick="adicionarAoCarrinho(this)" data-capa="${dados.capa}"><i class="fa fa-shopping-cart"></i> Adicionar ao carrinho</button>
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
