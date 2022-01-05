window.onload = function() {
    let cookie = getCookie("theme");
    if (cookie == 'dark' || cookie == '' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        changeTheme("dark", false);
    }
    else {
        changeTheme("light", false);
    }

    if (document.getElementsByClassName('footer_date')[0] != undefined) {
        let date = new Date().getFullYear()
        document.getElementsByClassName('footer_date')[0].innerHTML = date + ' ';
    }
    setTimeout(() => {//  Additional delay for changeTheme function
        document.body.style.visibility = 'visible';
        document.body.style.setProperty("--animation-delay-flash", "150ms");
    }, 80);
}

function getTheme(theme) {
    if (document.getElementById("light-theme-sun").style.display == 'none') {
        return 'light';
    }
    else if (document.getElementById("dark-theme-moon").style.display == 'none') {
        return 'dark';
    }
    else {
        console.log('Error: Both icons are hidden. Fallbacking to light theme.');
        return 'light';
    }
}

function changeTheme(theme, setCookie = true) {
    if (theme == 'dark') {
        document.body.style.setProperty("--background-color", "#34353B");
        document.body.style.setProperty("--text-color", "#F0F0F0");
        document.body.style.setProperty("--social-onhover-color", "#BFBFBF");
        document.body.style.setProperty("--project-card-color", "#52535e");
        document.body.style.setProperty("--note-warning", "#8cdeff");
        document.body.style.setProperty("--theme-change-button", "#D3D3D3");
        document.body.style.setProperty("--navbar-onhover-color", "#6e6f7d");
        document.body.style.setProperty("--theme-icon-onhover", "#bfbfbf");
        document.body.style.setProperty("--link-color", "#b2c9ff");
        document.body.style.setProperty("--warning-color", "#FFD700");
        document.body.style.setProperty("--link-hover-color", "#c1c5ff");

        document.getElementById("light-theme-sun").style.display = 'none';
        document.getElementById("dark-theme-moon").style.display = 'block';
        
        if (setCookie) {
            let date = new Date();
            date.setFullYear(date.getFullYear() + 10);
            document.cookie = "theme=dark; expires=" + date.toUTCString(); + "; path=/; Secure";
        }
    }
    else if (theme == 'light') {
        document.body.style.setProperty("--background-color", "white");
        document.body.style.setProperty("--text-color", "black");
        document.body.style.setProperty("--social-onhover-color", "#333");
        document.body.style.setProperty("--project-card-color", "#D3D3D3");
        document.body.style.setProperty("--note-warning", "#b70000");
        document.body.style.setProperty("--theme-change-button", "#34353B");
        document.body.style.setProperty("--navbar-onhover-color", "#bfbfbf");
        document.body.style.setProperty("--theme-icon-onhover", "#42434A");
        document.body.style.setProperty("--link-color", "#013ff1");
        document.body.style.setProperty("--warning-color", "#b70000");
        document.body.style.setProperty("--link-hover-color", "#3552a7");

        document.getElementById("light-theme-sun").style.display = 'block';
        document.getElementById("dark-theme-moon").style.display = 'none';

        if (setCookie) {
            let date = new Date();
            date.setFullYear(date.getFullYear() + 10);
            document.cookie = "theme=light; expires=" + date.toUTCString(); + "; path=/; Secure";
        }
    }

    else {
        console.log('Error: Valid theme not provided for changeTheme function.');
    }
}

function getCookie(cname) {// stolen from w3schools B)
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}