# Given a string, write a program that can check that the following symbols are balanced
# ((), [], {})


def balancing_symbols_lexer(some_string, balancing_pairs=["()"]):
    balancing_counters = {}
    for pair in balancing_pairs:
        balancing_counters[pair] = 0
    for pair in balancing_pairs:
        for i in some_string:
            if i is pair[0]:
                balancing_counters[pair] += 1
            if i is pair[1]:
                balancing_counters[pair] -= 1
            if balancing_counters[pair] < 0:
                break
    succeed = True
    for pair in balancing_pairs:
        succeed = succeed or False
        if balancing_counters[pair] < 0:
            print("Fail: %s missing %s" % (pair[1], pair[0]))
            succeed = False
        elif balancing_counters[pair] > 0:
            succeed = False
            print("Fail: %s missing %s" % (pair[0], pair[1]))
    if succeed:
        print("Pass")


balancing_symbols_lexer("()")
balancing_symbols_lexer(")(")
balancing_symbols_lexer("(()")
balancing_symbols_lexer("app(djio)asdf((ad)a)")
balancing_symbols_lexer("app(djio())asdf()ad)a)")
balancing_symbols_lexer("app(djio((asdf()ad)a)")

print("\n\n\n")
balancing_symbols_lexer("([])", ["()", "[]"])
balancing_symbols_lexer("[])(", ["()", "[]"])
balancing_symbols_lexer("(){}", ["()", "[]", "{}"])
balancing_symbols_lexer("app(djio)asdf((ad)a)")
balancing_symbols_lexer("app(djio())asdf()ad)a)")
balancing_symbols_lexer("app(djio((asdf()ad)a)")
