import matplotlib.pyplot as plt
import numpy as np

def draw_vietnam_flag():
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor('#C21807')

    # Draw the darker red background
    ax.add_patch(plt.Rectangle((0, 0), 3, 2, color='#C21807'))

    # Function to draw the star
    def draw_star(center, size):
        # Calculate the points of a five-pointed star
        angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
        angles = np.add(angles, np.pi / 2)
        radii = np.array([size, size * 0.4] * 5)
        points = np.vstack((radii * np.cos(angles), radii * np.sin(angles))).T
        star_points = points + center

        # Draw the star
        star = plt.Polygon(star_points, color='#FFFF00', edgecolor='none')
        ax.add_patch(star)

    # Draw the yellow star
    draw_star((1.5, 1), 0.8)

    # Set the limits and remove axes
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 2)
    ax.axis('off')

    # Remove all borders and spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Remove the white border completely
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    plt.show()

draw_vietnam_flag()