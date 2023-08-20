function calcularTotalComDesconto(valorTotal, descontoPercentual) {
    const desconto = (valorTotal * descontoPercentual) / 100;
    const totalComDesconto = valorTotal - desconto;
    return totalComDesconto;
}

module.exports=calcularTotalComDesconto