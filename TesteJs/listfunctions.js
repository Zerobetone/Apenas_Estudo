
function sum(numbers){
    let soma = 0;
    numbers.forEach(number => {
        soma += number;
    });
    return soma;
};


function average(numbers){

    return (sum(numbers))/numbers.length;    
};


function max(numbers){
    let maior = numbers[0];
    numbers.forEach(number=>{
        if(maior<number){
            maior= number;
        }

    });
    return maior;
}


function min(numbers){
    let menor = numbers[0];
    numbers.forEach(number=>{
        if(menor>number){
            menor= number;
        }

    });
    return menor;
}

module.exports = {
    sum: sum,
    average: average,
    max: max,
    min: min
};



