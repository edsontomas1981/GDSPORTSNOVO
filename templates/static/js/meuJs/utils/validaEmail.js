function validarEmail(email) {
    const expressaoRegular = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return expressaoRegular.test(email);
  }






