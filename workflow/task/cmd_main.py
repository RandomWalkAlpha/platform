import json
from cmd_manager import parse
from data.model import DataModel


def main():
    while True:
        model = None
        try:
            name = input("Input factor name:\n> ")
            exp = input("Input factor calculation expression:\n> ")
            model = DataModel(name, exp)
            parse.delay(json.dumps(model.__dict__))
            model.update('finished')
        except Exception:
            model.disabled()
            print("Error occurred!")
            continue


"""
This file is used to input the factor expression which is to be evaluated.
"""
if __name__ == '__main__':
    main()
