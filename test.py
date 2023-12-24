from LLM import request
import g4f


print(request.LMRequest(provider=g4f.Provider.FakeGpt).send('Привет!'))