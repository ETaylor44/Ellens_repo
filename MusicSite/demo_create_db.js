const mysql = require('mysql2');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Ruskiedog44",
  database: "mysql"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT username, password FROM users", function (err, result, fields) {
    if (err) throw err;
    for (i = 0; i < result.length; i++){
      if (result[i].username == "admin" && result[i].password == 'password'){
        console.log("Logged in");
      }
    }
  });
});

console.log("message")

