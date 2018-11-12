function openNav() {
     document.getElementById("sidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("sidebar").style.width = "0px";
}

function addItem() {
     //This function will add 2 rows of user_input into the page
     var text_box1 = document.createElement("INPUT");
     var text_box2 = document.createElement("INPUT");

     var name = document.getElementById("in_name");
     var revenue = document.getElementById("in_revenue");

     //Target Tag: <input type="text" id="output" value=user_input readonly>
     text_box1.setAttribute("id", "out_name");
     text_box2.setAttribute("id", "out_revenue");
     text_box1.setAttribute("class", "textfield");
     text_box2.setAttribute("class", "textfield");

     text_box1.setAttribute("type", "text");
     text_box2.setAttribute("type", "text");
     text_box1.setAttribute("value", name.value);
     text_box2.setAttribute("value", revenue.value);

     document.body.appendChild(text_box1);
     document.body.appendChild(text_box2);

     document.getElementById("out_name").readOnly = true;
     document.getElementById("out_revenue").readOnly = true;
     //name.setAttribute("readonly");
}

function removeItem() {
     //This function will remvove 2 rows of user_input from the page
     var name = document.getElementById("name");
     var revenue = document.getElementById("revenue");

     name.parentNode.removeChild(name);
     revenue.parentNode.removeChild(revenue);
}
