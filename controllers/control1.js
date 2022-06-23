const conn = require('../database/db')

const control = {}

control.getAll = (req,res) => {
    conn.query('SELECT * FROM ciudades', (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

control.insert = (req, res) => {
    const ciudad = req.body
    console.log(ciudad)
    conn.query('INSERT INTO ciudades SET ?', [ciudad], (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

control.update = (req, res) => {
    const id = req.params.id
    const ciudad = req.body
    console.log(ciudad)
    conn.query('UPDATE ciudades SET ? WHERE id = ?', [ciudad, id], (err, resultado)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(resultado)
        } 
    })
}

module.exports = control