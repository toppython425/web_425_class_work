class SushiError(Exception):
    def __init__(self, message, sushi):
        super().__init__(message)
        self.sushi = sushi


class TooFewRiceError(SushiError):
    def __init__(self, message, sushi, rice):
        super().__init__(message, sushi)
        self.rice = rice


class TooMuchRiceError(SushiError):
    def __init__(self, message, sushi, rice):
        super().__init__(message, sushi)
        self.rice = rice


def make_sushi(sushi, rice):
    if sushi not in ['california', 'philadelphia', 'yamato']:
        raise SushiError('Позиции нет в меню!', sushi)
    if rice < 50:
        raise TooFewRiceError('Слишком мало риса!!', sushi, rice)
    elif rice > 100:
        raise TooMuchRiceError('Слишком много риса!!', sushi, rice)

    return f'Ваши суши: {sushi} готовы!'


if __name__ == '__main__':
    for (sushi, rice) in [('bismark', 70), ('california', 0), ('philadelphia', 75), ('yamato', 110), ('bismark', 0)]:
        try:
            print(make_sushi(sushi, rice))
        except TooFewRiceError as TFRE:
            print(f'{TFRE}: {TFRE.sushi}, {TFRE.rice}')
        except TooMuchRiceError as TMRE:
            print(f'{TMRE}: {TMRE.sushi}, {TMRE.rice}')
        except SushiError as SE:
            print(f'{SE}: {SE.sushi}')
