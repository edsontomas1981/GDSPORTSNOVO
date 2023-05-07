function mascaraTelefone(input) {
    const valorAnterior = input.value.replace(/\D/g, "");
    const digitos = valorAnterior.length;
    let valorFormatado = "";
  
    if (digitos < 11) {
      valorFormatado = valorAnterior.replace(/(\d{0,2})(\d{0,4})(\d{0,4})/, "($1) $2-$3");
    } else {
      valorFormatado = valorAnterior.replace(/(\d{0,2})(\d{0,5})(\d{0,4})/, "($1) $2-$3");
    }
  
    input.value = valorFormatado;
  }
  