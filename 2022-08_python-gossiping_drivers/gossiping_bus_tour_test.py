from gossiping_bus_tour import gossiping_bus_tour


def test_no_bus_today():
    routes = []
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "never")


def test_one_route():
    routes = [[1, 2, 3, 4]]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "0")


def test_2_routes_first_stop():
    routes = [
        [1],
        [1],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "1")


def test_2_routes_never():
    routes = [
        [1],
        [2],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "never")
