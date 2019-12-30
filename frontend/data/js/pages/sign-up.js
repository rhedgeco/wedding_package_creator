let first = document.getElementById('first-name');
let last = document.getElementById('last-name');
let email = document.getElementById('email');
let username = document.getElementById('username');
let password = document.getElementById('password');
let passLock = document.getElementById('passLock');
let confirm = document.getElementById('confirm-password');
let confLock = document.getElementById('confLock');
let confirmTip = document.getElementById('confirm-tip');

function check_passwords_match() {
    if (confirm.value !== password.value) {
        confirmTip.setAttribute('data-error', 'passwords must match.');
        confirm.classList.remove('valid');
        confirm.classList.add('invalid');
        confLock.innerHTML = "lock_open";
        return false;
    } else {
        confirmTip.setAttribute('data-error', '');
        confLock.innerHTML = "lock";
        return true;
    }
}

function create_account() {
    if(!check_passwords_match()) return;
    let request = new XMLHttpRequest();
    let form = new FormData();
    request.open('POST', '/api/users');
    request.onload = function () {
        if (this.status === 200) {
            window.location.href = "/";
        } else {
            M.toast({html: 'Failed to create User.<br>Status: ' + this.status + '<br>' + this.responseText})
        }
    };
    form.append('first_name', first.value);
    form.append('last_name', last.value);
    form.append('email', email.value);
    form.append('username', username.value);
    form.append('password', password.value);
    request.send(form);
}

password.onblur = function () {
    if(password.value.length > 0)
    {
        passLock.innerHTML = "lock";
    } else {
        passLock.innerHTML = "lock_open";
    }
};

confirm.onblur = function () {
    check_passwords_match();
};