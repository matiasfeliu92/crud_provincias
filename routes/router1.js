const express = require('express')
const router = express.Router()
const control = require('../controllers/control1')

router.get('/lista', control.getAll)
router.post('/insertar', control.insert)
router.post('/editar/:id', control.update)

module.exports = router