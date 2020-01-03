from cipher import encript, decript_bot

def test_in_and_out():
    string = 'This is a test string. I plan to use this to see if the encription works. The one quirk is that it doesn\'t handle upper case letters'
    assert decript_bot(encript(string, 10)) == string.lower()