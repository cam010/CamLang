try:
    from cl_parser import Parser
    from executor import Executor
    from functions import Funcs
    import sys

    from variables import Variables


    try:
        file = sys.argv[1]
    except:
            file = input("Path to file to open: ")
    with open(file, "r") as f:
        content = f.read()
    funcs = Funcs().functions
    parser = Parser(content)
    parser.make_tokens()
    executor = Executor(parser.tokens, funcs)
    executor.execute()
    Variables().reset_vars()
    input("Press RETURN to finish")
except Exception as e:
    print(e)
    input()

# try except for when converted to exe
