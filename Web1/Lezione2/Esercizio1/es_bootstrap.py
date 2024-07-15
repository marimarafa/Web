pag1 = """
<div class="col-sm">
    <div class="card">
        <img class="card-img-top" src="java.png" alt="Java">
        <div class="card-body">
            <h5 class="card-title">Java</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
    </div>
</div>
"""

pag2 = """
<div class="col-sm">
    <div class="card">
        <img class="card-img-top" src="html.jpg" alt="Html">
        <div class="card-body">
            <h5 class="card-title">Html</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
    </div>
</div>
"""

pag3 = """
<div class="col-sm">
    <div class="card">
        <img class="card-img-top" src="python.png" alt="Python">
        <div class="card-body">
            <h5 class="card-title">Python</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
    </div>
</div>
"""



with open("Web1/Lezione2/Esercizio1/index.html", "w") as file:
    n = 2
    pagina = '<div class="row">' + pag1 + (n * pag2) + pag3 + '</div>'

    pagina_html = f"""<!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <link href="stile.css" rel="stylesheet">
            <title>Site</title>
        </head>
        <body>
            <div class="container">
                {pagina}
            </div>
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        </body>
    </html>
    """
    file.write(pagina_html)
#cckewea
