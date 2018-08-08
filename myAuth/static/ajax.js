function request(method, url, headers, succsess_func, error_func, data=""){
	let xhr = new XMLHttpRequest();
 	xhr.open(method, url);
 	for (key in headers){
 		xhr.setRequestHeader(key, headers[key]);
 	}
	xhr.onreadystatechange = function() {
	    if(xhr.readyState == 4 & xhr.status == 200) {
	        succsess_func(xhr);
	    }
	    else if (xhr.readyState == 4){
	    	error_func(xhr);
	    }
	}
	xhr.send(data);
}

