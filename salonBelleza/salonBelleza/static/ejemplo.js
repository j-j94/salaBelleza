$(document).ready(function(){
   $(".eliminar").click(function(){
    var url2 = "eliminacion";
    var valores ={"prueba":1};
    $.ajax({
      type: "POST",
      url: url2,
      data: valores,
      beforeSend: function(){
        $("#resultado").html("procesando...");
      },
      success: function (response){
        $("#resultado").html(response);
      }
    });
   });
});
