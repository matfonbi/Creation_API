from flask import Flask, request, render_template_string

app = Flask(__name__)

# Page HTML avec formulaire pour entrer deux nombres
HTML_FORM = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Somme de deux nombres</title>
</head>
<body>
    <h1>Entrez deux nombres pour calculer leur somme</h1>
    <form method="POST" action="/api/v1/add">
        <label for="num1">Nombre 1 :</label>
        <input type="number" id="num1" name="num1" required>
        <br><br>
        <label for="num2">Nombre 2 :</label>
        <input type="number" id="num2" name="num2" required>
        <br><br>
        <button type="submit">Calculer</button>
    </form>
    {% if result is not none %}
        <h2>Résultat : {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/api/v1/add', methods=["GET", "POST"])
def add_numbers():
    result = None
    if request.method == "POST":
        try:
            # Récupérer les nombres du formulaire
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))

            # Calculer la somme
            result = num1 + num2
        except ValueError:
            result = "Entrées invalides, veuillez entrer des nombres valides."

    # Afficher le formulaire HTML avec le résultat (si calcul effectué)
    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
