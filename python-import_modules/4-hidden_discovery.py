#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util

    # Load the compiled module from hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names, filter those that don't start with '__', sort, and print
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
