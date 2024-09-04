def count_word_lengths(s):
    assert all([x.isalpha() or x == " " for x in s])
    assert type(s) is str

    x = s.split(" ")
    final = []
    final_num = []
    count = 0
    for i in x:
        if i != "":
            final.append(i)

    for t in range(len(final)):
        for w in final[t]:
            count += 1
        final_num.append(count)
        count = 0

    return final_num


print(count_word_lengths("the quick  brown   fox jumped over     the lazy  dog"))
