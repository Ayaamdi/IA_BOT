
import random

recettes = {
    "طاجين الدجاج": {
        "ingredients": ["الدجاج", "البطاطا", "البصلة", "الزيتون"],
        "preparation": "شحري البصلة مع الدجاج والتوابل، زيدي البطاطا والزيتون وشوية الماء وخليه يطيب."
    },

    "الكسكس": {
        "ingredients": ["الكسكس", "الجزر", "القرعة", "الحمص", "اللحم"],
        "preparation": "وجدي المرق بالخضر واللحم والحمص، وفوري الكسكس حتى يطيب."
    },

    "المسمن": {
        "ingredients": ["الدقيق", "الفينو", "الزيت", "الزبدة"],
        "preparation": "خلطي الدقيق والفينو والماء والملح، دلكي العجين، سرحيه وطيبيه فالمقلة."
    },

    "المعكرونة": {
        "ingredients": ["المعكرونة", "مطيشة", "الفرماج", "البصلة"],
        "preparation": "طيبي المعكرونة، وجدي صلصة المطيشة والبصلة وزيدي الفرماج."
    },

    "البيض بالطماطم": {
        "ingredients": ["البيض", "مطيشة", "البصلة", "الفلفلة"],
        "preparation": "شحري البصلة والفلفلة والمطيشة، زيدي البيض وخليه يطيب."
    },

    "سلطة مغربية": {
        "ingredients": ["مطيشة", "الخيار", "البصلة"],
        "preparation": "قطعي الخضر صغار، زيدي الملح والزيت والزيتون والحامض."
    }
}


def bot_cuisine():

    print("\n" + "=" * 35)
    print("🍲 مرحبا بيك فـ مساعد المطبخ ديالك!")
    print("=" * 35)

    nom = input("\nشنو سميتك؟ ")

    print("\nمرحبا", nom, "❤️")
    print("أنا هنا باش نعاونك تختاري شنو تطيبي اليوم!")

    while True:

        print("\nشنو بغيتي ندير ليك؟")
        print("1 - نقترح عليك طبخة حسب المكونات اللي عندك")
        print("2 - نختار ليك طبخة عشوائية")
        print("3 - نشوفو جميع الوصفات")
        print("4 - نخرج")

        choix = input("\nاختاري رقم: ")

        if choix == "1":

            print("\nشنو عندك فالدار؟")
            print("كتبي المكونات وفرقي بينهم بفاصلة.")

            ingredients = input("🥕 المكونات ديالك: ")
            ingredients = [
                i.strip() for i in ingredients.split(",")
            ]

            suggestions = []

            for nom_recette, details in recettes.items():

                communs = set(ingredients) & set(details["ingredients"])

                if len(communs) >= 2:
                    suggestions.append((nom_recette, len(communs)))

            suggestions.sort(key=lambda x: x[1], reverse=True)

            if suggestions:

                print("\n😍 لقيت ليك هاد الاقتراحات:")

                for recette, score in suggestions:

                    print("\n🍽️", recette)
                    print("المكونات المتوفرة:", score)
                    print("طريقة التحضير:")
                    print(recettes[recette]["preparation"])

            else:
                print("\n😅 مع الأسف ما لقيتش وصفة مناسبة.")
                print("جربي دخلي مكونات أخرى.")

        elif choix == "2":

            recette = random.choice(list(recettes.keys()))

            print("\n❤️ اليوم اخترت ليك:")
            print("🍽️", recette)

            print("\nالمكونات:")
            print(", ".join(recettes[recette]["ingredients"]))

            print("\nطريقة التحضير:")
            print(recettes[recette]["preparation"])

        elif choix == "3":

            print("\n📖 هادي هي الوصفات اللي عندي:")

            for recette in recettes:
                print("🍴", recette)

        elif choix == "4":

            print("\nبالصحة والراحة ❤️")
            print("إلى اللقاء!")
            break

        else:
            print("\nاختيار غير صحيح، عاودي جربي 😊")


bot_cuisine()
