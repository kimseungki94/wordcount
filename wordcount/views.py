from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    # 단어 : 몇번 단어 : 몇번
    for word in words:
        # include
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            # add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})

    # 사전형 객체 : 왼쪽엔 키값, 오른쪽엔 value를 말함
