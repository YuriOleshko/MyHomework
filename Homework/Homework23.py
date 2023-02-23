def popular_words(txt, lst):
    txt = txt.lower().split()
    result = dict()
    for i in lst:
        result[i] = txt.count(i)
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
print('OK')
