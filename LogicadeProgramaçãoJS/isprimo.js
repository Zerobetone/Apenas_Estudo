function isprime(number){
    if(number<=1){
        return false
    }
    
        for(let i =2 ; i<=Math.sqrt(number);i++){
            if(number%i === 0){
                return  false;
            }
            
             }
             return true;
}

function resposta(retorno){
    if(retorno==true){
        return " não é um valor primo";
    }
    return " é primo";
}

var n=4;
var valor_resposta= isprime(n);
console.log(resposta("O número "+ n + valor_resposta));