function openNav() {
     document.getElementById("sidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("sidebar").style.width = "0px";
}

//This function will add items when the addition button is clicked
$(document).ready(function() {
     var counter = 0

     //Add item
     $("#add").click(function() {
          var name = $("#in_name").val();
          var revenue = $("#in_revenue").val();

          $("#added_employees").append(
               "<div id=employee" + counter + ">" +
               "<input type='text' class='added_employee' id='employee" + counter + '\' value="' + name + '" readonly>' +
               "<input type='text' class='added_employee' id='employee" + counter + '\' value="' + revenue + '" readonly>' +
               "<input type='button' class='added_employee' value='X' id='employee" + counter + "\'></div>"
          );
          name = 0;
          revenue = 0;
          counter++;
     });

     $("#added_employees").on('click', ".added_employee", function() {
          var employee_id = $(this).attr('id');

          $("#" + employee_id).remove();
     });
});
