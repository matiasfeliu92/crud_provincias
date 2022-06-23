const conn = require('../database/db')

const control = {}

control.getAll = (req,res) => {
    conn.query('SELECT * FROM provincias', (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

control.insert = (req, res) => {
    const provincia = req.body
    console.log(provincia)
    conn.query('INSERT INTO provincias SET ?', [provincia], (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

control.update = (req, res) => {
    const id = req.params.id
    const provincia = req.body
    console.log(provincia)
    conn.query('UPDATE provincias SET ? WHERE id = ?', [provincia, id], (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

module.exports = control