# Classic 3D - Redux

This project aims to rebuild the original Classic 3D resource pack from the ground up. The original project grew increasingly complex and harder to maintain. With years of legacy code and a lack of interest, the project became abandoned. Redux will be a carful and methodical recreation.

## Build

### Debug
 
Create a file in your `.minecraft` folder called `allowed_symlinks.txt`. Add the directory of the project's `build` folder.

Run the following command to generate a 1.20 debug build:

```sh
mcpacker build debug 1-20
```
