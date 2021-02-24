document.addEventListener('DOMContentLoaded', function() {
    initialize();

	document.addEventListener('click', event => { //unused as of 20.10.29
		const element = event.target;
		console.log("Something was clicked");
	})
});

function initialize(){
	console.log("You are now on the createbug page, This is being printed from the intialize function...")
	document.getElementById("id_type").classList.add('form-control'); // Add bootstrap class to type
	document.getElementById("id_severity").classList.add('form-control'); // Add bootstrap class to severity
}