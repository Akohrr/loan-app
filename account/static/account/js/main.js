
$("#new-loan-btn").click(function () {
    $("#new-loan-modal").show();
});

$('#close-new-loan-modal').click(function () {
    $("#new-loan-modal").hide();
});

$("#new-loan-btn").click( function () {
    var element = $(this);
    $.ajax({
      url: '/loan/new-loan/',
      type: 'get',
      dataType: 'json',
    
      success: function (info) {
        $("#new-loan-modal").show();
        $(".form-data").html(info.html);
      }

    });
  });



  $("#new-loan-form").on("submit", function (e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({

      url: '/loan/new-loan/',
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (info) {
        if (info.saved_successfully) {
          $("#new-loan-modal").css('display', 'none');
          location.reload();
        }
        else {
          $('.form-data').html(info.html);
        }
      }
    });
  });