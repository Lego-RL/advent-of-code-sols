with open("input.txt", "r") as f:
    # with open("fakeinput.txt", "r") as f:
    data = f.readlines()


class Operation:
    def __init__(self, operation_type: str, operand: int | None = None):
        """
        If double_operand is true,
        """

        self.operation_type = operation_type
        self.operand = operand

    def execute_operation(self, other_operand: int = 0) -> int:
        """
        other_operand should only be 0 in cases where monkey's
        operation uses its own operand as both operands for
        its affect on worry level
        """

        if self.operation_type == "+":
            if self.operand is None:
                return other_operand + other_operand
            else:
                return self.operand + other_operand

        # if not addition, must be multiplication
        if self.operand is None:
            return other_operand * other_operand

        else:
            return self.operand * other_operand

    def __str__(self):
        return f"{self.operation_type=}, {self.operand=}"


class Item:
    def __init__(self, worry_level: int):
        self.worry_level = worry_level


class Monkey:
    def __init__(
        self,
        name: str,
        items: list[Item],
        worry_level_operation: Operation,
        divisible_by: int,
        monkey_choices: list[int],
        times_inspected=0,
    ):
        self.name = name
        self.items = items
        self.worry_level_operation = worry_level_operation
        self.divisible_by = divisible_by
        self.monkey_choices = monkey_choices

        self.times_inspected = times_inspected


monkeys: list[list[str]] = []

# while newline_idx := data.index("\n"):
while len(data) > 0:
    try:
        newline_idx = data.index("\n")
        monkeys.append(data[:newline_idx])
        data = data[newline_idx + 1 :]

    # on last monkey
    except ValueError:
        monkeys.append(data)
        break

monkey_objs: list[Monkey] = []
for monkey in monkeys:
    monkey_name: str = monkey[0].strip().strip(":")

    starting_items_str: list[str] = monkey[1].strip("Starting items:").split(",")
    starting_items: list[Item] = [Item(int(item)) for item in starting_items_str]

    operation_str = monkey[2][monkey[2].index("=") + 2 :]
    operation_lst = operation_str.split(" ")
    operation_lst[-1] = operation_lst[-1].strip("\n")

    if operation_str.count("old") == 2:
        operation: Operation = Operation(operation_lst[1], None)

    else:
        operation: Operation = Operation(operation_lst[1], int(operation_lst[-1]))

    divisible_by: int = int(monkey[3].split(" ")[-1])

    true_monkey: int = int(monkey[4].split(" ")[-1])
    false_monkey: int = int(monkey[5].split(" ")[-1])
    monkey_choices = [true_monkey, false_monkey]

    monkey_objs.append(
        Monkey(monkey_name, starting_items, operation, divisible_by, monkey_choices)
    )

ROUNDS: int = 20

for round in range(ROUNDS):
    for monkey in monkey_objs:
        while monkey.items:
            monkey.times_inspected += 1

            # item = monkey.items[item_idx]
            item = monkey.items[0]

            # monkey inspects item
            item_worry_level: int = item.worry_level

            # worry level is increased
            item.worry_level = monkey.worry_level_operation.execute_operation(
                item_worry_level
            )

            # items's worry level is divided by 3 //
            item.worry_level = item.worry_level // 3

            # check worry level divisible by, throw item to correct monkey
            if item.worry_level % monkey.divisible_by == 0:
                monkey_objs[monkey.monkey_choices[0]].items.append(item)

            else:
                monkey_objs[monkey.monkey_choices[1]].items.append(item)
            del monkey.items[0]

num_inspections: list[int] = []
for monkey in monkey_objs:
    num_inspections.append(monkey.times_inspected)

num_inspections.sort()

most_inspected, second_most_inspected = num_inspections[-1], num_inspections[-2]

print(most_inspected * second_most_inspected)
