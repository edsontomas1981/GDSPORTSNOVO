let menu  =document.getElementById('menu')
window.addEventListener('load',()=>{

    carregaMenu();

})



const carregaMenu = async (e)=>{
    let url = '/produtos/read_categorias/'
    let dados = {'login':email.value,'senha':senha.value}
    let conexao = new Conexao(url,dados)
    let html=`<li class="active"><a href="/home/" class="teste" id="0" onclick="teste(this)">Home</a></li>`
    let result= await conexao.sendPostRequest()
    console.log(result) 
    result.categorias.forEach(element => {
        html+=geraMenu(element)
    });
    // Adicionando o HTML gerado na div container
    menu.innerHTML = html;
    e.preventDefault();
}


const geraMenu = (dados)=>{
    // Gerando o HTML a partir do resultado da requisição
    return `
        <li><a href="#" class="teste"  id="${dados.id}" onclick="carregaPageMenu(this)">${dados.categoria}</a></li>
    `;
}

const carregaPageMenu = (idMenu)=>{
    const url = `/home/categoria/?idMenu=${idMenu.id}`;
    window.location.href = url;
}

// ${dados.capa}