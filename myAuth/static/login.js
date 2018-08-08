function succsess(xhr){
	var token = xhr.response.split(":")[1].slice(1,-2);
	localStorage.setItem("token", token);
	console.log(token)
	var msgText = document.getElementsByClassName("msgText")[0];
	msgText.innerText = "Succsess";

}

function error(xhr){
	var msgText = document.getElementsByClassName("msgText")[0];
	msgText.innerText = "Error";
}