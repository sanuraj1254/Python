def rem(i, word):
    for itrm in i:
        i.remove(word)
        return i

i = ["sanu","hbvd","udgfkh","kjdfgh"]

print(rem(i , "sanu"))