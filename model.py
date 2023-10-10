import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("satvikag/chatbot")
model = AutoModelForCausalLM.from_pretrained("satvikag/chatbot")

text="What are you doing these days?"

for step in range(1):
    new_user_input_ids = tokenizer.encode(text+ tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    chat_history_ids = model.generate(
        bot_input_ids, max_length=500,
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=100, 
        top_p=0.7,
        temperature = 0.8
    )
    ans=tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(ans)
    # print("AI: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

# new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')
# bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

# chat_history_ids = model.generate(
#     bot_input_ids, max_length=500,
#     pad_token_id=tokenizer.eos_token_id,  
#     no_repeat_ngram_size=3,       
#     do_sample=True, 
#     top_k=100, 
#     top_p=0.7,
#     temperature = 0.8
# )
# ans=tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
# print(ans)
# print("AI: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))