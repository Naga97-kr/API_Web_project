/*var country;

function input(){
    var input = document.getElementById("city").value;
    if (input != null){
        country = input.toLowerCase();
        localStorage.setItem("city",JSON.stringify(country));
        location.href= "http://mysite.com:8000/weather";
    }
    else {
        location.href= "http://mysite.com:8000/index";
    }
}*/

var country;  
var gender;
function input(){     
    var input = document.getElementById("city").value; 
    var input_gender = document.getElementById("gender").value;
    gender = input_gender
    localStorage.setItem("gender",JSON.stringify(gender));    
    if (input != null ){         
        country = input.toLowerCase();  
        localStorage.setItem("city",JSON.stringify(country));  
        location.href= "http://mysite.com:8000/weather";   
    } 
    }

