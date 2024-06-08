function syntaxHighlight(json) {
    if (typeof json != 'string') {
         json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}


document.querySelector("#send").onclick = async ()=>{
  document.querySelector("#spinner").classList.toggle("hidden");
  const a = document.querySelector("#a").value
  const req = await fetch("/api/sentiment", {
    body: JSON.stringify({
      content:a,
    }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
   const res = await req.json();
  document.querySelector("pre").innerHTML = syntaxHighlight(res)

  document.querySelector("#spinner").classList.toggle("hidden");
}
