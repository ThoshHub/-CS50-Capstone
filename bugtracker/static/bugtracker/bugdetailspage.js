document.addEventListener('DOMContentLoaded', function() {
    var bug_id = document.querySelector('#bugdetailspage_id').innerHTML // returns 1 upon load
    initialize(bug_id);

	document.addEventListener('click', event => { //unused as of 20.10.29
		const element = event.target;
		console.log("Something was clicked");
	})
});

async function initialize(bug_id) {
	console.log("You have reached bugdetails page...")
    console.log(bug_id.toString())

    fetch('/bugtracker/bugdetailcontent/' + bug_id)
    .then(res => res.json())
    .then(data => {
        // log the data
        console.log(data)
        
        // display the data onscreen
        display_bug(data)
    })
}

function display_bug(data){
    console.log("Attempting to display the bug... ")
    console.log("This feature has not been implemented yet... ")
}