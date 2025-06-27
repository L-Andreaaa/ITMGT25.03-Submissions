def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if to_member in social_graph[from_member]["following"]:
        a = True #FROM follows TO
    else:
        a = False #FROM does not follow TO
    
    if from_member in social_graph[to_member]["following"]:
        b = True #TO follows FROM
    else:
        b = False #TO does not follow FROM
        
    if a == True and b == True:
        status = "friends"
    elif a == True and b == False:
        status = "follower"
    elif a == False and b == True:
        status = "followed by"
    else:
        status = "no relationship"

    return status

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    status = 0
    winner = ""
    
    for row in range(len(board)):
        if len(set(board[row])) == 1:
            if "" in board[row]:
               status
               winner 
            else:
                status = status + 1
                winner = board[row][0]
        else:
            status
            winner 
      
    flip = []
    for row in range(len(board)):
        for col in range(len(board)):
            flip.append(board[col][row])
        if len(set(flip)) == 1 and "" not in flip:
            status = status + 1
            winner = flip[0]
            break
        elif len(set(flip)) != 1:
            status
            winner
            flip.clear()
    
    diagonal_1 = []
    diagonal_2 = []
    
    for point in range(len(board)):
        diagonal_1.append(board[point][point])
        diagonal_2.append(board[point][len(board[1]) - (point + 1)])
    if len(set(diagonal_1)) == 1:
        status = status + 1
        winner = diagonal_1[0]
    elif len(set(diagonal_2)) == 1:
        status = status + 1
        winner = diagonal_2[0]
    else:
        status
        winner

    all_board = []
    for row in range(len(board)):
        for col in range(len(board)):
            all_board.append(board[col][row])
    if len(set(all_board)) == 1 and all_board[0] == "":
        status
    
    if status == 0:
        winner = "NO WINNER"

    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    minutes = 0
    route = list(route_map.values())  
    list_legs = list(route_map)
   
    for first in range(len(list_legs)):
        if first_stop == list_legs[first][0]: 
            for second in range(len(list_legs)): # 0, 1, 2
                if second_stop == list_legs[(first + second)%len(list_legs)][1]:
                    minutes = minutes + route[(first + second)%len(list_legs)]["travel_time_mins"]
                    break
                else:
                    minutes = minutes + route[(first + second)%len(list_legs)]["travel_time_mins"]

    return minutes