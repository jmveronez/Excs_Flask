const cardPokemons = document.querySelectorAll(".card_pokemon");
const pokemonSelecionado = document.querySelector("#pokemon_selecionado");

function selecionaPokemon(){
    const nomePokemon = this.getAttribute("data-nome");
    const numeroPokemon = this.getAttribute("data-numero")
    
    if(!this.classList.contains("selecionado")){
        if (numeroPokemon <= '003'){
            pokemonSelecionado.classList.add("um")
            pokemonSelecionado.classList.remove("dois")
            pokemonSelecionado.classList.remove("tres")
        } else if (numeroPokemon <= '006'){
            pokemonSelecionado.classList.add("dois")
            pokemonSelecionado.classList.remove("um")
            pokemonSelecionado.classList.remove("tres")
        } else if (numeroPokemon <= '009'){
            pokemonSelecionado.classList.add("tres")
            pokemonSelecionado.classList.remove("dois")
            pokemonSelecionado.classList.remove("um")
        }
        this.classList.add("selecionado");
        pokemonSelecionado.innerHTML = `O último Pokemon selecionado foi o <b>${nomePokemon}</b>`
    }
    else{
        this.classList.remove("selecionado");

        const pokemonsSelecionados = document.querySelectorAll(".selecionado")
        if (pokemonsSelecionados.length >= 1){
            pokemonSelecionado.innerHTML = `Você desselecionou o ${nomePokemon}. Ainda falta(m) ${pokemonsSelecionados.length} selecionados`
            if (numeroPokemon <= '003'){
                pokemonSelecionado.classList.add("um")
                pokemonSelecionado.classList.remove("dois")
                pokemonSelecionado.classList.remove("tres")
            } else if (numeroPokemon <= '006'){
                pokemonSelecionado.classList.add("dois")
                pokemonSelecionado.classList.remove("um")
                pokemonSelecionado.classList.remove("tres")
            } else if (numeroPokemon <= '009'){
                pokemonSelecionado.classList.add("tres")
                pokemonSelecionado.classList.remove("dois")
                pokemonSelecionado.classList.remove("um")
            }
        }else{
            pokemonSelecionado.innerHTML = "Selecione um Pokemon!"
            if (numeroPokemon <= '003'){
                pokemonSelecionado.classList.add("um")
                pokemonSelecionado.classList.remove("dois")
                pokemonSelecionado.classList.remove("tres")
            } else if (numeroPokemon <= '006'){
                pokemonSelecionado.classList.add("dois")
                pokemonSelecionado.classList.remove("um")
                pokemonSelecionado.classList.remove("tres")
            } else if (numeroPokemon <= '009'){
                pokemonSelecionado.classList.add("tres")
                pokemonSelecionado.classList.remove("dois")
                pokemonSelecionado.classList.remove("um")
            }
        }
    }
}

for(const cardPokemon of cardPokemons){
    cardPokemon.addEventListener("click", selecionaPokemon)
}