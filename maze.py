


def is_boundary_move(move, width, height):

	if (move[0] < 0) or (move[0] >= width) or (move[1] < 0) or (move[1] >= height):
		return 1
	else:
		return 0




# All possible moves from current position
def possible_moves(current_pos, visited_nodes, width, height):

	x_pos = current_pos[0]
	y_pos = current_pos[1]

	move_1 = (x_pos - 1, y_pos)
	move_2 = (x_pos, y_pos + 1)
	move_3 = (x_pos + 1, y_pos)
	move_4 = (x_pos, y_pos - 1)

	possible_moves = []
	valid_moves    = []
	possible_moves = [move_1, move_2, move_3, move_4]

	# Loop through and remove invalid boundary ones
	for move in possible_moves:
		if not is_boundary_move(move, width, height) and move not in visited_nodes:
			valid_moves.append(move)
	

	return valid_moves

def gen_maze(width, height, start_pos, end_pos, visited_nodes, valid_path):

	# Init visited nodes
	visited_nodes.append(start_pos)

	# We're done
	if start_pos == end_pos:
		print valid_path
		return (1,valid_path)



	# Get possible moves
	poss_moves = possible_moves(start_pos, visited_nodes, width, height)

	# For each possible move, recursively call gen_maze with the new start_position
	# and stop when you start_pos = end_pos
	for move in poss_moves:
		# Add the next move to the valid path
		length = len(valid_path)
		valid_path.append(move)
		print valid_path
		ret = gen_maze(width, height, move, end_pos, visited_nodes, valid_path)

		# This was the final move, so just pass the valid path back up the stack
		if ret[0] == 1:
			return (1,ret[1])

		# If you reach here, path is dead, so remove next move from valid path
		valid_path.remove(move)

	# If you reach here, there are no possible paths from the current position
	# that result in reaching the end
	return (0,valid_path)



visited_nodes = []

ret = gen_maze(4,4,(0,0),(1,0),[],[])

if ret[0] == 1:
	print "Valid path found!",ret[1]
