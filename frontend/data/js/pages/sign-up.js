function create_account() {
    var first = document.getElementById('first-name').value;
    var last = document.getElementById('last-name').value;
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var request = new XMLHttpRequest();
    var form = new FormData();
    request.open('POST','/api/users');
    request.onload = function () {
        if(this.status === 200){
            window.location.href = "/";
        } else {
            M.toast({html: 'Failed to create User.<br>Status: ' + this.status + '<br>' + this.responseText})
        }
    };
    form.append('first_name', first);
    form.append('last_name', last);
    form.append('email', email);
    form.append('username', username);
    form.append('password', password);
    request.send(form);
}