function succsess(xhr){
	var newdiv = document.createElement('div');
	newdiv.innerHTML = xhr.response
	document.getElementById('target').appendChild(newdiv); 
	console.log(xhr.response);
}

function error(xhr){
	console.log("Error")
}