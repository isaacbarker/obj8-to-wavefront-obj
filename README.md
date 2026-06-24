## X-Plane OBJ8 to Wavefront .obj standard

Converts X-Plane OBJ8 (.obj) files detailed here (https://developer.x-plane.com/article/obj8-file-format-specification)
to Wavefront (.obj) files for use in cases outside simulation (https://en.wikipedia.org/wiki/Wavefront_.obj_file),
specifically designed for converting simple meshes in CSL or Model Matching Libraries quickly.

### What is supported?

- VT, TEXTURE, TRIS and IDX commands
- .dds and .png textures with simple .mtl conversion, where the texture covers the entire mesh


### What isn't supported
-  ANIMATION & TEXTURE_LIT commands
-  Multiple textures

For examples of the results of using this tool see [isaacbarker/bluebell-csl-wavefront-obj](https://github.com/isaacbarker/bluebell-csl-wavefront-obj)


**DO NOT USE THIS SCRIPT ON COPYRIGHTED CONTENT**
