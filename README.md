## X-Plane OBJ8 to Wavefront .obj standard

Converts X-Plane OBJ8 (.obj) files detailed here (https://developer.x-plane.com/article/obj8-file-format-specification)
to Wavefront (.obj) files for use in cases outside simulation (https://en.wikipedia.org/wiki/Wavefront_.obj_file),
specifically designed for converting simple meshes in CSL or Model Matching Libraries quickly.

### Usage

To use the library simply install using `pip install obj8-to-wavefront-obj`. Then import the package and use the
following function:

```python

    from obj8_to_wavefront_obj import obj8_2_wavefront
    
    input_file_path = "input.obj"
    output_file_path = "output.obj"
    
    obj8_2_wavefront(input_file_path, output_file_path, relative_path=True)

```

The `relative_path` field determines if the outputted `.mtl` and texture will be referenced by their full path or just
their relative path. The default value is `True`.

### What is supported?

- VT, TEXTURE, TRIS and IDX commands
- .dds and .png textures with simple .mtl conversion, where the texture covers the entire mesh


### What isn't supported
-  ANIMATION & TEXTURE_LIT commands
-  Multiple textures

For examples of the results of using this tool see [isaacbarker/bluebell-csl-wavefront-obj](https://github.com/isaacbarker/bluebell-csl-wavefront-obj)


**DO NOT USE THIS SCRIPT ON COPYRIGHTED CONTENT**
