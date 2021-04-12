function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0)
      return c.substring(nameEQ.length, c.length);
  }
  return undefined;
}

window.onload = function() {
  if (document.getElementsByClassName('footer_date')[0] != undefined) {
    var date = new Date().getFullYear()
    document.getElementsByClassName('footer_date')[0].innerHTML = date + ' ';
    document.getElementsByClassName('footer_date')[1].innerHTML = date + ' ';
  }
  const cookie = getCookie('cookie');
  if (cookie == "1" && document.getElementsByClassName('cookie')[0] != undefined) {
    document.getElementsByClassName('bottom')[0].style.paddingBottom = '5px';
    document.getElementsByClassName('bottom2')[0].style.paddingBottom = '5px';
    document.getElementsByClassName('cookie')[0].style.display = 'none';
    document.getElementsByClassName('cookie2')[0].style.display = 'none';
  }
  if (document.getElementById("code") != undefined) {
    const code = getCookie('code');
    if (code != undefined) {
      document.getElementById("code").value = code;
    }
    const codeForm = document.getElementById("code");
    codeForm.addEventListener("keyup", function(event) {
      if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("code-button").click();
      }
    });
  }
  const urlParams = new URLSearchParams(window.location.search);
  const URLlogoutParam = urlParams.get("logout");
  if (URLlogoutParam != undefined) {
    document.getElementById("logout-message").style.display = 'block';
  }
  document.body.style.visibility = 'visible';
}

function acceptCookies() {
  document.getElementsByClassName('bottom')[0].style.paddingBottom = '5px';
  document.getElementsByClassName('bottom2')[0].style.paddingBottom = '5px';
  document.getElementsByClassName('cookie')[0].style.display = 'none';
  document.getElementsByClassName('cookie2')[0].style.display = 'none';
  var date = new Date();
  date.setFullYear(date.getFullYear() + 10);
  var expires = "; expires=" + date.toUTCString();
  document.cookie = "cookie=1" + expires + "; path=/";
}
