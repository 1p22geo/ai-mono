from agent import executor

print("Ready!")
while True:
    prompt = input('>')
    res = executor.stream(
        {"input": prompt, "chat_history": []})

    for p in res:
        print(p, end=" ")
