
const container = document.getElementById("recipes-container");
const message = document.getElementById("message");

// عرض الوصفات
function displayRecipes(recettes) {

    container.innerHTML = "";

    if (recettes.length === 0) {
        message.innerText = "😢 ما لقيتش وصفة مناسبة، جربي مكونات أخرى.";
        return;
    }

    message.innerText = "😍 ها شنو لقيت ليك!";

    recettes.forEach((recette, index) => {

        const card = document.createElement("div");
        card.className = "recipe-card";

        card.innerHTML = `
            <img src="${recette.image}" alt="${recette.nom}">

            <div class="recipe-info">
                <h3>${recette.nom}</h3>

                <p>${recette.description}</p>

                <p>⏱️ ${recette.temps}</p>

                <button onclick="showRecipe(${index})">
                    شوف طريقة التحضير
                </button>
            </div>
        `;

        container.appendChild(card);
    });

    window.currentRecipes = recettes;
}

// جلب جميع الوصفات
async function loadRecipes() {

    try {
        const response = await fetch("/recettes");
        const recettes = await response.json();

        displayRecipes(recettes);

    } catch (error) {
        message.innerText = "وقع مشكل فالاتصال بالسيرفر.";
    }
}

// البحث بالمكونات
async function searchRecipes() {

    const ingredients = document
        .getElementById("ingredients").value;

    if (ingredients.trim() === "") {
        message.innerText = "عافاك دخلي المكونات ديالك ❤️";
        return;
    }

    try {
        const response = await fetch("/chercher", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                ingredients: ingredients
            })
        });

        const recettes = await response.json();

        displayRecipes(recettes);

    } catch (error) {
        message.innerText = "وقع مشكل، عاودي المحاولة.";
    }
}

// اختيار طبخة عشوائية
async function randomRecipe() {

    try {
        const response = await fetch("/aleatoire");
        const recette = await response.json();

        displayRecipes([recette]);

        message.innerText = "🎉 هادي هي الطبخة اللي اخترت ليك اليوم!";

    } catch (error) {
        message.innerText = "وقع مشكل، عاودي المحاولة.";
    }
}

// عرض طريقة التحضير
function showRecipe(index) {

    const recette = window.currentRecipes[index];

    alert(
        "🍲 " + recette.nom +
        "\n\nالمكونات:\n" +
        recette.ingredients.join("، ") +
        "\n\nطريقة التحضير:\n" +
        recette.preparation
    );
}

// تشغيل التطبيق
loadRecipes();
