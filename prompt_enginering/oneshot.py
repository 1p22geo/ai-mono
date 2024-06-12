import lib


system =  """
You are a helpful AI assistant.
Provide short and informational responses.
"""

prompt = """
Q: What is the color of grass?
A: The color of grass is green.
Q: What is the color of the sky?
A: 
"""

print(lib.ai(system, prompt))
