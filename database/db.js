const mySql = require('mysql')
require('dotenv').config()

const conn = mySql.createConnection({
    host: process.env.DB_HOST,
    port: 3306,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
})

conn.connect((err)=>{
    if(err){
        console.error('El error de conexion ' + err)
    } else{
        console.log('MySql is connected')
    }
})

module.exports = conn