## linear gravity generator point of origin
for width and depth, it's the middle of the block.
But for height, it's the bottom of the block.

## Airtight custom doors using merge blocks

If using hinges for your door movement, use 2 of them.
 
The hinge block is a bit special since the hinge body and the hinge head occupy the same block space. 
Merging links two grids into one, but what that would theoretically do is try to shove a hinge head and hinge body on the same spot. 
Since that can't happen, the game stops you from doing it. 

merge blocks cannot merge two grids whose blocks' bounding cubes would overlap post-merge in any way, and they can't tell the difference between ones that actually can't overlap and ones that can.

So that's why you need the extra grid connecting the two - to put space between the ones being merged, while it ignores the grid it is hinged from due to it not being either of the merged grids

the door and the frame mustn't have full faces touching, or they will permanently merge - ie, when the emrge blocks turn off, they'll still be 1 grid.
The game doesn't remember the old seam or anything.
