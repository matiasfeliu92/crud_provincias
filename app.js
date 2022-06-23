const express = require('express')
const morgan = require('morgan')
const router = require('./routes/router')
const router1 = require('./routes/router1')
const cors = require('cors')
const app = express()

//SETEAMOS EL PUERTO DE LA APP
app.set("port", process.env.PORT || 4000);

//SETEAMOS EL MOTOR DE PLANTILLAS
app.set("view engine", "ejs");

app.use(morgan("dev"));

app.use(express.urlencoded({ extended: false }));
app.use(express.json())
app.use(cors({
    origin:['http://127.0.0.1:5500'],
    credentials:true
}))

app.use("/provincias", router);
app.use("/ciudades", router1);

// app.get("/", (req, res) => {
//   res.send("Welcome to my API Library");
// });

app.listen(app.get("port"), () => {
  console.log("http://localhost:" + app.get("port"));
});