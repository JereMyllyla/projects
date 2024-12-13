'use strict';

// Loop to add event listeners to each button.
// Each button calls 'processRoll' function with it's corresponding value.
const diceButtons = ["d2_btn", "d4_btn", "d6_btn", "d8_btn", "d10_btn", "d12_btn", "d20_btn", "d100_btn"];
diceButtons.forEach(buttonId => {
    document.getElementById(buttonId).addEventListener("click", () => {
        processRoll(document.getElementById(buttonId).value);
    });
});

document.querySelectorAll('input[name="roll_type"]').forEach(radio => {
    radio.addEventListener("change", () => {
        const multiple_dice_amount = document.getElementById("multiple_dice_amount");

        if (document.getElementById("roll_type_multiple").checked) {
            showHiddenElement(multiple_dice_amount);
        } else {
            hideElement(multiple_dice_amount);
        }
    });
});

// Makes reset button hide dice amount as well
document.getElementById("reset_btn").addEventListener("click", () => {
    const multiple_dice_amount = document.getElementById("multiple_dice_amount");
    hideElement(multiple_dice_amount);
});

function showHiddenElement(element) {
    element.classList.remove("hidden");
};

function hideElement(element) {
    element.classList.add("hidden");
};

document.getElementById("settings_button").addEventListener("click", () => {
    const settings = document.getElementById("settings");
    settings.classList.toggle("hidden");
    const history = document.getElementById("roll_history");
    hideElement(history);
});

document.getElementById("history_btn").addEventListener("click", () => {
    const history = document.getElementById("roll_history");
    history.classList.toggle("hidden");
});

function updateElement(id, value) {
    document.getElementById(id).innerHTML = value;
};


// Dice rolling functions

function rollDie(die_max) {
    return Math.floor((Math.random()* die_max) +1);
};

function regularRoll(die_max, mod) {
    const num = rollDie(die_max);
    const total_num = num + mod;
    return {num, total_num};
};

function advantageRoll(die_max, mod) {
    const num1 = rollDie(die_max);
    const num2 = rollDie(die_max);

    const num = Math.max(num1, num2);
    const unused_num = Math.min(num1, num2);
    const total_num = num + mod;

    return {num, unused_num, total_num};
};

function disadvantageRoll(die_max, mod) {
    const num1 = rollDie(die_max);
    const num2 = rollDie(die_max);

    const num = Math.min(num1, num2);
    const unused_num = Math.max(num1, num2);
    const total_num = num + mod;

    return {num, unused_num, total_num};
};

function getDiceAmount() {
    let die_amount = document.getElementById("multiple_dice_amount").value;
    // make sure dice amount within 1-100
    if (die_amount < 1) {
        die_amount = 1;
        document.getElementById("multiple_dice_amount").value = die_amount;
    } else if (die_amount > 100) {
        die_amount = 100;
        document.getElementById("multiple_dice_amount").value = die_amount;
    };
    return die_amount;
};

function multipleRoll(die_max, mod) {
    const die_amount = getDiceAmount();
    let num = 0;

    for (let i = 0; i < die_amount; i++) {
        let num_rolled = rollDie(die_max);
        num += num_rolled;
    };
    const total_num = num + mod;
    return {num, total_num};
};

// make sure mod within -100-100 
function getMod() {
    let mod = document.getElementById("modifier_number").value;
    if (mod != "") {
        mod = parseInt(mod);
        if (mod < -100) {
            mod = -100;
            document.getElementById("modifier_number").value = mod;
        } else if (mod > 100) {
            mod = 100;
            document.getElementById("modifier_number").value = mod;
        };
    } else {
        mod = 0;
    };
    return mod;
};

function setModMarker(mod) {
    return mod < 0 ? "" : "+";
};

let roll_number = 1; // Not good to have a global variable
function addToHistory (result, die_max, mod, roll_type) {
    const mod_mark = setModMarker(mod);
    if (roll_type === "advantage" || roll_type === "disadvantage") {
        document.getElementById("roll_history").innerHTML += `<p class="log_entry">Roll ${roll_number}: 2d${die_max} => ${result.num} (${result.unused_num}) ${mod_mark} ${mod} = ${result.total_num}</p> <br>`;
    } else if (roll_type === "multiple") {
        const die_amount = getDiceAmount();
        document.getElementById("roll_history").innerHTML += `<p class="log_entry">Roll ${roll_number}: ${die_amount}d${die_max} => ${result.num} ${mod_mark} ${mod} = ${result.total_num}</p> <br>`;
    } else {
        document.getElementById("roll_history").innerHTML += `<p class="log_entry">Roll ${roll_number}: 1d${die_max} => ${result.num} ${mod_mark} ${mod} = ${result.total_num}</p> <br>`;
    };  
    roll_number += 1;
};

function getRollResult(roll_type, die_max, mod) {
    let result = {};
    if (roll_type === "advantage") {
        result = advantageRoll(die_max, mod);
        result.display = `${result.num} (${result.unused_num})`;
    } else if (roll_type === "disadvantage") {
        result = disadvantageRoll(die_max, mod);
        result.display = `${result.num} (${result.unused_num})`;
    } else if (roll_type === "multiple") {
        result = multipleRoll(die_max, mod);
        result.display = `${result.num}`;
    } else {
        result = regularRoll(die_max, mod);
        result.display = `${result.num}`;
    }
    return result;
};

function setRollResult(mod, total, display) {
    updateElement("roll_result", display);
    updateElement("mod", mod);
    updateElement("result", total);
};

function shakeDieLogo() {
    const dieIcon = document.querySelector("#top_die i");
    const animation_duration = 1500; // Set the animation duration in ms
    dieIcon.classList.add("fa-shake");
    dieIcon.style.setProperty("--fa-animation-duration", `${animation_duration}ms`);
    setTimeout(() => {
        dieIcon.classList.remove("fa-shake");
    }, animation_duration);
};

function processRoll(die_max) {
    const mod = getMod();
    const roll_type = document.querySelector('input[name="roll_type"]:checked').value;
    const result = getRollResult(roll_type, die_max, mod);

    setRollResult(mod, result.total_num, result.display);
    addToHistory(result, die_max, mod, roll_type);
    shakeDieLogo();
};





