# freeHPC - Free HoloPlay Core SDK
_Authors: Yann Vernier, Christian Stolze_

This free library replicates some of the functionality of the proprietary HoloPlay Core SDK of the Looking Glass Factory under a [GPL compatible license](https://github.com/regcs/freehpc/blob/master/LICENSE). Its main purpose is to enable work with the Looking Glass devices with GPL'ed software. The authors of freeHPC are not associated with the Looking Glass Factory.

## Readme

Some info will follow later.

## Known limitations:

- pretty hacky solutions in general
- requires [hidapi](https://github.com/libusb/hidapi) and the corresponfing python wrapper [pyhid](https://github.com/apmorton/pyhidapi) to be installed in your python environment
- may fail to connect to Looking Glass under special circumstances on macOS
- currently does not support Looking Glass Portrait

## License

This python library is released under the [MIT license](https://github.com/regcs/freehpc/blob/master/LICENSE).
