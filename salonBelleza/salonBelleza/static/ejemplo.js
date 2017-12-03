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

function actualizarTabla(){
  $("#tablaprueba").dataTable({
    "ajax":{url:"/cliente/actualizar"},
    "destroy":true,
    "columns":[
      {"data":"cedula"},
      {"data":"nombre"},
      {"data":"correo"},
      {"data":"botonE"},
      {"data":"botonA"}
    ]
  });
}
   $(".actualizar").click(function(){
     actualizarTabla();
   });

   $("#tablaprueba").on("click","button.eliminar", function(){
     var url = "/cliente/eliminacion";
     var x=$(this).attr("id");
     $.ajax({
       type:"POST",
       url: url,
       data: {"id":x},
       success: function (response){
         alert(response);
         actualizarTabla();
       }
     });
   });
   $("#tablaprueba").on("click","button.act", function(){
     var x=$(this).attr("id");
     var url = "/cliente/fupdate/"+x;
     location.href=url;
   });
});
