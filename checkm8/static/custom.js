document.querySelector("#send").onclick = async () => {
  document.querySelector("#spinner").classList.toggle("hidden");
  const script = document.querySelector("#script").value;
  const req = await fetch("/api/script", {
    body: JSON.stringify({
      script,
    }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res = await req.json();
  document.querySelector("#pre").innerText = res.answer;
  document.querySelector("#download").innerText = `Download [answer.txt]`;
  document.querySelector("#download").download = `answer.txt`;
  document.querySelector("#download").href =
    `data:text/plain;base64,${btoa(res.answer)}`;
  document.querySelector("#spinner").classList.toggle("hidden");
};
