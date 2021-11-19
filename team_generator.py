
def generate(team_size):
    if team_size < 2:
        return
    out = open(f'output/Size {team_size}.csv', 'w')
    for i in range(team_size):
        print(f'Player {i + 1}', end=',', file=out)
    print(file=out)
    current = 1
    with open('codes.csv', 'r') as codes:
        for code in codes:
            if current == team_size:
                print(code[:4], file=out)
                current = 1
            else:
                print(code[:4], end=',', file=out)
                current += 1


if __name__ == '__main__':
    lower = int(input('Please enter team size lower bound >= 2: '))
    if lower < 2:
        lower = 2
    upper = int(input('Please enter team size upper bound: '))
    if upper < lower:
        i = lower
        lower = upper
        upper = i
    i = lower
    while i <= upper:
        generate(i)
        print(f'Generated file for team size {i} at \'output/Size {i}.csv\'')
        i += 1
