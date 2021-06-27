window.onload = init;
var saveAnswer;

function init() {
    console.log("Hi")
    saveAnswer = document.getElementById('save')
    saveAnswer.onclick = save
}

function save(){
    alert("Вы уверены?")
    var answer = $("input:radio[name=answer]:checked").val()

    var req = new XMLHttpRequest();
    var url = "/quest/save?answer=" + answer

    req.open("GET", url, true)
    req.send()
}