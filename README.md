# Classic 3D - Redux

<a href='https://ko-fi.com/P5P5KH154' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi3.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
[![Modrinth](https://img.shields.io/modrinth/dt/FRSckbRo)](https://modrinth.com/resourcepack/FRSckbRo "Modrinth")

This project aims to rebuild the original Classic 3D resource pack from the ground up.
The original project grew increasingly complex and harder to maintain.
With years of legacy code and a lack of interest, the project became abandoned.
Redux is a careful and methodical recreation.

## Build

Classic 3D Redux is built with `mcpacker`.

### Debug

Create a file in your `.minecraft` folder called `allowed_symlinks.txt`. Add the directory of the project's `build` folder.

Run the following command to generate a 1.20 debug build:

```sh
mcpacker build debug 1-20
```
