
def generate(team_size):
    if team_size < 2:
        return
    out = open(f'output/Size {team_size}.csv', 'w')
    team_member = 1
    while team_member < team_size:
        print(f'Player {team_member}', end=',', file=out)
        team_member += 1
    print(f'Player {team_size}', file=out)
    current = 1
    with open('codes.csv', 'r') as codes:
        for index, code in enumerate(codes):
            if current == team_size or index == 9999:
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
