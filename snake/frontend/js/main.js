
function register(username){

	const Http = new XMLHttpRequest();

	var ip = location.host.split(':')[0]; 

	const url='http://' + ip + ':5000/add_user?username=' + username.toString(); 
	Http.onreadystatechange = (e) => {

		// Request has finished
		if (Http.readyState === 4) {

			// If user already exists
			if(Http.response == "Invalid User"){
				const errors_log = document.getElementById('errors'); 
				errors_log.innerHTML = Http.response + " " + username.toString(); 
			}
			// Username has been added - go to next page
			else{
				localStorage.setItem('username', username);
				window.location.href = '/snake.html';
			} 
		}
	}      
	Http.open("GET", url);
	Http.send();  
}

function getLeaderboard() {
    const Http = new XMLHttpRequest();
	var ip = location.host.split(':')[0]; 

    const url='http://'+ ip + ':5000/get_leaderboard';
    Http.onreadystatechange = (e) => {
        if (Http.readyState === XMLHttpRequest.DONE) {
            table = document.createElement('table');
			table.innerHTML = "<tr><th>Username</th><th>Score</th></tr>"


            document.getElementById('myItemList').appendChild(table);
            var obj = JSON.parse(Http.responseText);
			console.log(obj);
            (obj).forEach(function (item) {
				// Create row for the data with the elements inside
                let tr = document.createElement('tr');
				let td1 = document.createElement('td');
				let td2 = document.createElement('td');
				td1.innerHTML = item['name']; 
				td2.innerHTML = item['score']; 

				// Add the 'td' to the 
				tr.appendChild(td1); 
				tr.appendChild(td2); 
				table.appendChild(tr);
            });
        }
    }
    
    Http.open("GET", url);
    Http.send();
}