
from flask import Flask, render_template, request, jsonify
import random
import re
app = Flask(__name__)


recettes = [
    {
        "nom": "طاجين الدجاج بالزيتون",
        "categorie": "غداء",
        "ingredients": ["الدجاج", "البطاطا", "البصلة", "الزيتون"],
        "description": "طاجين مغربي تقليدي بنين.",
        "temps": "45 دقيقة",
        "image": "static/طاجين الدجاج بالزيتون.webp",
        "preparation": "شحري البصلة والدجاج مع التوابل، زيدي البطاطا والزيتون وشوية الماء وخليه يطيب."
    },
    {
        "nom": "الكسكس المغربي",
        "categorie": "غداء",
        "ingredients": ["الكسكس", "الجزر", "القرعة", "الحمص", "اللحم"],
        "description": "كسكس بالخضر واللحم.",
        "temps": "90 دقيقة",
        "image": "static/الكسكس المغربي.webp",
        "preparation": "وجدي المرق بالخضر واللحم والحمص، وفوري الكسكس حتى يطيب."
    },
    {
        "nom": "الحريرة",
        "categorie": "عشاء",
        "ingredients": ["العدس", "الحمص", "مطيشة", "القزبر", "الكرافس"],
        "description": "حريرة مغربية دافئة.",
        "temps": "60 دقيقة",
        "image": "static/الحريرة.webp",
        "preparation": "طيبي الحمص والعدس مع المطيشة والتوابل، زيدي القزبر والكرافس والتدويرة."
    },
    {
        "nom": "البسطيلة بالدجاج",
        "categorie": "غداء",
        "ingredients": ["الدجاج", "البصل", "البيض", "اللوز", "ورقة البسطيلة"],
        "description": "بسطيلة مغربية بالدجاج واللوز.",
        "temps": "75 دقيقة",
        "image": "static/البسطيلة بالدجاج.webp",
        "preparation": "طيبي الدجاج مع البصل والتوابل، وجدي الحشوة بالبيض واللوز، عمري الورقة ودخليها للفران."
    },
    {
        "nom": "المعكرونة بالفرماج",
        "categorie": "غداء",
        "ingredients": ["المعكرونة", "مطيشة", "الفرماج", "البصلة"],
        "description": "معكرونة سهلة وسريعة.",
        "temps": "25 دقيقة",
        "image": "static/المعكرونة بالفرماج.webp",
        "preparation": "طيبي المعكرونة، وجدي صلصة المطيشة والبصلة وزيدي الفرماج."
    },
    {
        "nom": "البيض بالطماطم",
        "categorie": "فطور",
        "ingredients": ["البيض", "مطيشة", "البصلة", "الفلفلة"],
        "description": "فطور مغربي بسيط وبنين.",
        "temps": "15 دقيقة",
        "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=600",
        "preparation": "شحري البصلة والفلفلة والمطيشة، زيدي البيض وخليه يطيب."
    },
    {
        "nom": "الرفيسة",
        "categorie": "غداء",
        "ingredients": ["الدجاج", "العدس", "البصل", "المسمن", "الحلبة"],
        "description": "رفيسة مغربية بالدجاج والعدس.",
        "temps": "90 دقيقة",
        "image": "static/الرفيسة.webp",
        "preparation": "طيبي الدجاج مع البصل والعدس والحلبة والتوابل، وقدميه فوق المسمن مقطع."
    },
    {
        "nom": "البيتزا المنزلية",
        "categorie": "عشاء",
        "ingredients": ["الدقيق", "مطيشة", "الفرماج", "الزيتون"],
        "description": "بيتزا بالفرماج والزيتون.",
        "temps": "40 دقيقة",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600",
        "preparation": "وجدي العجين، سرحيه، زيدي صلصة المطيشة والفرماج والزيتون ودخليه للفران."
    },
    {
        "nom": "سلطة مغربية",
        "categorie": "عشاء",
        "ingredients": ["مطيشة", "الخيار", "البصلة", "الفلفلة"],
        "description": "سلطة خفيفة ومنعشة.",
        "temps": "10 دقائق",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
        "preparation": "قطعي الخضر صغار، زيدي الملح والزيت والحامض وخلطي مزيان."
    },
    {
        "nom": "بطاطا محمرة",
        "categorie": "عشاء",
        "ingredients": ["البطاطا", "الثوم", "القزبر", "التوابل"],
        "description": "بطاطا محمرة بالتوابل.",
        "temps": "25 دقيقة",
        "image": "https://images.unsplash.com/photo-1518013431117-eb1465fa5752?w=600",
        "preparation": "قطعي البطاطا وطيبيها، ثم حمريها مع الثوم والقزبر والتوابل."
    },
    {
        "nom": "طاجين الكفتة",
        "categorie": "غداء",
        "ingredients": ["الكفتة", "مطيشة", "البيض", "البصلة"],
        "description": "كفتة بالبيض وصلصة المطيشة.",
        "temps": "35 دقيقة",
        "image": "static/طاجين الكفتة.webp",
        "preparation": "وجدي صلصة المطيشة والبصلة، زيدي كويرات الكفتة، وفي الأخير زيدي البيض."
    },
    {
        "nom": "العدس",
        "categorie": "غداء",
        "ingredients": ["العدس", "مطيشة", "الثوم", "القزبر"],
        "description": "عدس مغربي بالتوابل.",
        "temps": "45 دقيقة",
        "image": "static/العدس.webp",
        "preparation": "طيبي العدس مع المطيشة والثوم والقزبر والتوابل حتى يعقاد المرق."
    },
    {
        "nom": "البغرير",
        "categorie": "فطور",
        "ingredients": ["السميدة", "الدقيق", "الخميرة", "العسل"],
        "description": "بغرير خفيف ومثقب.",
        "temps": "30 دقيقة",
        "image": "static/البغرير.webp",
        "preparation": "خلطي السميدة والدقيق والخميرة والماء، طيبي البغرير فمقلة وقدميه بالعسل."
    },
    {
        "nom": "المسمن",
        "categorie": "فطور",
        "ingredients": ["الدقيق", "الفينو", "الزبدة", "الزيت"],
        "description": "مسمن مغربي مورق.",
        "temps": "40 دقيقة",
        "image": "static/المسمن.webp",
        "preparation": "عجني الدقيق والفينو بالماء والملح، سرحي العجين بالزيت والزبدة وطيبيه فالمقلة."
    },
    {
        "nom": "بان كيك",
        "categorie": "فطور",
        "ingredients": ["الدقيق", "البيض", "الحليب", "السكر"],
        "description": "بان كيك طري وحلو.",
        "temps": "20 دقيقة",
        "image": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?w=600",
        "preparation": "خلطي الدقيق والبيض والحليب والسكر، وصبي الخليط فمقلة سخونة."
    },
    {
        "nom": "كيكة الشوكولاتة",
        "categorie": "حلويات",
        "ingredients": ["الدقيق", "البيض", "السكر", "الشوكولاتة"],
        "description": "كيكة بالشوكولاتة.",
        "temps": "45 دقيقة",
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600",
        "preparation": "خلطي البيض والسكر والدقيق والشوكولاتة، وصبي الخليط فالقالب ودخليه للفران."
    },
    {
        "nom": "شوربة الخضر",
        "categorie": "عشاء",
        "ingredients": ["الجزر", "البطاطا", "القرعة", "البصلة"],
        "description": "شوربة خضر صحية ودافئة.",
        "temps": "30 دقيقة",
        "image": "static/شوربة الخضر.webp",
        "preparation": "طيبي الخضر مع الماء والملح، ومن بعد طحنيهم حتى يولي الخليط كريمي."
    },
    {
        "nom": "ساندويتش الدجاج",
        "categorie": "عشاء",
        "ingredients": ["الدجاج", "الخبز", "الخس", "الفرماج"],
        "description": "ساندويتش سريع بالدجاج.",
        "temps": "20 دقيقة",
        "image": "static/ساندويتش الدجاج.webp",
        "preparation": "طيبي الدجاج بالتوابل، عمري الخبز بالدجاج والخس والفرماج."
    }
]
last_recette = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recettes")
def get_recettes():
    return jsonify(recettes)


@app.route("/chercher", methods=["POST"])

@app.route("/chercher", methods=["POST"])

@app.route("/chercher", methods=["POST"])

@app.route("/chercher", methods=["POST"])
def chercher():

    data = request.get_json()
    texte = data.get("ingredients", "").lower().strip()

    texte = texte.replace("،", ",")
    mots = re.split(r"[,;\s]+", texte)

    equivalences = {
        "btata": "البطاطا",
        "batata": "البطاطا",
        "basla": "البصلة",
        "bsla": "البصلة",
        "sbla": "البصلة",
        "djaj": "الدجاج",
        "djej": "الدجاج",
        "khizo": "الجزر",
        "maticha": "مطيشة",
        "bid": "البيض"
    }

    ingredients = [
        equivalences.get(mot, mot)
        for mot in mots if mot
    ]

    resultats = []

    for recette in recettes:

        composants = [
            i.lower() for i in recette["ingredients"]
        ]

        # خاص جميع المكونات المدخلة تكون موجودة
        if all(i in composants for i in ingredients):
            resultats.append(recette)

    return jsonify(resultats)





@app.route("/aleatoire")

@app.route("/aleatoire")
def aleatoire():

    global last_recette

    choix = [
        recette for recette in recettes
        if recette["nom"] != last_recette
    ]

    recette = random.choice(choix)

    last_recette = recette["nom"]

    return jsonify(recette)
if __name__ == "__main__":
    app.run(debug=True)
