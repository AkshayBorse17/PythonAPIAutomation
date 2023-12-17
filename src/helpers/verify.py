
def statuscode(exp,act):
    assert exp==act, "Status code invalid..."

def json_key_not_null(key):
    assert key != 0, "Json key error..."


def response_key_not_none(key):
    assert key is not None, "Response value roor..."


def response_time(time):
    assert time<1000000000000000,"Response time issue..."
