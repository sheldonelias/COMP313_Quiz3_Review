import matplotlib.pyplot as plt

# Holds the coord values
tri_shape_x = []
tri_shape_y = []
tri_shape_z = []

# Holds the coordinate values in point vector lists.
tri_shape_points = []

# Holds the enumerated vertices, but after decrementing to make them zero-based.
tri_shape_f = []

def importObj(shape_name):

    # Import the OBJ
    file = open(shape_name + '.obj')

    vertex_count = 0

    # Fills the list to become 2d matrices (list of lists) of point vectors and coord lists
    list_of_lines = file.readlines()
    for line in list_of_lines:
        if line[0] == 'v':
            vertex_count += 1
            #print(line)
            line_v = line.strip('v \n')
            #print(line_v)
            pnt_vect = line_v.split(' ')

            for index, str in enumerate(pnt_vect):
                # print(str)
                pnt_vect[index] = float(str)

            # print('pnt_vect', pnt_vect)
            tri_shape_points.append(pnt_vect)
            tri_shape_x.append(pnt_vect[0])
            tri_shape_y.append(pnt_vect[1])
            tri_shape_z.append(pnt_vect[2])

        # Creates the face list
        if line[0] == 'f':

            line_f = line.strip('f \n')
            face = line_f.split(' ')
            for index, vector in enumerate(face):
                point_val = vector[0]
                face[index] = int(point_val) - 1
            # print(face)
            tri_shape_f.append(face)

    '''
    print('tri_shape_f')
    print(tri_shape_f)
    print('tri_shape_points')
    print(tri_shape_points)
    '''
    return vertex_count, tri_shape_x, tri_shape_y, tri_shape_z, tri_shape_points, tri_shape_f
    pass


def plot_shape(tri_shape_points, tri_shape_f):

    # GRID SETUP FOR SEQUENTIAL COMBINED ROTATIONS
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.axis([-2, 2, -2, 2])
    plt.axis('on')
    plt.grid(True)

    # Loop to plot all tris
    for face in tri_shape_f:
        # plt.plot([0,1],[0,1], color='k')
        # vertex 0 to 1
        plt.plot([ tri_shape_points[  face[0] ] [0], tri_shape_points[ face[1]] [0] ],
                 [ tri_shape_points[  face[0] ] [1], tri_shape_points[ face[1]] [1] ],
                 color='k')
        # vertex 1 to 2
        plt.plot([ tri_shape_points[  face[1] ] [0], tri_shape_points[ face[2]] [0] ],
                 [ tri_shape_points[  face[1] ] [1], tri_shape_points[ face[2]] [1] ],
                 color='red')
        # vertex 2 to 0
        plt.plot([ tri_shape_points[  face[2] ] [0], tri_shape_points[ face[0]] [0] ],
                 [ tri_shape_points[  face[2] ] [1], tri_shape_points[ face[0]] [1] ],
                 color='k')

        pass

    plt.show()
    pass


def main():
    importObj('tetrahedron') # Choose from cube, tetrahedron, octahedron
    plot_shape(tri_shape_points, tri_shape_f)
    pass

# main()