import bpy
import bmesh
import numpy as np
from PIL import Image

def create_plane(img_path, block_size=1.0):
    # Load the image
    img = Image.open(img_path)

    # Convert the image to a numpy array
    img = np.asarray(img)

    # Get the image size
    height, width, _ = img.shape

    # Create a plane
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=width-1, y_segments=height-1, size=1)
    plane = bpy.data.objects.new("Plane", bpy.data.meshes.new("Plane"))
    plane.data = bm.to_mesh()
    plane.data.uv_textures.new()
    bm.free()

    # Scale the plane to match the block size
    plane.scale = (width * block_size, height * block_size, block_size)

    # Texture the plane with the image
    mat = bpy.data.materials.new("Material")
    plane.data.materials.append(mat)
    plane.data.uv_textures[0].data[0].image = bpy.data.images.load(img_path)
    plane.data.uv_textures[0].active = True

    # Return the plane object
    return plane

def create_minecraft_blocks(img_path, block_size=1.0):
    # Load the image
    img = Image.open(img_path)

    # Convert the image to a numpy array
    img = np.asarray(img)

    # Get the image size
    height, width, _ = img.shape

    # Create a cube for each pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = img[y, x]

            # Only create a cube if the pixel is not fully transparent
            if r + g + b > 0:
                bpy.ops.mesh.primitive_cube_add(size=block_size)
                cube = bpy.context.object
                cube.location = (x * block_size, y * block_size, 0)

                # Map the texture of the cube to the corresponding part of the image
                uv_coords = (x / (width - 1), y / (height - 1))
                mat = cube.data.materials[0]
                mat.use_nodes = True
                tex_node = mat.node_tree.nodes.new("ShaderNodeTexImage")
                tex_node.image = bpy.data.images.load(img_path)
                uv_node = mat.node_tree.nodes.new("ShaderNodeUVMap")
                uv_node.uv_map = "UVMap"
                mat.node_tree.links.new(uv_node.outputs[0], tex_node.inputs[0])

                # Set the color of the cube
                cube.data.materials[0].diffuse_color = (r / 255, g / 255, b / 255)

#group the cubes to form larger blocks
def group_cubes():
    # Select all the cubes
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.select_by_type(type="EMPTY")

    # Group the cubes
    bpy.ops.object.group_link(group="Minecraft Blocks")

#export the 3D model to a Minecraft world file
def export_world():
    # Select all the cubes
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.select_by_type(type="EMPTY")

    # Export the world
    bpy.ops.export.mcprep.export_world()



def main():
    # Create a plane
    plane = create_plane("la.jpeg", block_size=0.5)

    # Create the Minecraft blocks
    create_minecraft_blocks("img.png", block_size=0.5)

    # Add the plane to the scene
    bpy.context.scene.collection.objects.link(plane)

    # Group the cubes
    group_cubes()

    # Export the world
    export_world()

if __name__ == "__main__":
    main()
