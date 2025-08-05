const express = require("express");
const router = express.Router();

// Landing page route.
router.get("/", (req,res) => {
    res.render("main", {pieceOfMusic: fakeAPI()});
});

const fakeAPI = () => {
    return [
        {
            composer: "Johannes Brahms",
            title: "Intermezzo Opus. 118, No. 2", 
            year: 1878,
            imgExt: function() {
                return this.title.split(" ").join("")
            }
        },
        {
            composer: "Johann Sebastian Bach",
            title: "Toccata and Fugue in E minor",
            year: 1705,
            imgExt: function() {
                return this.title.split(" ").join("")
            }
        },
        {
            composer: "Ludwig van Beethoven",
            title: "Piano Sonata in C# Minor (Moonlight)", 
            year: 1810,
            imgExt: function() {
                return this.title.split(" ").join("").replace("#", "sharp")
            }
        }
    ]
}

router.get("/contact", (req, res) => {
    res.render("contact");
});

router.get("/login", (req, res) => {
    res.render("login");
});

router.get("/searchResults", (req, res) => {
    res.render("searchResults");
});

router.get("/score", (req, res) => {
    res.render("score");
});

router.get("/music", (req, res) => {
    res.render("music");
});

router.get("/users", (req, res) => {
    res.render("users");
});

router.post('/main',function(req,res){
    let username = req.body.username,
    password = req.body.password;
    
    const sql = "SELECT username, password FROM users";

    // get a connection from the pool
    res.locals.pool.getConnection(function(err, connection) {
        if(err) { console.log(err); return; }
        // make the query
        connection.query(sql, [username, password], function(err, results) {
            connection.release();
            if(err) { console.log(err); callback(true); return; }
            this.message = "hello";
            for (let i = 0; i < results.length; i++){
                if (results[i].username == username && results[i].password == password){
                    let message = "logged in"
                    let loggedIn = true;
                    res.render("main", {message, loggedIn, pieceOfMusic: fakeAPI()});
                    return;
                };
                message = "Please try again."
                res.render("login", {message});
            };
        });
    });
 });

module.exports = router;