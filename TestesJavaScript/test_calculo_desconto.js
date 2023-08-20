const chai = require ('chai');
const calculo_desconto = require('./calculo_desconto');

const expect = chai.expect;
const assert = chai.assert;

describe("CalcoloDesconto",()=>{
    it("Deve retorna o valor correto após aplicar um desconto de 10% em um valor total de 100", ()=>{
        const valorTotal =100;
        const descontoPercentual=10;
        const valorComDesconto = calculo_desconto(valorTotal,descontoPercentual);
        expect(valorComDesconto).to.equal(90);
    });
    it("Verifica se a função calcularTotalComDesconto retorna o valor correto após aplicar um desconto de 25% em um valor total de 200.", ()=>{
        const valorTotal =200;
        const descontoPercentual = 25;
        const valorComDesconto= calculo_desconto(valorTotal,descontoPercentual);
        expect(valorComDesconto).to.equal(150);
    })
});