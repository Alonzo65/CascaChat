import json 
import random

#builds our conversation overtime

def get_recent_messages():
    
    #Define the file name and learn instruction
    file_name = "stored_Data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are conversing and teaching the user about nuclear energy and other similar topics. Ask short questions to gauge the limit of knowledge that the user has on these topics. Your name is Casca. Keep your answers to under 50 words."
    }
    
    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humor."
    else:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include a rather challenging question."
        
    #Append instruction to messages
    messages.append(learn_instruction)
    
    #Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            
            #Append last 5 items of data
            if data:
                if len(data) < 7:
                    for item in data:
                        
                        messages.append(item)
                else:
                    for item in data[-7:]:
                        messages.append(item)
                        
    except Exception as e:
        print(e)
        pass
    
    
    #Return
    return messages
    
#Store Messages in our database
def store_messages(request_message, response_message):
    
    #Define the file name
    file_name = "stored_data.json"
    
    #Get recent messages
    messages = get_recent_messages()[1:]
    
    #Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    
    
    #Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)
        
        
#Reset messages
def reset_messages():
    #Overwrite current file with nothing
    open("stored_data.json", "w")
    