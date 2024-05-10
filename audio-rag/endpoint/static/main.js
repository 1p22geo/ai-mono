document.querySelector("#send").onclick = async () => {
  const prompt = document.querySelector("#q").value;
  document.querySelector("#q").value = "";

  document.querySelector("#spinner").classList.toggle("hidden");

  const q_div = document.createElement("div");
  q_div.className =
    "m-4 mr-24 flex flex-col gap-2 items-start bg-emerald-400 p-4 rounded-md";
  const user_div = document.createElement("div");
  user_div.innerText = "User:";
  const prompt_div = document.createElement("div");
  prompt_div.innerText = prompt;
  q_div.appendChild(user_div);
  q_div.appendChild(prompt_div);
  document.querySelector("#main").appendChild(q_div);

  const req = await fetch("/api/query", {
    body: JSON.stringify({
      prompt,
    }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res = await req.json();
  console.log(res);
  const r_div = document.createElement("div");
  r_div.className =
    "m-4 ml-24 flex flex-col gap-2 bg-emerald-300 p-4 rounded-md";
  const a_div = document.createElement("div");
  a_div.innerText = "RAG:";
  const answer_div = document.createElement("div");
  answer_div.innerText = res.answer;
  const context_div = document.createElement("div");
  res.context.forEach((elem) => {
    const context_item = document.createElement("div");
    context_item.className = "m-4 border-b-2";
    const text = document.createElement("div");
    text.innerText = elem.page_content;
    context_item.appendChild(text);
    const source = document.createElement("div");
    source.innerText = elem.metadata.source;
    source.className = "text-right font-semibold";
    context_item.appendChild(source);
    context_div.appendChild(context_item);
  });
  r_div.appendChild(a_div);
  r_div.appendChild(answer_div);
  r_div.appendChild(context_div);

  document.querySelector("#main").appendChild(r_div);

  document.querySelector("#spinner").classList.toggle("hidden");
};
const getFileType = (filename) => {
  switch (filename.split(".").at(-1)) {
    case "txt":
      return "Text file";
    case "wav":
      return "WAV Sound recording";
    case "pdf":
      return "PDF document";
    default:
      return "<<unknown>>";
  }
};

fetch("/files").then((res) =>
  res.json().then((json) => {
    document.querySelector("#files").innerHTML =
      `<h1 class="text-xl">Files in RAG store</h1>` +
      json
        .map(
          (file) => `
  <div class="p-4 bg-white rounded-md flex flex-row items-center justify-between"><div>${file}</div><div class="italic">${getFileType(file)}</div></div>
`,
        )
        .join("");
  }),
);
