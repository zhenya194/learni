const ask = document.getElementById("ask");
const process_olympiad_tasks = document.getElementById("process_olympiad");
function yes() {
    ask.style.display = "none";
    process_olympiad_tasks.style.display = "block";
}

function to_complete() {
    document.getElementById("old_complete_btn").style.display = "none";
    document.getElementById("complete_alert").style.display = "block";
    document.getElementById("new_complete_btn").style.display = "block";
}

function finish() {
    document.getElementById("process_olympiad").style.display = "none";
    document.getElementById("olympiad_result").style.display = "block";
}
