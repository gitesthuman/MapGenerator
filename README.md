# MapGenerator

Requires Python3.10, numpy, opencv2, tkinter.

# Assets
In folder assets there are some textures I uploaded. If you want to use or own ones, add them in file `resources.py` to list `textures`. 
The patern is tuple containing: (texture_path, texture_name).

# Guide

Select dimensions your map you want to have and single tile size in pixels.

![image](https://user-images.githubusercontent.com/90265591/213894945-4e06ed63-e5ff-497f-99a7-9aa360cb3d7e.png)

Right-click on field you want to change, then select one of the textures.
Press ENTER to save your image. The file will be named `your_map.png`.

![image](https://user-images.githubusercontent.com/90265591/213894860-e63adedc-d3e9-4b5b-bb34-3428741c8129.png)

You can also hold left mouse button to select an area and paste one texture to 
every single of selected fields.

![img](https://user-images.githubusercontent.com/90265591/213919314-e20c81a4-215a-495e-a3bb-a6de5622a8be.png)

After saving the map you can set up entities' positions. Press ENTER to save it
to a json file `entities.json`.