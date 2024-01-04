from GPT import GPT

cutPrompt = """
Напиши по пунктам САМУЮ важную информацию из нашего диалога.  В таком формате:

1. **(Сущность): (Название Если есть)**
   - (Факт 1)
   - (Факт 2)

Пример:
1. **Пользователь: Артем**
   - У него хорошая погода.
   - Он интересуется программированием.

2. **Ассистент: chatGPT, Элизар**
   - Является моделью GPT
   - Рассказывает про молнию.
   - Знает Артема.

Факты должны быть короткими - до 5 слов.
"""

cutPrompt2 = """
Напиши по пунктам САМУЮ важную информацию из нашего диалога. Ответ должен быть не больше 20 слов. Пример:
```Артем - У него хорошая погода. Он интересуется программированием.```
"""

cutPrompt3 = """
Извлеки информацию из нашего диалога по такому шаблону:
```
Извлеченная информация:
Участники диалога: [Участники диалога]
Тема диалога: [Тема диалога]
Важная информация: [Важная информация]
```
"""

def main():
    gpt = GPT()

    # print(gpt.send_message({'role': 'systems', 'content': 'Текст для анализа: Пример текста, в котором есть имена, номера телефонов и должности.'}))

    while True:
        userText = input('>>> ')
        if userText == 'exit':
            break
        elif userText == 'cut':
            print('Сокращаем чат размером:', len(gpt.history))
            lastAnswer = gpt.history[-1]['content']
            lastRequest = gpt.history[-2]['content']
            history = gpt.history
            gpt.history = []
            gpt.history = [{'role': 'system', 'content': gpt.send_message({'role': 'user', 'content': f'```\n{history}\n```\n{cutPrompt3}'})},
                           {'role': 'user', 'content': lastRequest},
                           {'role': 'assistant', 'content': lastAnswer}]
            print('Чат сокращен до:', len(gpt.history), '\n')
            print(gpt.history[0])
        else:
            print('\n---------------------\n\n', gpt.send_message({'role': 'user', 'content': userText}), '\n\n---------------------\n')
if __name__ == "__main__":
    main()