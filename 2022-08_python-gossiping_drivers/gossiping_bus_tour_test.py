from gossiping_bus_tour import gossiping_bus_tour


def test_dummy():
    assert(3 == 3)


def test_no_bus_today():
    gossiping_done = gossiping_bus_tour([])
    assert(gossiping_done == "never")


def test_one_route():
    routes = [[1, 2, 3, 4]]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "0")
