def longest_repetition(chars):
    #my_set = set(chars)
    my_dict= {}
    for k in range (0, len(chars)):
        if chars[k] in my_dict.keys():
            continue
        else:
            my_dict [chars[k]] = 0
    for s in my_dict.keys():
        sum = 0
        for k in range (0,len(chars)):
            if s == chars[k]:
                sum+=1
                if sum > my_dict.get(s):
                    my_dict[s] = sum
            else:
                if sum > my_dict.get(s):
                   my_dict[s] = sum
                sum = 0
    try:
        max_value = max(list(my_dict.values()))
    except ValueError:
        return '', 0
    for k, v in my_dict.items():
        if v == max_value:
            return k,v

def solution (chars):
    last = ''
    count = 0
    max = (last, count)
    for c in chars:
        if c == last:
            count += 1
        else:
            last = c
            count = 1
        if max[1] < count: max = (last, count)
    return max


print(longest_repetition("5vs43awq1cypzd32xqkfzi4874ygr3asraqitgkdxjhfg505g4eb4e4vvb0hebn1jtqajjta36epd5bof7tm3iegtvsca7ilia6y7u6d48xk1etzgtned1dtiwlopz1d42jso873cfmb42awnb2dkjnr7l72ze03v7lpptg1ucoweivmaq979xht7sx0q62uv9c3yzpta142hyo4gjf4yv770zuc0frqx188ouiio1o2xjnp12otkrstnwr10vc30vesbfk3pm4uq9z9la51n04sm0o1uomb0czbfvn0hkplfdxnrerxu6s2sjfylambxchwz36mf1kawz5krknl2b2tk2ax3h9ydkfyfiimpoulkitczh8c7x4k9ba473wf9uuzcjkfmrfiek75zbqb9d065w29ovrh7v6p0zobzzvggp7auiywt4o1b5ri55ph64xywfhxqq1c3olptu07dlncd7x30fqdw5ubpcgywiy0l6yyg9n1"))
print(solution("5vs43awq1cypzd32xqkfzi4874ygr3asraqitgkdxjhfg505g4eb4e4vvb0hebn1jtqajjta36epd5bof7tm3iegtvsca7ilia6y7u6d48xk1etzgtned1dtiwlopz1d42jso873cfmb42awnb2dkjnr7l72ze03v7lpptg1ucoweivmaq979xht7sx0q62uv9c3yzpta142hyo4gjf4yv770zuc0frqx188ouiio1o2xjnp12otkrstnwr10vc30vesbfk3pm4uq9z9la51n04sm0o1uomb0czbfvn0hkplfdxnrerxu6s2sjfylambxchwz36mf1kawz5krknl2b2tk2ax3h9ydkfyfiimpoulkitczh8c7x4k9ba473wf9uuzcjkfmrfiek75zbqb9d065w29ovrh7v6p0zobzzvggp7auiywt4o1b5ri55ph64xywfhxqq1c3olptu07dlncd7x30fqdw5ubpcgywiy0l6yyg9n1"))