let currentPosition = [0,1];
let motATrouver = document.querySelector("#motATrouver").textContent;

// function encodeWord who takes word as parameter and return the word encoded
function encodeWord(word) {
    let wordEncoded = "";
    for (let i = 0; i < word.length; i++) {
        if (i === 0) {
            wordEncoded += word.charAt(i).toUpperCase();
        } else {
            wordEncoded += '.';
        }
    }
    return wordEncoded;
}

document.querySelector("#motATrouver").textContent = encodeWord(motATrouver);



function getUserWordWritten(positionRow, lengthY) {
    let wordUser = "";
    for (let j = 0; j < lengthY; j++) {
        wordUser += document.getElementsByTagName("tr")[positionRow].children.item(j).textContent.toUpperCase();
    }
    return wordUser;
}

function verifyChar(char, word, position){
    let tab_word = word.toString().split('');
    for (let chars of tab_word) {
        if(char.toUpperCase() === chars.toUpperCase()) {
            // console.log(char.toUpperCase() === tab_word[position].toUpperCase())
            return char.toUpperCase() === tab_word[position].toUpperCase();
        }
    }
}

function delayedLoop(index, indice, nombre_colonnes, nombre_lignes) {
    if (index < nombre_colonnes) {
        // On récupère la lettre de la ligne
        let letterLine = document.getElementsByTagName("tr")[indice].children.item(index).textContent.toUpperCase();

        // Si la lettre de la ligne est dans le mot mais mal placée
        if (verifyChar(letterLine, motATrouver, index) === false) {
            // On met la lettre en jaune
            document.getElementsByTagName("tr")[indice].children.item(index).classList.add("mal-place");
            for (let index = 0; index < document.querySelectorAll(".input-lettre").length; index++) {
                if (document.querySelectorAll(".input-lettre")[index].textContent === letterLine) {
                    document.querySelectorAll(".input-lettre")[index].classList.add("lettre-mal-place");
                    break;
                }
            }
        }

        // Si la lettre de la ligne est dans le mot et bien placée
        if (verifyChar(letterLine, motATrouver, index) === true) {
            // On met la lettre en rouge
            document.getElementsByTagName("tr")[indice].children.item(index).classList.add("bien-place");
            for (let index = 0; index < document.querySelectorAll(".input-lettre").length; index++) {
                if (document.querySelectorAll(".input-lettre")[index].textContent === letterLine) {
                    document.querySelectorAll(".input-lettre")[index].classList.remove("lettre-mal-place");
                    document.querySelectorAll(".input-lettre")[index].classList.add("lettre-bien-trouve");
                    break;
                }
            }
        }

        // Si la lettre n'est pas dans le mot
        if (verifyChar(letterLine, motATrouver, index) === undefined) {
            // On ne fait rien
            document.getElementsByTagName("tr")[indice].children.item(index).classList.add("non-trouve");
            for (let index = 0; index < document.querySelectorAll(".input-lettre").length; index++) {
                if (document.querySelectorAll(".input-lettre")[index].textContent === letterLine) {
                    document.querySelectorAll(".input-lettre")[index].classList.remove("lettre-mal-place");
                    document.querySelectorAll(".input-lettre")[index].classList.add("lettre-non-trouve");
                    break;
                }
            }
        }

        index++;
        setTimeout(() => delayedLoop(index, indice, nombre_colonnes, nombre_lignes), 200);
    } else {
        for (let k = 0; k < nombre_colonnes; k++) {
            if (indice + 1 < nombre_lignes) {
                if (k === 0) {
                    document.getElementsByTagName("tr")[indice + 1].children.item(k).textContent = motATrouver.charAt(0).toUpperCase();
                }
                else if (document.getElementsByTagName("tr")[indice].children.item(k).classList.contains("bien-place")) {
                    document.getElementsByTagName("tr")[indice + 1].children.item(k).textContent = motATrouver.charAt(k).toUpperCase();
                } else {
                    document.getElementsByTagName("tr")[indice + 1].children.item(k).textContent = '.';
                }
            }
        }


        document.getElementsByTagName("tr")[indice].classList.add("not_playable_row");
        document.getElementsByTagName("tr")[indice + 1].classList.remove("not_playable_row");
    }
}

document.addEventListener('click', (event) => {
    let win = true;
    let row = 0;
    let contain_false = [];
    if (event.target.classList.contains("input-lettre")) {
        // console.log(event.target.textContent);
        const nb_rows = document.getElementsByTagName("tr").length;
        const nb_columns = document.getElementsByTagName("td").length / nb_rows;

        // On parcourt les lignes pour trouver la ligne jouable
        for(let i = 0; i < nb_rows; i++) {
            // Si la ligne est jouable
            if (document.getElementsByTagName("tr")[i].classList.contains("not_playable_row") === false) {
                // On parcourt les colonnes en partant de la colonne après la première lettre
                for (let j = 1; j < nb_columns; j++) {

                    if(event.target.textContent === '⌫') {
                        // Si on est sur la dernière colonne ou si la case suivante est vide
                        if ((j + 1 === nb_columns) || document.getElementsByTagName("tr")[i].children.item(j + 1).textContent === '.') {
                            document.getElementsByTagName("tr")[i].children.item(j).textContent = '.';
                            document.getElementsByTagName("tr")[i].classList.remove("full_leter");
                            break;
                        }
                    }

                    // Si la touche appuyée est "Enter"
                    if (event.target.textContent === '↲' && document.getElementsByTagName("tr")[i].classList.contains("full_leter")) {
                        // On boucle pour chaque colonne de la ligne pour comparer les lettres
                        delayedLoop(0, i, nb_columns, nb_rows);

                        setTimeout(() => {
                            if (document.getElementsByTagName("tr")[i].children.item(j).classList.contains("bien-place")) {
                                contain_false.push(true);
                            } else {
                                contain_false.push(false);
                            }
                        }, 2500);

                        setTimeout(() => {
                            win = !contain_false.includes(false);
                        }, 3500);

                        setTimeout(() => {
                            if (win) {
                                let array = []
                                document.querySelector("#state_win").textContent = "Bravo, tu as gagné !";
                                document.querySelector("#word_to_find").innerHTML = "'" + motATrouver + "'";
                                document.querySelector("#nb_try").textContent = "'" + (i + 1) + "'";
                                if (row < 7) {
                                    for (let h = 1; h < nb_columns + 1; h++) {
                                        let span = document.createElement("span");
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("bien-place")) {
                                            span.textContent = "🟥";
                                            array.push("🟥")
                                        }
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("mal-place")) {
                                            span.textContent = "🟡";
                                            array.push("🟡");
                                        }
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("non-trouve") ||
                                            document.getElementsByTagName("tr")[row].children.item(h - 1).classList.length === 0) {
                                            span.textContent = "🟦";
                                            array.push("🟦");
                                        }
                                        document.querySelector("#game-resume-r-" + (j)).appendChild(span);
                                    }
                                    console.log(array)
                                    row++
                                    document.querySelector("#modal-container").style.display = 'flex';
                                }

                                for (let k = 0; k < document.querySelectorAll("option").length ; k++) {
                                    if (document.querySelectorAll("option")[k].text === motATrouver.toUpperCase()) {
                                        // console.log(document.querySelectorAll("option")[k].value)
                                        document.querySelector("#id_word").value = document.querySelectorAll("option")[k].value;
                                    }
                                }

                                document.querySelector('#id_user').value = document.querySelector('#idCurrentUser').textContent
                                document.querySelector('[name=nb_try]').value = (i+1)
                                document.querySelector('[name=is_win]').checked = true

                                switch (i) {
                                    case 0: document.querySelector('[name=points]').value = 50;
                                        break;
                                    case 1: document.querySelector('[name=points]').value = 40;
                                        break;
                                    case 2: document.querySelector('[name=points]').value = 30;
                                        break;
                                    case 3: document.querySelector('[name=points]').value = 20;
                                        break;
                                    case 4: document.querySelector('[name=points]').value = 10;
                                        break;
                                    default: document.querySelector('[name=points]').value = 0;
                                }
                            }
                        }, 5000);
                    }

                    // Si la touche appuyée est autre que "Enter" ou "Backspace"
                    if (event.target.textContent !== '↲' && event.target.textContent !== '⌫') {
                        // Si la case est vide / Si la case contient un point
                        if (document.getElementsByTagName("tr")[i].children.item(j).textContent === '.') {
                            // On ajoute la lettre dans la case
                            document.getElementsByTagName("tr")[i].children.item(j).textContent = event.target.textContent;
                            // Si on se trouve sur la derniere colonne de la ligne
                            if (j === nb_columns - 1) {
                                // On passe la ligne en état (full_leter) qui permet de passer à la ligne suivante
                                document.getElementsByTagName("tr")[i].classList.add("full_leter");
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
});

document.addEventListener('keydown', (event) => {
    let win = true;
    let row = 0;
    let contain_false = [];
    var nomTouche = event.key;
    const authorized_keys = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n','Enter','Backspace']
    const nb_rows = document.getElementsByTagName("tr").length;
    const nb_columns = document.getElementsByTagName("td").length / nb_rows;

    // Si la touche appuyée est autorisée
    if(authorized_keys.includes(nomTouche)) {

        // On parcourt les lignes pour trouver la ligne jouable
        for(let i = 0; i < nb_rows; i++) {
            // Si la ligne est jouable
            if (document.getElementsByTagName("tr")[i].classList.contains("not_playable_row") === false) {
                // On parcourt les colonnes en partant de la colonne après la première lettre
                for (let j = 1; j < nb_columns; j++) {

                    if(nomTouche === 'Backspace') {
                        // Si on est sur la dernière colonne ou si la case suivante est vide
                        if ((j + 1 === nb_columns) || document.getElementsByTagName("tr")[i].children.item(j + 1).textContent === '.') {
                            document.getElementsByTagName("tr")[i].children.item(j).textContent = '.';
                            document.getElementsByTagName("tr")[i].classList.remove("full_leter");
                            break;
                        }
                    }

                    // Si la touche appuyée est "Enter"
                    if (nomTouche === 'Enter' && document.getElementsByTagName("tr")[i].classList.contains("full_leter")) {
                        // On boucle pour chaque colonne de la ligne pour comparer les lettres
                        delayedLoop(0, i, nb_columns, nb_rows);

                        setTimeout(() => {
                            if (document.getElementsByTagName("tr")[i].children.item(j).classList.contains("bien-place")) {
                                contain_false.push(true);
                            } else {
                                contain_false.push(false);
                            }
                        }, 2500);

                        setTimeout(() => {
                            win = !contain_false.includes(false);
                        }, 3500);

                        setTimeout(() => {
                            if (win) {
                                let array = []
                                document.querySelector("#state_win").textContent = "Bravo, tu as gagné !";
                                document.querySelector("#word_to_find").innerHTML = "'" + motATrouver + "'";
                                document.querySelector("#nb_try").textContent = "'" + (i + 1) + "'";
                                if (row < 7) {
                                    for (let h = 1; h < nb_columns + 1; h++) {
                                        let span = document.createElement("span");
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("bien-place")) {
                                            span.textContent = "🟥";
                                            array.push("🟥")
                                        }
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("mal-place")) {
                                            span.textContent = "🟡";
                                            array.push("🟡");
                                        }
                                        if (document.getElementsByTagName("tr")[row].children.item(h - 1).classList.contains("non-trouve") ||
                                            document.getElementsByTagName("tr")[row].children.item(h - 1).classList.length === 0) {
                                            span.textContent = "🟦";
                                            array.push("🟦");
                                        }
                                        document.querySelector("#game-resume-r-" + (j)).appendChild(span);
                                    }
                                    console.log(array)
                                    row++
                                    document.querySelector("#modal-container").style.display = 'flex';
                                }

                                for (let k = 0; k < document.querySelectorAll("option").length ; k++) {
                                    if (document.querySelectorAll("option")[k].text === motATrouver.toUpperCase()) {
                                        // console.log(document.querySelectorAll("option")[k].value)
                                        document.querySelector("#id_word").value = document.querySelectorAll("option")[k].value;
                                    }
                                }

                                document.querySelector('#id_user').value = document.querySelector('#idCurrentUser').textContent
                                document.querySelector('[name=nb_try]').value = (i+1)
                                document.querySelector('[name=is_win]').checked = true

                                switch (i) {
                                    case 0: document.querySelector('[name=points]').value = 50;
                                        break;
                                    case 1: document.querySelector('[name=points]').value = 40;
                                        break;
                                    case 2: document.querySelector('[name=points]').value = 30;
                                        break;
                                    case 3: document.querySelector('[name=points]').value = 20;
                                        break;
                                    case 4: document.querySelector('[name=points]').value = 10;
                                        break;
                                    default: document.querySelector('[name=points]').value = 0;
                                }
                            }
                        }, 5000);
                    }

                    // Si la touche appuyée est autre que "Enter" ou "Backspace"
                    if (nomTouche !== 'Enter' && nomTouche !== 'Backspace') {
                        // Si la case est vide / Si la case contient un point
                        if (document.getElementsByTagName("tr")[i].children.item(j).textContent === '.') {
                            // On ajoute la lettre dans la case
                            document.getElementsByTagName("tr")[i].children.item(j).textContent = nomTouche.toUpperCase();
                            // Si on se trouve sur la derniere colonne de la ligne
                            if (j === nb_columns - 1) {
                                // On passe la ligne en état (full_leter) qui permet de passer à la ligne suivante
                                document.getElementsByTagName("tr")[i].classList.add("full_leter");
                            }
                            let full_row = false;
                            for (let cases in document.getElementsByTagName("tr")[i].children) {
                                if (document.getElementsByTagName("tr")[i].children.item(cases).textContent === '.') {
                                    break;
                                } else {
                                    full_row = true;
                                }
                                if (full_row) {
                                    document.getElementsByTagName("tr")[i].classList.add("full_leter");
                                }
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
});


function generateTable() {
    // creates a <table> element and a <tbody> element
    const tbl = document.createElement("table");
    const tblBody = document.createElement("tbody");

    // creating all cells
    for (let i = 0; i < 6; i++) {
        // creates a table row
        const row = document.createElement("tr");

        for (let j = 0; j < motATrouver.length; j++) {
            // Create a <td> element and a text node, make the text
            // node the contents of the <td>, and put the <td> at
            // the end of the table row
            const cell = document.createElement("td");
            cell.id = (i+1) + '-' + (j+1);
            var cellText = document.createTextNode(`.`);
            var firstLetter = document.createTextNode(`${motATrouver.charAt(0).toUpperCase()}`);
            if (i > 0 && j > 0) {
                row.classList.add("not_playable_row");
            }
            if (i === 0 && j === 0) {
                cell.appendChild(firstLetter);
            }
            else if(i === 0 && j > 0){
                cell.appendChild(cellText);
            }
            row.appendChild(cell);
        }

        // add the row to the end of the table body
        tblBody.appendChild(row);
    }

    // put the <tbody> in the <table>
    tbl.appendChild(tblBody);
    // appends <table> into <body>
    var grille = document.getElementById("grille");
    grille.appendChild(tbl);
    // sets the border attribute of tbl to '2'
    // tbl.setAttribute("border", "2");

    document.querySelector("input").style.display = "none";
}

generateTable();