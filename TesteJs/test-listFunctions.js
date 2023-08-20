const chai = require("chai");
const expect = chai.expect;

const {sum, average, max, min} = require("./listfunctions");

describe("Testes Funcionais do File test-listFunctions.js", ()=>{
    let lista_numbers=[2,3,4,5,6]
    it("Deve retornar a soma correta dos elementos em lista",()=>{
     expect(sum(lista_numbers)).to.equal(20);
    });
    it("Deve retornar a média correta dos elementos em lista",()=>{
        expect(average(lista_numbers)).to.equal(4);
    });
    it("Deve retornar o maior valor elementos em lista",()=>{
      expect(max(lista_numbers)).to.equal(6);
    });
    it("Deve retornar o menor valor elementos em lista",()=>{
        expect(min(lista_numbers)).to.equal(2);
       });
});