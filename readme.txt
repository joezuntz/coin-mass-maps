Downloading point clouds
------------------------

url: https://datasync.ed.ac.uk/index.php/s/UNxa8FCiVm2nlbw
password: coin

You can download the complete folder and unzip it.
For some reason using MacOS Finder to this failed for me, but cmd line unzip worked.

Files
-----

Simulations:
    Points:
        {i}-full-noisy.fits
        {i}-full-noisefree.fits
        {i}-masked-noisy.fits
        {i}-masked-noisefree.fits

        These are all RA,Dec points sampled from the corresponding FLASK kappa maps.
        All have the same cosmology, listed in the coin.config file.
        "full" means full-sky, "masked" uses the DES Y1 mask.
        "noisefree" means directly from the simulated kappa maps
        "noisy" means after map-making using the flask simulated catalogs

    Truths:
        {i}-truth-maps.fits
        Healpix maps of the true kappa, g1, g2

DES:
    des-masked-noisy.fits

    This is a densely sampled (10^6 points) set from DES Y1 E maps.
    You might want to downsample it.


Generating your own point clouds
--------------------------------

- Get input data from here, downloading the entire folder and putting it in this directory:
    https://datasync.ed.ac.uk/index.php/s/113vLrhBSRFywJh
    password: coin
    
    Again, MacOS Finder to this failed for me, but cmd line unzip worked.

- Install
    This requires the tool "flask" to be compiled and on your PATH:
    https://github.com/hsxavier/flask

- Configure
    The relevant choices are mostly defined at the top of make-mass-maps.py
    You probably don't need to adjust the flask settings, but could have a look

- Run
    python make-mass-maps.py


