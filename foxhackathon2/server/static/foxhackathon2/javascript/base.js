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
               //hide the div after creation
               "<div id='employee" + counter + "\' style='display:none;'>" +
               "<input type='text' class='added_employee' id='employee" + counter + '\' value="' + name + '" readonly>' +
               "<input type='text' class='added_employee' id='employee" + counter + '\' value="' + revenue + '" readonly>' +
               "<input type='button' class='removeItem' value='X' id='employee" + counter + "\'></div>"
          );

          //show the div with transition
          $("#employee" + counter).show('fast');

          name = 0;
          revenue = 0;
          counter++;
     });

     $("#added_employees").on('click', ".removeItem", function() {
          var employee_id = $(this).attr('id');

          //hide div
          $("#" + employee_id).hide(100, function() {
               //remove div
               $("#" + employee_id).remove();
          })
     });
});
