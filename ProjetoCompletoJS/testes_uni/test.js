const chai = require("chai");
const expect = chai.expect;

const createTask = require('./filecreatetask'); // Corrija o caminho conforme necessário

describe("Testes da Implementação CRUD TASKS", () => {
  it("DEVE VERIFICAR A FUNÇÃO CREATE", () => {
    const titulo = 'Dever de casa';
    const descricao = 'Matemática';
    let lista_task = createTask(titulo, descricao); // Apenas chame a função diretamente
    expect(lista_task).to.have.lengthOf(1); // Corrija o erro de sintaxe aqui
    expect(lista_task[0]).to.equal({ title: 'Dever de casa', description: 'Matemática' }); // Corrija o erro de sintaxe aqui
  });
});




