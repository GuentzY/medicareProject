$(function(){
    var $registerForm = $("#frmContact");
    if($registerForm.length){
        $registerForm.validate({
            rules:{
                txtNombreCompleto:{
                    required: true
                },
                txtRut: {
                    required: true
                },
                txtTelefono: {
                    required: true
                },
                txtEmail: {
                    required: false
                }
            },
            messages:{
                txtNombreCompleto:{
                    required: 'Por favor, ingrese un nombre válido'
                },
                txtRut: {
                    required: 'Ingrese su RUT'
                },
                txtTelefono: {
                    required: 'Ingrese un numero de contacto'
                },
                txtEmail: {
                    required: 'Ingrese un correo válido!'
                }
            }
        })
    }
})
