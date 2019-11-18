import numpy as np
import healpy as hp
import fitsio
import matplotlib.pyplot as plt


def points_in_mask(ridge_points, mask):
    # Unpack the ridge points
    ra, dec = ridge_points.T

    # Get the size of the mask and from that the resolution
    mask_npix = mask.size
    mask_nside = hp.npix2nside(mask_npix)

    # Get the pixel index for the ridge points    
    pix = hp.ang2pix(mask_nside, ra, dec, lonlat=True)

    # return an array of whether the pixel is masked at each ridge point
    return mask[pix]>0

def main():
    # Load the input data
    mask = fitsio.read("../coin-input/y1a1_spt_mcal_0.2_1.3_mask.fits")['mask']
    ridge_points = np.load("des_real_ridges.npy")

    # Find which points are masked out
    selection = points_in_mask(ridge_points, mask)

    # Report the mask fraction
    f = 1 - selection.sum() / selection.size
    print(f"Fraction removed: {f:.1%}")

    # Plot a map of which points are cut (black) and which are kept (red)
    plt.plot(ridge_points[ selection,0], ridge_points[ selection,1], 'r.', markersize=1)
    plt.plot(ridge_points[~selection,0], ridge_points[~selection,1], 'k.', markersize=1)
    plt.show()

if __name__ == '__main__':
    main()
    