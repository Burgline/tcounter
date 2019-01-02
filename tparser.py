

def remove_other_chars(w, right_chars):
    buff = ''
    for c in w:
        for r in right_chars:
            if ord(c) == r:
                buff += buff.join(c)
                break
    return buff


def remove_sen(w, start_p, end_p):
    beg_to_del = w.find(start_p)
    end_to_del = w.find(end_p)
    while beg_to_del != -1 and end_to_del != -1:
        w = w[:beg_to_del] + ' ' + w[beg_to_del + end_to_del + len(end_p):]
        beg_to_del = w.find(start_p)
        end_to_del = w.find(end_p)
    return w


def remove_part(w, part):
    beg_to_del = w.find(part)
    while beg_to_del != -1:
        w = w[:beg_to_del] + ' ' + w[beg_to_del + len(part):]
        beg_to_del = w.find(part)
    return w


def get_top(*files):
    l = {}
    #whitelisted characters:
    good_chars = [i for i in range(ord('0'), ord('9')+1)]
    good_chars.extend([i for i in range(ord('a'), ord('z') + 1)])
    good_chars.extend([i for i in range(ord('а'), ord('я') + 1)])
    good_chars.append(ord('ё'))
    good_chars.append(ord('-'))
    for f in files:
        c = open(f, 'r', encoding='utf8')
        pstr = c.readline()
        while pstr != '':
            if '<div class="text">' in pstr:
                pstr = c.readline()
                while '</div>' not in pstr:
                    pstr = remove_sen(pstr, '<a', '</a>')
                    pstr = remove_sen(pstr, '<code>', '</code>')
                    pstr = remove_part(pstr, '<br>')
                    pstr = remove_part(pstr, '&quot')
                    for word in pstr.split():
                        word = word.lower()
                        word = remove_other_chars(word, good_chars)
                        if word == '':
                            continue
                        try:
                            l[word] = l[word] + 1
                        except KeyError:
                            l[word] = 1
                    pstr = c.readline()
            pstr = c.readline()
        c.close()
    return sorted(l.items(), key=lambda x: x[1], reverse=True)
