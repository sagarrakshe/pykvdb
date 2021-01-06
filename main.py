from typing import Any, Optional

from inmemory_store import InMemory

SET = "SET"
GET = "GET"
DEL = "DEL"
INCR = "INCR"
INCRBY = "INCRBY"

VALID_COMMANDS = [SET, GET, DEL, INCR, INCRBY]


# TODO: Remove global store
store = InMemory()


def cmd_parser(cmd: str) -> Optional[Any]:
    tokens = cmd.split(" ")

    if tokens[0] not in VALID_COMMANDS:
        print("Incorrect command")
        return None

    # GET
    if tokens[0] == GET:
        if len(tokens) == 2:
            print(store.get(tokens[1]))
        else:
            print("Invalid GET Command")

    # SET
    elif tokens[0] == SET:
        if len(tokens) == 3:
            # TODO: Check for the valid int value before setting
            store.set(tokens[1], int(tokens[2]))
        else:
            print("Invalid SET command")

    # DEL
    elif tokens[0] == DEL:
        if len(tokens) == 2:
            store.delete(tokens[1])
        else:
            print("Invalid DEL command")

    # INCR
    elif tokens[0] == INCR:
        if len(tokens) == 2:
            store.incr(tokens[1])
        else:
            print("Invalid INCR command")

    # INCRBY
    elif tokens[0] == INCR:
        if len(tokens) == 3:
            # TODO: Type checking
            store.incrby(tokens[1], int(tokens[2]))
        else:
            print("Invalid INCR command")

    return tokens


def main():

    # TODO: Refactor cli interface
    while True:
        cmd = cmd_parser(input(">> "))
        if not cmd:
            break


if __name__ == "__main__":
    main()
