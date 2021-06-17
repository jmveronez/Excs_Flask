const pessoa = {
    nome: 'Betão',
    sobrenome: 'Einstein',
    idade: 42,
    doido: true,
    imagem_doido: 'https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg',
    imagem_serio: 'https://upload.wikimedia.org/wikipedia/commons/5/50/Albert_Einstein_%28Nobel%29.png'
}

const nome = document.querySelector("#nome");
const sobrenome = document.querySelector("#sobrenome");
const idade = document.querySelector("#idade");
const botao = document.querySelector("#altera_humor");

nome.innerText = pessoa.nome;
sobrenome.innerText = pessoa.sobrenome;
idade.innerText = pessoa.idade;

function atualizaHumor(){
    pessoa.doido = !pessoa.doido;
    const imagem = document.querySelector("#imagem");
    const humor = document.querySelector("#bloco_humor");

    if (pessoa.doido){
        imagem.src = pessoa.imagem_doido;
        humor.innerHTML = pessoa.nome + " <b>ENDOIDOU!</b>"
    }
    else{
        imagem.src = pessoa.imagem_serio;
        humor.innerHTML = pessoa.nome + " <b>EMBURROU!</b>"
    }
}

atualizaHumor();

botao.addEventListener('click', atualizaHumor);