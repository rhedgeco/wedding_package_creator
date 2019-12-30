let username = document.getElementById('username');
let password = document.getElementById('password');

function login_user() {
    let request = new XMLHttpRequest();
    let params = '?username='+username.value+'&password='+password.value;
    request.open('GET', '/api/auth'+params);
    request.onload = function () {
        if (this.status === 200) {
            document.cookie = 'authToken='+this.responseText;
            window.location.href = "wpc.html";
        } else {
            M.toast({html: 'Failed to log in.<br>Status: ' + this.status + '<br>' + this.responseText});
        }
    };
    request.send();
}