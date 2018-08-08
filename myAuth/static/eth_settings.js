function succsess(xhr){
	var msgText = document.getElementsByClassName("msgText")[0];
	msgText.innerText = "Succsess";
}

function error(xhr){
	var msgText = document.getElementsByClassName("msgText")[0];
	msgText.innerText = "Error";
}