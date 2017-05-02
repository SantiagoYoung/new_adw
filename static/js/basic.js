
var change1=document.getElementById("headerrighttext1");
var change2=document.getElementById("headerrighttext2");
change1.style.background="red";
change1.style.color="white";
var btn_click=1;
var mouse_over_btn1=function(){
    change1.style.background="white";
    change1.style.color="red";
}
var mouse_out_btn1=function(){
    if(btn_click=1){
        change1.style.background="red";
        change1.style.color="white";
    }
    else{
        change1.style.background="white";
        change1.style.color="black";
    }
}
var click_btn1=function(){
    btn_click==1;
    change1.style.background="red";
    change1.style.color="white";
    change2.style.background="white";
    change2.style.color="black";
}
var mouse_over_btn2=function(){
    change2.style.background="white";
    change2.style.color="red";
}
var mouse_out_btn2=function(){
    if(btn_click==2){
        change2.style.background="red";
        change2.style.color="white";
    }
    else{
        change2.style.background="white";
        change2.style.color="black";
    }
}
var click_btn2=function(){
    btn_click=2;
    change2.style.background="red";
    change2.style.color="white";
    change1.style.background="white";
    change1.style.color="black";
}
change1.onclick=click_btn1;
change1.onmouseover=mouse_over_btn1;
change1.onmouseout= mouse_out_btn1;
change2.onclick=click_btn2;
change2.onmouseover=mouse_over_btn2;
change2.onmouseout= mouse_out_btn2;
var change1=document.getElementById("headerrighttext1");
var change2=document.getElementById("headerrighttext2");
change1.style.background="red";
change1.style.color="white";
var btn_click=1;
var mouse_over_btn1=function(){
    change1.style.background="white";
    change1.style.color="red";
}
var mouse_out_btn1=function(){
    if(btn_click=1){
        change1.style.background="red";
        change1.style.color="white";
    }
    else{
        change1.style.background="white";
        change1.style.color="black";
    }
}
var click_btn1=function(){
    btn_click==1;
    change1.style.background="red";
    change1.style.color="white";
    change2.style.background="white";
    change2.style.color="black";
}
var mouse_over_btn2=function(){
    change2.style.background="white";
    change2.style.color="red";
}
var mouse_out_btn2=function(){
    if(btn_click==2){
        change2.style.background="red";
        change2.style.color="white";
    }
    else{
        change2.style.background="white";
        change2.style.color="black";
    }
}
var click_btn2=function(){
    btn_click=2;
    change2.style.background="red";
    change2.style.color="white";
    change1.style.background="white";
    change1.style.color="black";
}
change1.onclick=click_btn1;
change1.onmouseover=mouse_over_btn1;
change1.onmouseout= mouse_out_btn1;
change2.onclick=click_btn2;
change2.onmouseover=mouse_over_btn2;
change2.onmouseout= mouse_out_btn2;

