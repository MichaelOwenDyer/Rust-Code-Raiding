import math


def calculate_tries_with_striping(team_size, code_position):
    return math.ceil(code_position / team_size)


def calculate_tries_with_chunking(team_size, code_position):
    per_member = math.ceil(10000 / team_size)
    return code_position % per_member + 1


if __name__ == '__main__':
    size = 2
    while size <= 100:
        total_stripe, total_chunk, total_count = 0, 0, 0
        code_pos = 1
        with open('codes.csv', 'r') as codes:
            for code in codes:
                code_count = int(code[5:])
                total_stripe += calculate_tries_with_striping(size, code_pos) * code_count
                total_chunk += calculate_tries_with_chunking(size, code_pos) * code_count
                total_count += code_count
                code_pos += 1
        avg_tries_with_striping = total_stripe / total_count
        avg_tries_with_chunking = total_chunk / total_count
        print(size, avg_tries_with_striping, avg_tries_with_chunking)
        size += 1
