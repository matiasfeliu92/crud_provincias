const mySql = require('mysql')

const conn = mySql.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: '',
    database: 'prov_arg',
})

conn.connect((err)=>{
    if(err){
        console.error('El error de conexion ' + err)
    } else{
        console.log('MySql is connected')
    }
})

module.exports = conn