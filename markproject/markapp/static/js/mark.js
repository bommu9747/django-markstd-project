function validation(){
    var stdname=document.getElementById('exampleInputname').value;
    var stdmark=document.getElementById('exampleInputmark').value;
    var stdgrade=document.getElementById('exampleInputgrade').value;
    var format = /^[a-zA-Z\-]+$/
    

    if(stdname==""){
        document.getElementById('sname').innerHTML="enter student name"
        return false;
    }else{document.getElementById('sname').innerHTML=""}
    if(!isNaN(stdname)){
        document.getElementById('sname').innerHTML="only character are allowed"
        return false;
    }
    if(!format.test(stdname)){
        document.getElementById('sname').innerHTML="not use special characters"
        return false;
    }
    if(stdmark==""){
        document.getElementById('smark').innerHTML="enter student totalmarks"
        return false;
    }else{document.getElementById('smark').innerHTML=""}
    if(isNaN(stdmark)){
        document.getElementById('smark').innerHTML="only digitl numbers are allowed"
        return false;
    }

if(stdgrade==""){
    document.getElementById('sgarde').innerHTML="enter student grade total"
    return false;

}else{document.getElementById('sgarde').innerHTML=""}
if(!isNaN(stdgrade)){
    document.getElementById('sgarde').innerHTML="only character are allowed"
    return false;
}
}