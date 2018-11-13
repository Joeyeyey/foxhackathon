function openNav() {
     document.getElementById("sidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("sidebar").style.width = "0px";
}

//This function will add items when the addition button is clicked
$(document).ready(function() {
     var counter = 0;

     //Add item
     $("#add").click(function() {
          // TODO: sanitize user input before inserting it into the
          var name = $("#in_name").val();
          var revenue = $("#in_revenue").val();

          // TODO: add a dropdown list of job types based on user input
          $("#added_employees").append(
               //hide the div after creation
               "<div id='employee" + counter + "\' style='display:none;'>" +
               "<input type='text' class='added_employee' id='employee" + counter + '\' value="' + name + '" readonly>' +
               "<input type='text' class='added_employee_revenue' id='employee" + counter + '\' value="' + revenue + '" readonly>' +
               "<button class='removeItem' onclick='return false;' id='employee" + counter + "\'>X</button></div>"
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
          $("#" + employee_id).hide('fast', function() {
               //remove div
               $("#" + employee_id).remove();
          })
     });
});
