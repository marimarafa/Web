const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//pagina di invio della form
app.get('/', (req, res) => {
    console.log("Mi hai chiesto la form di registrazione");
    res.sendFile("formSemplice.html", { root: './htdoc' });
    });

//pagina di gestione dei dati della form se il metodo è GET
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname);
    console.log(req.body.fcognome);
    res.send("<html>Buona serata "+ req.query.fname +" "+ req.query.fcognome + "</html>");
    })

app.post('/mansendfile', (req, res) => {
    password_ricevuta = req.query.password;
    if(password_ricevuta == "paperino")
        res.send("<html>Bravo "+ req.query.fname + "<br> sono pronto a ricevere il file </br> </html>")
    });