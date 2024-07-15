pag11 = """
<div id="pag11">
    <h1>Welcome to Programming Languages</h1>
    <p>This page provides an overview of three popular programming languages: Java, HTML, and Python.</p>
</div>
"""

pag12 = """
<div class="row">
    <div class="col-sm">
        <div class="card card-equal text-white bg-primary mb-3">
            <img class="card-img-top" src="java.png" alt="Java">
            <div class="card-body">
                <h5 class="card-title">Java</h5>
                <p class="card-text">Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is widely used for building enterprise-scale applications.</p>
                <p><a href="https://www.java.com" target="_blank" class="btn btn-light">Per maggiori informazioni sul linguaggio Java</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm">
        <div class="card card-equal text-white bg-success mb-3">
            <img class="card-img-top" src="html.jpg" alt="HTML">
            <div class="card-body">
                <h5 class="card-title">HTML</h5>
                <p class="card-text">HTML (HyperText Markup Language) is the standard markup language for creating web pages and web applications. It is the foundation of web content and provides the basic structure of websites.</p>
                <p><a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank" class="btn btn-light">Per maggiori informazioni sul linguaggio HTML</a></p>
            </div>
        </div>
    </div>
    <div class="col-sm">
        <div class="card card-equal text-white bg-warning mb-3">
            <img class="card-img-top" src="python.png" alt="Python">
            <div class="card-body">
                <h5 class="card-title">Python</h5>
                <p class="card-text">Python is an interpreted, high-level, general-purpose programming language.It is widely used in data science, machine learning, web development, and automation.</p>
                <p><a href="https://www.python.org" target="_blank" class="btn btn-light">Per maggiori informazioni sul linguaggio Python</a></p>
            </div>
        </div>
    </div>
</div>
"""

pag13 = """
<div id="pag13">
    <h2>Contact Us</h2>
    <p>If you have any questions or would like more information about these programming languages, please contact us at info@programminglanguages.com.</p>
</div>
"""

n = 5
pagina = pag11 + (n * pag12) + pag13

complete_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programming Languages Overview</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="stile.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        {pagina}
    </div>
</body>
</html>
"""

with open('Lezione2/Esercizio1/index.html', 'w') as file:
    file.write(complete_html)


