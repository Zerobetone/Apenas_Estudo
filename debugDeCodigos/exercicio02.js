const alunos = [
    { nome: 'Ana', notas: [8, 7, 9] },
    { nome: 'João', notas: [5, 6, 7] },
    { nome: 'Maria', notas: [9, 9, 10] }
  ];
  
  function calcularMedia(notas) {
    let total = 0;
    for (let i = 0; i < notas.length; i++) {
      total += notas[i];
    }
    return total / notas.length;
  }
  
  function mostrarInformacoesAluno(aluno) {
    console.log(`Nome: ${aluno.nome}`);
    console.log(`Notas: ${aluno.notas.join(', ')}`);
    const media = calcularMedia(aluno.notas);
    console.log(`Média: ${media.toFixed(2)}`);
    console.log('---');
  }
  
  function mostrarInformacoesTurma(turma) {
    console.log('Informações da Turma:');
    for (let i = 0; i < turma.length; i++) {
      console.log(`Aluno ${i + 1}:`);
      mostrarInformacoesAluno(turma[i]);
    }
  }
  
  mostrarInformacoesTurma(alunos);