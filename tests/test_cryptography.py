from cryptography.cryptography import encrypt, decrypt, crack


# encrypt a string with a given shift
def test_encrypt():
    to_encrypt = 'Besto Friendo'
    actual = encrypt(to_encrypt, 7)
    expected = "Ilzav Myplukv"
    assert actual == expected
# decrypt a previously encrypted string with the same shift.
def test_decrypt():
    to_decrypt = "Ilzav Myplukv"
    actual = decrypt(to_decrypt, 7)
    expected = "Besto Friendo"
    assert actual == expected

# encryption should handle upper and lower case letters.
def test_encrypt_upper_and_lower():
    to_encrypt = 'Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.'
    actual = encrypt(to_encrypt, 32)
    expected = 'Lkgx oy tuz kbor. Oz zkrry eua cngz euax ckgqtkyy oy. Gtj utik eua qtuc euax ckgqtkyy, eua igt hkiusk yzxutmkx gy ckrr gy qotjkx.'
    assert actual == expected


# encryption should allow non-alpha characters but ignore them, including white space.
def test_non_alpha():
    to_encrypt = 'Hard work is worthless for those that don`t believe in themselves.'
    actual = encrypt(to_encrypt, 8)
    expected = 'Pizl ewzs qa ewzbptmaa nwz bpwam bpib lwv`b jmtqmdm qv bpmuamtdma.'
    assert actual == expected
    
# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack():
    encrypted = encrypt('It was the best of times, it was the worst of times.', 8)
    actual = crack(encrypted)
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected
