const express = require("express");
const app = express();
const port = 5000;
const handlebars = require("express-handlebars");
const mysql = require("mysql2");
var bodyParser = require('body-parser')

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies

require('dotenv').config();

app.set("view engine", "hbs");
app.engine("hbs", handlebars.engine({
    extname: "hbs",
    defaultLayout: "index"
}));

app.set('views', './views');

// Route to static pages
app.use(express.static("public"));
app.use(express.static('images'));

// Create DB connection pool
const pool = mysql.createPool({
    connectionLimit:    10,
    host:               process.env.DB_HOST,
    user:               process.env.DB_USER,
    password:           process.env.DB_PASS,
    database:           process.env.DB_NAME
  });


app.use(function(req, res, next) {
    res.locals.pool = pool;
    next();
  });

app.use('/', require('./server/routes/routes'));

app.listen(port, () => {
    console.log("listening on port " + port);
});