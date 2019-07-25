import utils


def main(input: str) -> str:
    input_lines = input.split('\n')
    top_right_positions = input_lines[0].strip().split(' ')
    top_right_coord = tuple(int(position) for position in top_right_positions)

    # all first lines of the rovers
    rovers_first_lines = [line for index, line in enumerate(input_lines[1:]) if index % 2 == 0]
    rovers_second_lines = [line for index, line in enumerate(input_lines[1:]) if index % 2 != 0]

    final_rovers = []

    for first_line, second_line in zip(rovers_first_lines, rovers_second_lines):
        positions = first_line.strip().split(' ')[:2]
        rover_position = tuple(int(position) for position in positions)
        rover_direction = first_line.strip().split(' ')[2]
        for command in second_line:
            if command in ['L', 'R']:
                rover_direction = utils.get_new_direction(rover_direction, command)
            elif command == 'M':
                rover_position = utils.get_new_grid_point(rover_position, rover_direction)
                rover_position = utils.limit_grid_point(rover_position, top_right_coord)

        final_rovers.append(f'{str(rover_position[0])} {str(rover_position[1])} {rover_direction}')

    return " \n".join(final_rovers)

