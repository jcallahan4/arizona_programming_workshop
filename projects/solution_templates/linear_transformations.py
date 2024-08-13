# linear_transformations.py
"""Volume 1: Linear Transformations.
Jake Callahan
Section 002
2018/09/18
"""
import time
from random import random

import numpy as np
from matplotlib import pyplot as plt


# Problem 1
def stretch(A, a, b):
    """
    Scale the points in A by a in the x direction and b in the
    y direction.

    Parameters:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        a (float): scaling factor in the x direction.
        b (float): scaling factor in the y direction.
    """
    raise NotImplementedError("Problem 1 incomplete!")


def shear(A, a, b):
    """
    Slant the points in A by a in the x direction and b in the
    y direction.

    Parameters:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        a (float): scaling factor in the x direction.
        b (float): scaling factor in the y direction.
    """
    raise NotImplementedError("Problem 1 incomplete!")


def reflect(A, a, b):
    """
    Reflect the points in A about the line that passes through the origin
    and the point (a,b).

    Parameters:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        a (float): x-coordinate of a point on the reflecting line.
        b (float): y-coordinate of the same point on the reflecting line.
    """
    raise NotImplementedError("Problem 1 incomplete!")


def rotate(A, theta):
    """
    Rotate the points in A about the origin by theta radians.

    Parameters:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        theta (float): The rotation angle in radians.
    """
    raise NotImplementedError("Problem 1 incomplete!")


def test_transforms():
    """
    Function that plots each type of transformation using
    the `horse.npy` array.
    """
    # Create stretch, shear, reflect, and rotated horses
    A = np.load("horse.npy")
    stretch_matrix = stretch(A, 1 / 2, 6 / 5)
    shear_matrix = shear(A, 1 / 2, 0)
    reflect_matrix = reflect(A, 0, 1)
    rotate_matrix = rotate(A, np.pi / 2)

    # Plot original horse
    ax1 = plt.subplot(2, 3, 1)
    ax1.plot(A[0], A[1], "k,")
    plt.axis([-1, 1, -1, 1])

    # Plot stretched horse
    ax2 = plt.subplot(2, 3, 2)
    ax2.plot(stretch_matrix[0], stretch_matrix[1], "k,")
    plt.axis([-1, 1, -1, 1])

    # Plot sheared horse
    ax3 = plt.subplot(2, 3, 3)
    ax3.plot(shear_matrix[0], shear_matrix[1], "k,")
    plt.axis([-1, 1, -1, 1])

    # Plot reflected horse
    ax4 = plt.subplot(2, 3, 4)
    ax4.plot(reflect_matrix[0], reflect_matrix[1], "k,")
    plt.axis([-1, 1, -1, 1])

    # Plot rotated horse
    ax5 = plt.subplot(2, 3, 5)
    ax5.plot(rotate_matrix[0], rotate_matrix[1], "k,")
    plt.axis([-1, 1, -1, 1])

    plt.show()


# Problem 2
def solar_system(T, x_e, x_m, omega_e, omega_m):
    """Plot the trajectories of the earth and moon over the time interval [0,T]
    assuming the initial position of the earth is (x_e,0) and the initial
    position of the moon is (x_m,0).

    Parameters:
        T (int): The final time.
        x_e (float): The earth's initial x coordinate.
        x_m (float): The moon's initial x coordinate.
        omega_e (float): The earth's angular velocity.
        omega_m (float): The moon's angular velocity.
    """
    raise NotImplementedError("Problem 2 incomplete!")


def random_vector(n):
    """Generate a random vector of length n as a list."""
    return [random() for i in range(n)]


def random_matrix(n):
    """Generate a random nxn matrix as a list of lists."""
    return [[random() for j in range(n)] for i in range(n)]


def matrix_vector_product(A, x):
    """Compute the matrix-vector product Ax as a list."""
    m, n = len(A), len(x)
    return [sum([A[i][k] * x[k] for k in range(n)]) for i in range(m)]


def matrix_matrix_product(A, B):
    """Compute the matrix-matrix product AB as a list of lists."""
    m, n, p = len(A), len(B), len(B[0])
    return [
        [sum([A[i][k] * B[k][j] for k in range(n)]) for j in range(p)] for i in range(m)
    ]


# Problem 3
def prob3():
    """Use time.time(), timeit.timeit(), or %timeit to time
    matrix_vector_product() and matrix-matrix-mult() with increasingly large
    inputs. Generate the inputs A, x, and B with random_matrix() and
    random_vector() (so each input will be nxn or nx1).
    Only time the multiplication functions, not the generating functions.

    Report your findings in a single figure with two subplots: one with matrix-
    vector times, and one with matrix-matrix times. Choose a domain for n so
    that your figure accurately describes the growth, but avoid values of n
    that lead to execution times of more than 1 minute.
    """
    raise NotImplementedError("Problem 3 incomplete!")


# Problem 4
def prob4():
    """Time matrix_vector_product(), matrix_matrix_product(), and np.dot().

    Report your findings in a single figure with two subplots: one with all
    four sets of execution times on a regular linear scale, and one with all
    four sets of exections times on a log-log scale.
    """
    raise NotImplementedError("Problem 4 incomplete!")
