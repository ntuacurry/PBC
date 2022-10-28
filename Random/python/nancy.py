string = input()

list = string.split()

axis_x = int(list[0])
axis_y = int(list[1])
robot_1_x = int(list[2])
robot_1_y = int(list[3])
time_1_1 = int(list[4])  # E1
time_1_2 = int(list[5])  # N1
energy_1 = int(list[6])
robot_2_x = int(list[7])
robot_2_y = int(list[8])
time_2_1 = int(list[9])  # E2
time_2_2 = int(list[10])  # N2
energy_2 = int(list[11])

if energy_1 >= energy_2:
    for time in range(1, energy_1 + 1):
        if energy_1 >= time:
            if (time % (time_1_1 + time_1_2)) <= time_1_2 and (time % (time_1_1 + time_1_2)) <= time_1_2 >= 1:
                robot_1_y += 1
                if robot_1_y == axis_y:
                    robot_1_y = 0
            else:
                robot_1_x += 1
                if robot_1_x == axis_x:
                    robot_1_x = 0
        else:
            robot_1_x = robot_1_x
            robot_1_y = robot_1_y

        if energy_2 >= time:
            if (time % (time_2_1 + time_2_2)) <= time_2_1 and (time % (time_2_1 + time_2_2)) >= 1:
                robot_2_x += 1
                if robot_2_x == axis_x:
                    robot_2_x =0
            else:
                robot_2_y += 1
                if robot_2_y == axis_y:
                    robot_2_y = 0
        else:
            robot_2_x = robot_2_x
            robot_2_y = robot_2_y

        if robot_1_x == robot_2_x and robot_1_y == robot_2_y:
            print("robots explode at time " + str(time))
            break

    if robot_1_x != robot_2_x or robot_1_y != robot_2_y:
        print("robots will not explode")

else:  
    for time in range(1, energy_2 + 1):
        if energy_1 >= time:
            if (time % (time_1_1 + time_1_2)) <= time_1_2 and (time % (time_1_1 + time_1_2)) <= time_1_2 >= 1:
                robot_1_y += 1
                if robot_1_y == axis_y:
                    robot_1_y = 0
            else:
                robot_1_x += 1
                if robot_1_x == axis_x:
                    robot_1_x = 0
        else:
            robot_1_x = robot_1_x
            robot_1_y = robot_1_y

        if energy_2 >= time:
            if (time % (time_2_1 + time_2_2)) <= time_2_1 and (time % (time_2_1 + time_2_2)) >= 1:
                robot_2_x += 1
                if robot_2_x == axis_x:
                    robot_2_x =0
            else:
                robot_2_y += 1
                if robot_2_y == axis_y:
                    robot_2_y = 0
        else:
            robot_2_x = robot_2_x
            robot_2_y = robot_2_y

        if robot_1_x == robot_2_x and robot_1_y == robot_2_y:
            print("robots explode at time " + str(time))
            break

    if robot_1_x != robot_2_x or robot_1_y != robot_2_y:
        print("robots will not explode")