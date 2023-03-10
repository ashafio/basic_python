// get html element to display time in
let display = document.getElementById("root");
function clock(){
// get current time
let currentTime=new Date().toLocaleTimeString();
// appent current time to DOM
display.innerHTML="It is"+currentTime;
}

// calculate time then updatte display every secound
setInterval(clock,1000);//(100ms=1s)