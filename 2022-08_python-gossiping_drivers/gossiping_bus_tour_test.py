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


def test_2_routes_second_stop():
    routes = [
        [1, 3],
        [2, 3],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "2")


def test_2_routes_stop_3():
    routes = [
        [1, 2, 3],
        [2, 1, 3],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "3")


def test_2_routes_stop_4():
    routes = [
        [1, 2, 1, 4],
        [2, 1, 3, 4],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "4")


def test_2_routes_stop_1_uneven():
    routes = [
        [1],
        [1, 2],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "1")


def test_3_routes_stop_3():
    routes = [
        [1, 2, 1, 2],
        [2, 1, 3, 1],
        [3, 2, 3, 4],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "3")


def test_3_routes_never():
    routes = [
        [1, 2, 1, 2],
        [2, 1, 2, 1],
        [3, 2, 3, 4],
    ]
    gossiping_done = gossiping_bus_tour(routes)
    assert(gossiping_done == "never")
