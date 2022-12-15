function validation(){
    var std=document.getElementById('exampleInputstudent').value;
    var adds=document.getElementById('exampleInputaddress').value;
    var phone=document.getElementById('exampleInputphone').value;
    // var format = "[@_!#$%^&*()<>?/|}{~:]";
    var format =/^[a-zA-Z\-]+$/
    if(std==""){
    document.getElementById('ustd').innerHTML="enter student name"
    return false;
}else{ document.getElementById('ustd').innerHTML=""}
if(!format.test(std)){
    document.getElementById('ustd').innerHTML="not use special characters"
    return false;
}
if(adds==""){
    document.getElementById('uaddress').innerHTML="enter student address"
    return false;``
}else{document.getElementById('uaddress').innerHTML=""}
if(phone==""){
    document.getElementById('uphone').innerHTML="enter your phone number"
    return false;
}
// if(!format.test(phone)){
//     document.getElementById('uphone').innerHTML="not use special characters"
//     return false;

if(isNaN(phone)){
    document.getElementById('uphone'.innerHTML="use 10 digital numbers")
    return false;
}
    if(phone.length!=10){
        document.getElementById('uphone').innerHTML="enter must 10 digital"
        return false;
}else{document.getElementById('uphone').innerHTML=""}
}