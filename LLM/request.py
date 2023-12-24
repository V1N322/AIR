import g4f
import errors

class LMRequest:
    def __init__(self, model = g4f.models.default, provider = None, debug = False):
        self.debug = debug
        self.provider = provider
        self.model = model
        if debug:
            print(f'LMRequest: model = {model}, provider = {provider.__name__}')

    def _send_with_provider(self, text, prov):
        print('Request in process...')
        return g4f.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": text}],
            provider=prov
        )
    
    def _send_without_provider(self, text):
        print('Request in process...')
        return g4f.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": text}]
        )

    def send(self, text):
        try:
            if self.provider:
                print(f'LMRequest.send: provider = {self.provider}')
                return self._send_with_provider(text, self.provider)
            else:
                print(f'LMRequest.send: provider = None')
                return self._send_without_provider(text)

        except Exception as e:
            print('Exception:', e)
            return f'{errors.bad_response_from_a_model}: {e}'