def arithmetic_arranger(problems: list[str], show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    base_result = []
    for problem in problems:
        sum_problem = problem.split('+')
        sub_problem = problem.split('-')
        if len(sum_problem) == 1 and len(sub_problem) == 1:
            return "Error: Operator must be '+' or '-'."
        split_problem = sum_problem if len(sum_problem) > 1 else sub_problem
        op: str = '+' if len(sum_problem) > 1 else '-'
        num1, num2 = split_problem[0].strip(), split_problem[1].strip()

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not num1.isnumeric() or not num2.isnumeric():
            return "Error: Numbers must only contain digits."

        result = None
        if op == '+':
            result = int(num1) + int(num2)
        if op == '-':
            result = int(num1) - int(num2)
        # Calculate the number on each line
        num_slash = max(len(f'{op} {num1}'), len(f'{op} {num2}'), len(str(result)) - (result < 0))
        base_result.append((num_slash, (num1, f'{op} {num2}', num_slash, str(result))))

    # DOING FORMATTER
    problem_spacing: int = 4
    result = []
    for idx in range(4):
        arr = []
        for spacing, entities in base_result:
            if isinstance(entities[idx], int):
                # Draw '-' for the result
                arr.append('-' * spacing)
            else:
                if not show_answers and idx == 3:
                    # Skip the result
                    break
                # Draw the entities
                if idx == 1:
                    op, num = entities[idx].split()
                    arr.append(op + num.rjust(spacing - 1))
                else:
                    arr.append(entities[idx].rjust(spacing))
        if arr:
            result.append((' ' * problem_spacing).join(arr))

    return '\n'.join(result)


if __name__ == '__main__':
    print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
