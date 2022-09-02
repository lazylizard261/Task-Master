
document.getElementById("content").addEventListener('keyup', () => {
    var x = document.getElementById("content").value;
    var submit_btn = document.getElementById("submit");
    if (x == "") {
        submit_btn.disabled = true;
        submit_btn.className = "btn btn-secondary"
    }
    else {
        submit_btn.disabled = false;
        submit_btn.className = "btn btn-success"
    }
});
