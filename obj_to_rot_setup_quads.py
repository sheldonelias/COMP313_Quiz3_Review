import matplotlib.pyplot as plt


# Holds the coord values
quad_shape_x = []
quad_shape_y = []
quad_shape_z = []

# Holds the coordinate values in point vector lists.
quad_shape_points = []

# Holds the enumerated vertices, but after decrementing to make them zero-based.
quad_shape_f = []



def importObj(shape_name):

    # Import the OBJ
    file = open(shape_name + '.obj')

    # Fills the list to become 2d matrices (list of lists) of point vectors and coord lists
    list_of_lines = file.readlines()
    vertex_count = 0
    for line in list_of_lines:
        if line[0] == 'v':
            vertex_count += 1
            #print(line)
            line_v = line.strip('v \n')
            #print(line_v)
            pnt_vect = line_v.split(' ')

            for index, str in enumerate(pnt_vect):
                pnt_vect[index] = float(str)

            # print('pnt_vect', pnt_vect)
            quad_shape_points.append(pnt_vect)
            quad_shape_x.append(pnt_vect[0])
            quad_shape_y.append(pnt_vect[1])
            quad_shape_z.append(pnt_vect[2])

        # Creates the face list
        if line[0] == 'f':

            line_f = line.strip('f \n')
            face = line_f.split(' ')

            for index, vector in enumerate(face):
                point_val = vector[0]
                face[index] = int(point_val) - 1
            # print(face)
            quad_shape_f.append(face)

    '''
    print('quad_shape_f')
    print(quad_shape_f)
    print('quad_shape_points')
    print(quad_shape_points)
    '''

    return vertex_count, quad_shape_x, quad_shape_y, quad_shape_z, quad_shape_points, quad_shape_f

    pass


def plot_shape(quad_shape_points, quad_shape_f):

    # GRID SETUP FOR SEQUENTIAL COMBINED ROTATIONS
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.axis([-2, 2, -2, 2])
    plt.axis('on')
    plt.grid(True)

    # Loop to plot all faces for each quad
    for face in quad_shape_f:
        # plt.plot([0,1],[0,1], color='k')
        # vertex 0 to 1
        plt.plot([ quad_shape_points[  face[0] ] [0], quad_shape_points[ face[1]] [0] ],
                 [ quad_shape_points[  face[0] ] [1], quad_shape_points[ face[1]] [1] ],
                 color='k')
        # vertex 1 to 2
        plt.plot([ quad_shape_points[  face[1] ] [0], quad_shape_points[ face[2]] [0] ],
                 [ quad_shape_points[  face[1] ] [1], quad_shape_points[ face[2]] [1] ],
                 color='k')

        # vertex 2 to 3
        plt.plot([ quad_shape_points[  face[2] ] [0], quad_shape_points[ face[3]] [0] ],
                 [ quad_shape_points[  face[2] ] [1], quad_shape_points[ face[3]] [1] ],
                 color='k')
       
        # vertex 3 to 0
        plt.plot([ quad_shape_points[  face[3] ] [0], quad_shape_points[ face[0]] [0] ],
                 [ quad_shape_points[  face[3] ] [1], quad_shape_points[ face[0]] [1] ],
                 color='k')

        pass

    plt.show()
    pass


def main():
    importObj('cube')
    plot_shape(quad_shape_points, quad_shape_f)
    pass

# main()