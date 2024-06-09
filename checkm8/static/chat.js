let user = "Guest";

let history = [];

let model_type = "casual";

function clear_history() {
  Array.from(document.querySelectorAll(".chat")).forEach((e) => {
    e.remove();
  });
  history = [];
}
document.querySelector("#reset").onclick = clear_history;

Array.from(document.querySelectorAll("[name=model]")).forEach((e) => {
  e.onclick = () => {
    model_type = e.value;
    clear_history();
  };
});
document.querySelector("[name=username]").onchange = () => {
  user = document.querySelector("[name=username]").value;
  clear_history();
};

document.querySelector("#send").onclick = async () => {
  const prompt = document.querySelector("#q").value;
  history.push({
    actor: "user",
    content: prompt,
  });
  document.querySelector("#q").value = "";

  document.querySelector("#spinner").classList.toggle("hidden");

  const q_div = document.createElement("div");
  q_div.className =
    "m-4 mr-24 flex flex-col gap-2 items-start bg-blue-400 p-4 rounded-md chat";
  const user_div = document.createElement("div");
  user_div.innerText = `${user}:`;
  const prompt_div = document.createElement("div");
  prompt_div.innerText = prompt;
  q_div.appendChild(user_div);
  q_div.appendChild(prompt_div);
  document.querySelector("#main").appendChild(q_div);
  const req = await fetch("/api/chat", {
    body: JSON.stringify({
      history,
      user: {
        uname: user,
      },
      settings: {
        behavior: model_type,
      },
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
    "m-4 ml-24 flex flex-col gap-2 bg-blue-300 p-4 rounded-md chat";
  const a_div = document.createElement("div");
  a_div.innerText = "Checkm8:";
  const answer_div = document.createElement("div");
  answer_div.innerText = res.answer;
  history.push({
    actor: "Checkm8",
    content: res.answer,
  });
  r_div.appendChild(a_div);
  r_div.appendChild(answer_div);

  document.querySelector("#main").appendChild(r_div);

  document.querySelector("#spinner").classList.toggle("hidden");
};
