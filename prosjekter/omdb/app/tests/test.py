import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.dont_write_bytecode = True #NO PYCHACHE
sys.path.insert(1, '../app')
import backend
import json

def test_hent_sok():
    imdbID = "tt0241527"
    result = backend.hent_film_info(imdbID)
    with open("./tests/fav_test.json") as f:
        data = json.load(f)

    assert vars(result) == data, "Data stemmer ikke!"

test_hent_sok()