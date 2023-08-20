const chai = require('chai');
const calculadora = require('./calculadora');

const assert = chai.assert;

describe('Calculadora', function() {
  it('Deve somar dois números corretamente', function() {
    assert.equal(calculadora.somar(2, 3), 5);
  });

  it('Deve subtrair dois números corretamente', function() {
    assert.equal(calculadora.subtrair(5, 2), 3);
  });

  it('Deve multiplicar dois números corretamente', function() {
    assert.equal(calculadora.multiplicar(3, 2), 6);
  });

  it('Deve dividir dois números corretamente', function() {
    assert.equal(calculadora.dividir(8, 2), 4);
  });

  it('Deve forçar um erro', function() {
    assert.equal(calculadora.somar(2, 2), 5); // Forçando um erro
  });
});