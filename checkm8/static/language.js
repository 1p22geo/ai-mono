document.querySelector("#send").onclick = async () => {
  document.querySelector("#spinner").classList.toggle("hidden");
  const a = document.querySelector("#a").value;
  const b = document.querySelector("#b").value;
  const req = await fetch("/api/corelate", {
    body: JSON.stringify({
      a,
      b,
    }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res = await req.json();
  document.querySelector("#answer").innerText = `Corelation: ${res.corelation}`;

  document.querySelector("#spinner").classList.toggle("hidden");
};
