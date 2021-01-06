from inmemory_store import InMemory

store = InMemory()

# for get_key testcase
store.set("global_key", 100)


def test_get_key():
    """Test fetching a key."""

    assert 100 == store.get("global_key")


def test_set_key():
    """Test setting a key."""
    key = "foo"

    store.set(key, 1)
    v = store.get(key)

    assert v == 1


def test_delete_key():
    """Test deleting a key."""
    key = "foobar"

    store.set(key, 1)
    v = store.get(key)

    assert v == 1

    store.delete(key)
    v = store.get(key)

    assert v is None


def test_increment_key():
    """Test incrementing a key by 1."""
    key = "bar"

    store.set(key, 1)
    store.incr(key)

    v = store.get(key)

    assert v == 2


def test_increment_by():
    """Test incrementing a key by a value."""

    key = "bar"

    store.set(key, 1)
    store.incrby(key, 10)

    v = store.get(key)

    assert v == 11
