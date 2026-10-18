import random

from django.http import HttpResponse
from django.views import View

QUOTES = [
    ('Talk is cheap. Show me the code.', 'Linus Torvalds'),
    ('Simple is better than complex.', 'Tim Peters'),
    ('First, solve the problem. Then, write the code.', 'John Johnson'),
    ('Programs must be written for people to read.', 'Harold Abelson'),
    ('The best way to predict the future is to invent it.', 'Alan Kay'),
    ('Premature optimization is the root of all evil.', 'Donald Knuth'),
]


class RandomQuoteView(View):
    def get(self, request):
        text, author = random.choice(QUOTES)
        return HttpResponse(f'"{text}" - {author}')
