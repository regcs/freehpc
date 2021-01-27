# freeHPC - Free HoloPlay Core SDK
_Authors: Yann Vernier, Christian Stolze_

This free library replicates some of the functionality of the proprietary HoloPlay Core SDK of the Looking Glass Factory under a [GPL compatible license](https://github.com/regcs/freehpc/blob/master/LICENSE). Its main purpose is to enable work with the Looking Glass devices with GPL software by providing a GPL-compatabile API. This API retrieves the calibration data of Looking Glass devices either via HIDAPI or via communication with the HoloPlay Service App. 

The authors of freeHPC are not associated with the Looking Glass Factory.

## Readme

Some info will follow later.

## Known limitations:

- pretty hacky solutions in general
- requires [hidapi](https://github.com/libusb/hidapi) and the corresponding python wrapper [pyhid](https://github.com/apmorton/pyhidapi) to be installed in your python environment
- may fail to connect to Looking Glass under special circumstances on macOS
- currently does support Looking Glass Portrait only via communication over HoloPlay Service App

## License

This python library is released under the [MIT license](https://github.com/regcs/freehpc/blob/master/LICENSE).

freeHPC partially relies on the following GPL-compatible open-source libraries and/or python modules:
- [pyhidapi](https://github.com/apmorton/pyhidapi) licensed under [MIT License](https://github.com/apmorton/pyhidapi/blob/master/LICENSE)
- [hidapi](https://github.com/flirc/hidapi) licensed under [GNU GPL v3](https://github.com/flirc/hidapi/blob/master/LICENSE-gpl3.txt)
- [pynng](https://github.com/codypiersall/pynng) licensed under [MIT license](https://github.com/codypiersall/pynng/blob/master/LICENSE.txt)
- [cbor](https://pypi.org/project/cbor/1.0.0/) licensed under [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
