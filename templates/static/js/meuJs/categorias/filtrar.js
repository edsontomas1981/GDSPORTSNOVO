function buscarPorSubcategoria(objetos, subcategorias) {
    const resultados = [];
    for (let i = 0; i < objetos.length; i++) {
        const obj = objetos[i];
        if (obj.subcategorias) {
            const matchingSubcategorias = obj.subcategorias.filter(subcat => subcategorias.id.includes(subcat.id));
            if (matchingSubcategorias.length > 0) {
                resultados.push(obj);
            }
        }
    }
    return resultados;
}