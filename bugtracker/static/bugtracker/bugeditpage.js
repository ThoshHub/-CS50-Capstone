document.addEventListener('DOMContentLoaded', function() {
    var bug_id = document.querySelector('#bugeditpage_id').innerHTML // returns 1 upon load
    initialize(bug_id);

	document.addEventListener('click', event => { //unused as of 20.10.29
		const element = event.target;
		console.log("Something was clicked");
	})
});

function initialize(bug_id){
    console.log("You are now on the bug edits page")
}