from PyTesting.src.watches import watchCollection



def test_create_person():
    watch_collection = watchCollection(name="Lance")
    assert watch_collection.name == "Lance"
    assert type(watch_collection.watches) == dict

def test_create_person_NoneType():
    watch_collection = watchCollection(name=None)
    assert watch_collection.name == "None"
    assert type(watch_collection.watches) == dict

def test_create_person_num():
    watch_collection = watchCollection(name=1010)
    assert watch_collection.name == "1010"
    assert type(watch_collection.watches) == dict


def test_create_person_num():
    watch_collection = watchCollection(name=1010)
    assert watch_collection.name == "Intent to Fail"
    assert type(watch_collection.watches) == dict