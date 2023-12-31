import g4f
import asyncio
import os
import time

# _providers = ''
# for i in os.listdir('.\g4f\Provider'):
#     if i.endswith(".py") and i != "__init__.py":
#         _providers += f'g4f.Provider.{i[:-3]},\n'
# print(_providers)





        




class GetProviders:
    def __init__(self) -> None:
        self._providers = [
    g4f.Provider.AiAsk,
    g4f.Provider.Aichat,        
    g4f.Provider.AiChatOnline,  
    g4f.Provider.AItianhu,      
    g4f.Provider.AItianhuSpace, 
    g4f.Provider.base_provider, 
    g4f.Provider.Berlin,        
    g4f.Provider.Bing,
    g4f.Provider.ChatAnywhere,  
    g4f.Provider.ChatBase,      
    g4f.Provider.ChatForAi,     
    g4f.Provider.Chatgpt4Online,
    g4f.Provider.ChatgptAi,     
    g4f.Provider.ChatgptDemo,   
    g4f.Provider.ChatgptDemoAi,
    g4f.Provider.ChatgptFree,
    g4f.Provider.ChatgptLogin,
    g4f.Provider.ChatgptNext,
    g4f.Provider.ChatgptX,
    g4f.Provider.DeepInfra,
    g4f.Provider.FakeGpt,
    g4f.Provider.FreeGpt,
    g4f.Provider.GeekGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.GptChatly,
    g4f.Provider.GptForLove,
    g4f.Provider.GptGo,
    g4f.Provider.GptGod,
    g4f.Provider.GptTalkRu,
    g4f.Provider.Hashnode,
    g4f.Provider.Koala,
    g4f.Provider.Liaobots,
    g4f.Provider.Llama2,
    g4f.Provider.MyShell,
    g4f.Provider.OnlineGpt,
    g4f.Provider.Opchatgpts,
    g4f.Provider.PerplexityAi,
    g4f.Provider.Phind,
    g4f.Provider.Pi,
    g4f.Provider.retry_provider,
    g4f.Provider.TalkAi,
    g4f.Provider.Vercel,
    g4f.Provider.Ylokh,
    g4f.Provider.You,
    g4f.Provider.Yqcloud
]
        self.fasters = []

    async def run_provider(self, provider: g4f.Provider.BaseProvider):
        startTime = time.time()
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=[{"role": "user", "content": "Hello"}],
                provider=provider,
            )
            timeEnd = round(time.time() - startTime, 2)
            print(f"{provider.__name__}:", 'работает за', timeEnd, 'секунд\n', response)
            
            if timeEnd <= 10:
                self.fasters.append(provider)
        except Exception as e:
            pass

    async def run_all(self):
        calls = [
            self.run_provider(provider) for provider in self._providers
        ]
        await asyncio.gather(*calls)


    def get_fasters(self):
        return self.fasters

async def main():
    getProviders = GetProviders()
    await getProviders.run_all()

    print(getProviders.fasters)

if __name__ == '__main__':
    asyncio.run(main())