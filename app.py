from flask import Flask, jsonify, session, request, redirect, url_for, render_template
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask_cors import CORS


tokenizer = AutoTokenizer.from_pretrained("satvikag/chatbot")
model = AutoModelForCausalLM.from_pretrained("satvikag/chatbot")


app = Flask(__name__)
CORS(app)


@app.route('/', methods=[ 'POST', 'GET'])
def dd():
    if(request.method=='POST'):
        text = request.form.get('text')
        if text is None:
            return "No text found in session"
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
            # return ans in json format
            return ans
    else:
        return render_template('index.html')
    
@app.route('/api', methods=[ 'POST'])
def getRes():
    if(request.method=='POST'):
        print(request.get_json())
        text = request.get_json()['text']
        if text is None:
            return "No text found in session"
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
            return jsonify({'message': ans})
   

if __name__=='main':
    app.run(debug=True)