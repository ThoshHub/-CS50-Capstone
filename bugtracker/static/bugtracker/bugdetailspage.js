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

    fetch('/bugtracker/bugdetailcontent/' + bug_id)
    .then(res => res.json())
    .then(data => {
        // log the data
        // console.log(data);
        
        // display the data onscreen
        display_bug(data, bug_id);
    })
}

function display_bug(data, bug_id){
    console.log("Attempting to display the bug 3... ");
    const bug_title = data.title.toString();
    const bug_description = data.description.toString();
    const bug_severity = data.severity.toString();
    const bug_estimate = data.estimate.toString();
    const bug_sme = data.sme.toString();
    const bug_org = data.org.toString();

    var bugpost = document.createElement('div');
    bugpost.id = "bug_" + bug_id;
    bugpost.innerHTML = generateBugDiv(bug_id, bug_title, bug_description, bug_severity, bug_estimate, bug_sme, bug_org); // Generates the inner HTML
	bugpost.innerHTML += generateEditButton(bug_id);

    document.querySelector('#bugdetailspage_info').append(bugpost)

    // Assign CSS
    document.getElementById(bugpost.id).className = "bugbox"
}

function generateBugDiv(bug_id, bug_title, bug_description, bug_severity, bug_estimate, bug_sme, bug_org){
    // generate html for  
    let severity_style = "btn btn-success" // default is green
    if (bug_severity.toUpperCase() == "MEDIUM") {
        severity_style = "btn btn-warning"
    } else  if (bug_severity.toUpperCase() == "HIGH" || bug_severity.toUpperCase() == "CRITICAL"){
        severity_style = "btn btn-danger"
    }

    let estimate_style =  "btn btn-success" // default is green
    if (parseInt(bug_estimate) > 5) {       // over 5 hours is yellow
        estimate_style = "btn btn-warning"
    } else if (parseInt(bug_estimate) > 10) { // over 10 hours is red
        estimate_style = "btn btn-danger"
    }

    let div = "<h1>" + bug_title +  "</h1><br>";
    div += "<h5>" + "<strong style=\"color: grey;\">Description: </strong>" + bug_description + "</h5>";
    div += "<h5>" + "<strong style=\"color: grey;\">Priority: </strong>" + "<span class=\"" + severity_style + "\">" + capitalizeFirstLetter(bug_severity.toLowerCase()) + "</span></h5>";
    div += "<h5>" + "<strong style=\"color: grey;\">Estimate: </strong>" +  "<span class=\"" + estimate_style + "\">" + bug_estimate + "  Hour(s)" + "</span></h5>";
    div += "<h5>" + "<strong style=\"color: grey;\">Assigned To: </strong>" + bug_sme + "</h5>";
    div += "<h5>" + "<strong style=\"color: grey;\">Company: </strong>" + bug_org + "</h5>";

    return div; // dummy
}

function generateEditButton(bug_id){
	button = "<a class=\"btn btn-primary\" style=\"color:white\""
	button += "href=\"/bugtracker/bugdetailspage/" + bug_id +"/edit\" >" 
	button += "Edit" 
	button += "</a>"

    return button; // dummy
}

function capitalizeFirstLetter(string) {
	return string.charAt(0).toUpperCase() + string.slice(1);
}