#Ex 8-9,10,11 Messages

bunch_o_messages = ['Hey!',
                    'Where are you',
                    'How you doin?',
                    'im ok',
                    'what???',
                    'this is incredible',
                    'python is great',
                    'whats bitcoin?',
                    'coool m8 :)',
                    ]

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop()
        print("Sent message:", message)
        sent_messages.append(message)
    return sent_messages

show_messages(bunch_o_messages)

show_messages(send_messages(bunch_o_messages[:]))
