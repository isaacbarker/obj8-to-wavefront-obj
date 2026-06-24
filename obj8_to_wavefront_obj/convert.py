"""

X-Plane OBJ8 to Wavefront .obj standard

Converts X-Plane OBJ8 (.obj) files detailed here (https://developer.x-plane.com/article/obj8-file-format-specification)
to Wavefront (.obj) files for use in cases outside simulation (https://en.wikipedia.org/wiki/Wavefront_.obj_file)
This converter does not currently (and probably will never) support Animation
TEXTURE_LIT is also not supported

DO NOT USE THIS SCRIPT ON COPYRIGHTED CONTENT

"""

import os
from pathlib import Path

from PIL import Image

def obj8_2_wavefront(input_file_path, output_file_path, relative_path=True):

    output_file_stem = '.'.join(output_file_path.split('.')[:-1])
    input_file_stem = '/'.join(input_file_path.split('/')[:-1])
    name = Path(input_file_path).stem

    # define list of vertices, texture coordinates, and normal coordinates, as well as faces
    v = []
    vt = []
    vn = []
    idx = []
    f = []
    texture_path = ""

    # read lines for filepath
    with (open(input_file_path, "r")) as input_file:

        # parse OBJ8 file line-by-line
        lines = input_file.readlines()

        for line in lines:
            line = line.strip()

            if line.startswith('VT'):
                # match vertices VT commands to individual v, vt and vn
                data = line.split(" ")

                # separate out data points
                geometric_vertices = (data[1], data[2], data[3])
                normal_vertices = (data[4], data[5], data[6])
                texture_coordinates = (data[7], data[8])

                # append to file
                v.append(geometric_vertices)
                vt.append(texture_coordinates)
                vn.append(normal_vertices)

            if line.startswith('IDX') or line.startswith('IDX10'):
                # match index table

                # strip identifier
                indexes = line.split(" ")
                indexes.pop(0)

                # 1-index the elements and add to idx
                indexes = list(map(int, indexes))
                indexes_one_indexed = [x + 1 for x in indexes]

                # add to idx list to be used
                idx.extend(indexes_one_indexed)

            if line.startswith('TRIS'):
                # match faces
                data = line.split(" ")

                # extract offset and count
                offset = int(data[1])
                count = int(data[2])

                # group specified indices into 3
                idx_start = offset
                idx_end = offset + count

                active_idx = idx[idx_start:idx_end]

                # Someone scarily good at one-liners:
                # https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
                faces = zip(*(iter(active_idx),) * 3)
                f.extend(faces)

            if line.startswith('TEXTURE '):
                # build texture file
                data = line.split(" ")
                texture_path = input_file_stem + "/" + data[1]

                if texture_path.endswith('.dds'):
                    img = Image.open(texture_path)
                    texture_path = output_file_stem + '.png'
                    os.makedirs(os.path.dirname(texture_path), exist_ok=True)
                    img.save(texture_path)

    # create .mtl file from data
    with open(output_file_stem + ".mtl", "w") as output_file:
        output_file.write("newmtl Material\n")

        if relative_path:
            output_file.write("map_Kd " + name + ".png\n")
        else:
            output_file.write("map_Kd " + texture_path)

    # create .obj file from data
    with open(output_file_stem + ".obj", "w") as output_file:

        # add texture
        if relative_path:
            output_file.write("mtllib " + name + ".mtl\n")
        else:
            output_file.write("mtllib " + output_file_stem + ".mtl\n")

        # create v, vt and vn commands
        output_file.write("\n# list of geometric vertices\n")
        for vs in v:
            v_command = "v " + " ".join(map(str, vs))
            output_file.write(v_command + "\n")

        output_file.write("\n# list of texture coordinates\n")
        for vts in vt:
            vt_command = "vt " + " ".join(map(str, vts))
            output_file.write(vt_command + "\n")

        output_file.write("\n# list vertex normals\n")
        for vns in vn:
            vn_command = "vn " + " ".join(map(str, vns))
            output_file.write(vn_command + "\n")

        # create face commands
        output_file.write("\nusemtl Material\n")
        output_file.write("\n# list of faces\n")
        for faces in f:
            f_command = "f " + " ".join(f"{face}/{face}/{face}" for face in faces)
            output_file.write(f_command + "\n")