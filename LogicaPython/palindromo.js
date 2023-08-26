

function is_palindromo(palavra){
    palavra = palavra.toLowerCase();
    var reversed = palavra.split('').reverse().join('');
    if(palavra === reversed) {
        return palavra+" é um palindromo";
    }
    return "Não é palindromo!";

}

console.log(is_palindromo("natan"));