const express = require('express')
const router = express.Router()
const control = require('../controllers/control')

router.get('/lista', control.getAll)
router.get('/view1', control.getView1)
router.get('/view_1', control.getView_1)
router.post('/insertar', control.insert)
router.post('/editar/:id', control.update)

module.exports = router 