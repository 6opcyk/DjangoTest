function succsess(xhr){
	data = JSON.parse(xhr.response);
	document.getElementById("rate").innerText = data["eth_rate"]
	document.getElementById("number").innerText = data["number"]
	document.getElementById("date").innerText = data["date"]
	document.getElementById("hash").innerText = data["block_hash"]
	document.getElementById("difficulty").innerText = data["difficulty"]
	document.getElementById("gasUsed").innerText = data["gasUsed"]
	document.getElementById("link").setAttribute("href", data["link"])
	document.getElementById("balance").innerText = data["balance"]
}

function error(xhr){
	console.log("Error")
}