document.addEventListener('DOMContentLoaded', function() {
    var bug_id = document.querySelector('#bugdetailspage_id').innerHTML // returns 1 upon load
    initialize(bug_id);

	document.addEventListener('click', event => { //unused as of 20.10.29
		const element = event.target;
		console.log("Something was clicked");
	})
});

async function initialize(bug_id) {
	//console.log("You have reached bugdetails page...");
    //console.log(bug_id.toString());

    fetch('/bugtracker/bugdetailcontent/' + bug_id);
    .then(res => res.json());
    .then(data => {
        // log the data
        // console.log(data);
        
        // display the data onscreen
        display_bug(data, bug_id);
    })
}

function display_bug(data, bug_id){
    console.log("Attempting to display the bug... ");
    const bug_title = data.title;
    const bug_description = data.description;
    const bug_severity = data.severity;
    const bug_estimate = data.estimate;
    const bug_sme = data.sme;
    const bug_org = data.org;

    var bugpost = document.createElement('div');
    bugpost.id = "bug_" + bug_id;
    bugpost.innerHTML = generateBugDiv(bug_id, bug_title, bug_description, bug_severity, bug_estimate, bug_sme, bug_org); // Generates the inner HTML
    bugpost.innerHTML += generateEditButton(bug_id);
}

function generateBugDiv(bug_id, bug_title, bug_description, bug_severity, bug_estimate, bug_sme, bug_org){
    return "0   "; // dummy
}

function generateEditButton(bug_id){
    return "0"; // dummy
}