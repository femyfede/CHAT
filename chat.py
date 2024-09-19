import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

  system_instruction="you are a datascientist, you task is to enage in conservatiopn and answer quetion about data science and the related quetion",
)


history=[]

print("Bot: hellow,how can i help you?")

while True:
 
 user_input=input("you:")

 chat_session = model.start_chat(
  history=history

)

 response = chat_session.send_message("user_input")
 model_response = response.text
 print('fBot:{model_response}')
 print()


 history.append({"role":"user","parts":[user_input]})
 history.append({"role":"model","parts":[model_response]})