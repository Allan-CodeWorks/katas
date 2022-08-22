def test_dummy():
    assert(3 == 3)


def test_no_bus_today():
    gossiping_done = gossiping_bus_tour([])
    assert(gossiping_done == "never")
