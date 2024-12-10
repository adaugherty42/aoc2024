reports = []

with open("inputs/day2") as fp:
    for line in fp.read().split('\n'):
        reports.append([int(x) for x in line.split()])

def is_report_safe(report):
    if not report: return False
    if len(report) == 1: return True

    is_always_decreasing, is_always_increasing = True, True

    for i in range(1, len(report)):
        # if diff between adjacent levels is not in range [1,3], fail immediately
        if not 1 <= abs(report[i] - report[i-1]) <= 3: return False

        if is_always_decreasing and report[i] >= report[i-1]: is_always_decreasing = False
        if is_always_increasing and report[i] <= report[i-1]: is_always_increasing = False

    # if is_always_decreasing or is_always_increasing:
    #     print(report)

    return is_always_decreasing or is_always_increasing

def is_report_safe_with_removal(report):
    if is_report_safe(report): return True

    for i in range(0, len(report)):
        if is_report_safe(report[:i] + report[i+1:]): return True

    return False


# part 1
part_1_res = sum([1 if is_report_safe(report) else 0 for report in reports])
print(f'part 1: {str(part_1_res)}')

# part 2
part_2_res = sum([1 if is_report_safe_with_removal(report) else 0 for report in reports])
print(f'part 2: {str(part_2_res)}')