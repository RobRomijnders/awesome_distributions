"""
Visualize points on the 3-simplex (eg, the parameters of a
3-dimensional multinomial distributions) as a scatter plot
contained within a 2D triangle.

David Andrzejewski (david.andrzej@gmail.com)
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as MT
import matplotlib.lines as L
from scipy.stats import dirichlet


def plotSimplex(points, fig=None,
                vertexlabels=['0', '1', '2'],
                **kwargs):
    """
    Plot Nx3 points array on the 3-simplex
    (with optionally labeled vertices)

    kwargs will be passed along directly to matplotlib.pyplot.scatter

    Returns Figure, caller must .show()
    """
    if (fig == None):
        fig = plt.figure()
    # Draw the triangle
    l1 = L.Line2D([0, 0.5, 1.0, 0],  # xcoords
                  [0, np.sqrt(3) / 2, 0, 0],  # ycoords
                  color='k')
    fig.gca().add_line(l1)
    fig.gca().xaxis.set_major_locator(MT.NullLocator())
    fig.gca().yaxis.set_major_locator(MT.NullLocator())
    # Draw vertex labels
    fig.gca().text(-0.05, -0.05, vertexlabels[0])
    fig.gca().text(1.05, -0.05, vertexlabels[1])
    fig.gca().text(0.5, np.sqrt(3) / 2 + 0.05, vertexlabels[2])
    # Project and draw the actual points
    projected = projectSimplex(points)
    plt.scatter(projected[:, 0], projected[:, 1], **kwargs)
    # Leave some buffer around the triangle for vertex labels
    fig.gca().set_xlim(-0.2, 1.2)
    fig.gca().set_ylim(-0.2, 1.2)

    return fig


def projectSimplex(points):
    """
    Project probabilities on the 3-simplex to a 2D triangle

    N points are given as N x 3 array
    """
    # Convert points one at a time
    tripts = np.zeros((points.shape[0], 2))
    for idx in range(points.shape[0]):
        # Init to triangle centroid
        x = 1.0 / 2
        y = 1.0 / (2 * np.sqrt(3))
        # Vector 1 - bisect out of lower left vertex
        p1 = points[idx, 0]
        x = x - (1.0 / np.sqrt(3)) * p1 * np.cos(np.pi / 6)
        y = y - (1.0 / np.sqrt(3)) * p1 * np.sin(np.pi / 6)
        # Vector 2 - bisect out of lower right vertex
        p2 = points[idx, 1]
        x = x + (1.0 / np.sqrt(3)) * p2 * np.cos(np.pi / 6)
        y = y - (1.0 / np.sqrt(3)) * p2 * np.sin(np.pi / 6)
        # Vector 3 - bisect out of top vertex
        p3 = points[idx, 2]
        y = y + (1.0 / np.sqrt(3) * p3)

        tripts[idx, :] = (x, y)

    return tripts


if __name__ == '__main__':
    alphas = [5, 13, 2]
    alphas_aggregated = [alphas[0], alphas[1] + alphas[2]]

    num_samples_scatter = 100
    num_samples_histogram = 10 ** 6

    samples = dirichlet(alpha=alphas).rvs(size=num_samples_scatter)

    # Do scatter plot
    fig = plotSimplex(samples, s=10)
    plt.title(f'Scatter plot of 3D Dirichlet with alphas {alphas}')
    fig.show()

    plt.figure()
    marginalised_samples = dirichlet(alpha=alphas_aggregated).rvs(size=num_samples_histogram)
    plt.hist(marginalised_samples[:, 1], bins = int(np.sqrt(num_samples_histogram)), density=True)
    plt.xlabel('First dimension' + '<' + '-'*20 + '>' + 'Second and third dimension aggregated')
    plt.title('Histogram of aggregated 3D Dirichlet')
    plt.ylabel(f'Normalized histogram of {num_samples_histogram} samples')
    plt.xlim([0.0, 1.0])

    plt.show()
