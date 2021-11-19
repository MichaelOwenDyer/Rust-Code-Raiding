
def calculate_probabilities():
    out = open('output/Code Probabilities.csv', 'w')
    with open('codes.csv', 'r') as codes:
        i, total = 0, 0
        for code in codes:
            i += 1
            total += int(code[5:])
        print(f'Counted total weight of {total} over {i} elements.\nPrinting probabilities...')
        codes.seek(0)
        cumulative = 0
        print('Code,Count,Individual Probability,Cumulative Probability', file=out)
        for code in codes:
            individual = int(code[5:])
            cumulative += individual
            print(f'{code[:4]},{individual},{(individual / total):.20f},{(cumulative / total):.20f}', file=out)

if __name__ == '__main__':
    calculate_probabilities()
