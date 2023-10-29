import hashlib

def loop_function(hash, use_salts, salts):
    with open('top-10000-passwords.txt', 'r') as file:
        for line in file:
            if use_salts:
                check = salts + line.strip('\n')
            else:
                check = line.strip('\n')
            ans = hashlib.sha1(check.encode()).hexdigest()
            if ans == hash:
                return line.strip('\n')
            elif use_salts:
                new_check = line.strip('\n') + salts
                answ = hashlib.sha1(new_check.encode()).hexdigest()
                if answ == hash:
                    return line.strip('\n')
    return "PASSWORD NOT IN DATABASE"

def crack_sha1_hash(hash, use_salts=False):
    if not use_salts:
        return loop_function(hash, False, None)
    else:
        with open('known-salts.txt', 'r') as salts:
            for line in salts:
                line = line.strip('\n')
                ans = loop_function(hash, True, line)
                if ans != "PASSWORD NOT IN DATABASE":
                    return ans
    return "PASSWORD NOT IN DATABASE"