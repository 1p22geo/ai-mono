from agent import executor

print("Ready!")
while True:
    prompt = input('>')
    res = executor.invoke(
        {"input": prompt, "chat_history": []})

    print(res['output'])
