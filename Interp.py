class Tokens(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def __str__(self):
        return 'Token({}, {})'.format(self.token, self.value)

    def __repr__(self):
        return self.__str__()

    class Interpreter(object):
        def __init__(self, tokens):
            self.tokens = tokens
            self.current = 0
            self.position = 0

        def Error(self, msg):
            raise Exception(msg)

        def Next(self):
            tokens = self.tokens
            if self.position >= len(tokens)-1:
                return None

            current = tokens[self.position]
            if current.isdigit():
                token = Tokens('NUMBER', int(current))
                self.position += 1
            elif current == '+':
                token = Tokens('PLUS', current)
                self.position += 1

            return token
            self.Error('Invalid token')

        def Expression(self):
            token = self.Next()
            if token is None:
                return None
            if token.token == 'NUMBER':
                return token.value
            elif token.token == 'PLUS':
                return self.Expression() + self.Expression()
            else:
                self.Error('Invalid token')

        def Run(self):
            return self.Expression()

        def Main(self):
            print(self.Run())

