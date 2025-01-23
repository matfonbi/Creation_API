from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "NTg1kbgzlvPAqKo37dapqplkx6oiQZQgJ6UN9TCKRyk"
jwt = JWTManager(app)

# Base de données fictive avec produits et commentaires
products_data = {
    "iphone": [
        "Excellent produit, mais un peu cher.",
        "Bonne qualité, mais la batterie ne dure pas assez longtemps.",
        "Super appareil photo et design élégant.",
        "L'écran est incroyable, mais le prix est élevé.",
        "Je suis satisfait de mon achat, malgré le coût."
    ],
    "macbook": [
        "Puissant et rapide, idéal pour le travail.",
        "Très léger et facile à transporter.",
        "Un peu cher pour les spécifications.",
        "Le clavier est agréable à utiliser.",
        "La durée de vie de la batterie est excellente."
    ],
    "samsung": [
        "Rapport qualité-prix exceptionnel.",
        "La qualité de l'écran est impressionnante.",
        "La batterie dure toute la journée.",
        "Un bon choix pour Android.",
        "Un peu compliqué à configurer au début."
    ],
    "playstation": [
        "Les graphismes sont incroyables.",
        "Une large sélection de jeux.",
        "Un design moderne et cool.",
        "Le mode multijoueur est génial.",
        "Le prix est raisonnable pour ce qu'il offre."
    ],
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "password":
        return render_template('search.html')
    return "Identifiants incorrects", 401

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        product_name = request.form.get("product_name").lower()
        comments = products_data.get(product_name, ["Aucun commentaire trouvé pour ce produit."])
        return render_template('results.html', product_name=product_name, comments=comments)
    return render_template('search.html')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    product_name = request.form.get("product_name").lower()
    comment = request.form.get("comment")

    if product_name and comment:
        # Ajoute le commentaire au produit
        if product_name in products_data:
            products_data[product_name].append(comment)
        else:
            products_data[product_name] = [comment]

    # Recharge la page des résultats
    comments = products_data.get(product_name, ["Aucun commentaire trouvé pour ce produit."])
    return render_template('results.html', product_name=product_name, comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
