import neuroLang

def chat():
    rqst = neuroLang.LModel()


    while True:
        msg = input(' > ')

        message = rqst.request(msg)

        for chunk in message:
            print(chunk.choices[0].delta.content, end="", flush=True)

def main():
    chat()

if __name__ == '__main__':
    main()