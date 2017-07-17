$(document).ready(function(){
//necesario para que funcione las peticiones post con ajax y django
  function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
//
   $(".actualizar").click(function(){
    var url = "/cliente/actualizar";
    $.ajax({
      type: "GEST",
      url: url,
      beforeSend: function(){
        $("#resultado").html("procesando...");
      },
      success: function (response){
        personas=JSON.parse(response)
        for (var i in personas){
          nuevafila="<tr><td>"+personas[i].fields.cedula+
          "</td><td>"+personas[i].fields.nombre+personas[0].fields.apellido+
          "</td><td>"+personas[i].fields.correo+"</td><td><button class=\"eliminar\">E</button></td></tr>";
          $("#tablaprueba").append(nuevafila);
          $("#resultado").html("");
        }
      }
    });
   });

   $(".eliminar").click(function(){
     console.log("si");
     var url = "/cliente/eliminacion";
     $.ajax({
       type:"POST",
       url: url,
       data: {"cedula":1032462924},
       beforeSend: function(){
         console.log("esperadno");
       },
       success: function (response){
         console.log(response)
       }
     });
   });
});
