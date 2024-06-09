document.querySelector("#send").onclick = async ()=>{
  document.querySelector("#spinner").classList.toggle("hidden");
  const product = document.querySelector("#product").value
  const info = document.querySelector("#info").value
  const style = document.querySelector("#style").value
  const items = document.querySelector("#items").value
  const req = await fetch("/api/marketing", {
    body: JSON.stringify({
      product,
      info,
      style,
      items
    }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res = await req.json();
  document.querySelector("#pre").innerText = res.answer
  document.querySelector("#download").innerText = `Download [${product}.txt]`
  document.querySelector("#download").download = `${product}.txt`
  document.querySelector("#download").href = `data:text/plain;base64,${btoa(res.answer)}`
  document.querySelector("#spinner").classList.toggle("hidden");
}
