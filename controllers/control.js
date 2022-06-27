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

control.getView1 = (req, res) => {
    conn.query('SELECT ciudades.nombre AS ciudad, provincias.nombre AS prov, ciudades.poblacion_hab AS pob_ciudad, ciudades.superficie_km2 AS sup_ciudad FROM provincias JOIN ciudades ON ciudades.ref_ciudad = provincias.id ORDER BY prov ASC', (err, result)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(result)
        } 
    })
}

control.getView_1 = (req, res) => {
    conn.query('SELECT *FROM prov_ciud', (err, result)=>{
        if(err){
            return res.status(403).json(err)
        } else {
            return res.status(200).json(result)
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