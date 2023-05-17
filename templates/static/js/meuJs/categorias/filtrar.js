// let btnFiltrar = document.getElementById('btnFiltrar')
// function verificarCheckboxes(div) {
//     // Obtém a referência para a div que contém os checkboxes
//     let divCheckboxes = document.getElementById(div);
  
//     // Obtém todos os elementos filhos da div
//     let elementos = divCheckboxes.getElementsByTagName('input');
  
//     // Array para armazenar os checkboxes marcados
//     let checkboxesMarcados = [];

    
//     // Percorre os elementos e verifica quais são checkboxes marcados
//     for (let i = 0; i < elementos.length; i++) {
//       let elemento = elementos[i];
//       if (elemento.type === 'checkbox' && elemento.checked) {
//         checkboxesMarcados.push(elemento);
//       }
//     }
    
//     let listaCheckbox = []
//     // Exibe os checkboxes marcados no console
//     console.log('Checkboxes marcados:');
//     checkboxesMarcados.forEach(function(checkbox) {
//         lista.push(checkbox.id);
//     });
//   }

//   btnFiltrar.addEventListener('click',()=>{
//     let subcategorias = verificarCheckboxes('filtroCategorias');
//     verificarCheckboxes('filtroMarcas');
//   })
  