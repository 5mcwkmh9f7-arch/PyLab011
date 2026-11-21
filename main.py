#!/usr/bin/env python3
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite


def main():
    # Root of the mindmap
    root = MindMapComposite("Building a Kitchen Cabinet", "circle")

    design = MindMapComposite("Design", "oval")
    design.add(MindMapLeaf("Measure the wall and openings", "plain"))
    design.add(MindMapLeaf("Draw the layout", "plain"))
    design.add(MindMapLeaf("Pick door style and finish", "plain"))
    root.add(design)

    materials = MindMapComposite("Materials", "square")
    materials.add(MindMapLeaf("Plywood or melamine sheets", "plain"))
    materials.add(MindMapLeaf("Edgebanding", "plain"))
    materials.add(MindMapLeaf("Hinges and drawer slides", "plain"))
    materials.add(MindMapLeaf("Stain or paint", "plain"))
    root.add(materials)

    shop = MindMapComposite("Shop Work", "hexagon")
    cutting = MindMapComposite("Cutting", "cloud")
    cutting.add(MindMapLeaf("Draw it in Cabinet Vision", "plain"))
    cutting.add(MindMapLeaf("Send it to the CNC to cut", "plain"))
    shop.add(cutting)
    shop.add(MindMapLeaf("Run edges on the edgebander", "plain"))
    shop.add(MindMapLeaf("Assemble the boxes", "plain"))
    shop.add(MindMapLeaf("Spray the finish", "plain"))
    root.add(shop)

    install = MindMapComposite("Install", "bang")
    install.add(MindMapLeaf("Level and shim", "plain"))
    install.add(MindMapLeaf("Screw boxes to the wall", "plain"))
    install.add(MindMapLeaf("Hang doors and adjust", "plain"))
    root.add(install)

    quality = MindMapComposite("Quality Control", "oval")
    quality.add(MindMapLeaf("Check gaps and reveals", "plain"))
    quality.add(MindMapLeaf("Touch up the finish", "plain"))
    root.add(quality)

    print("mindmap")
    root.display(2)


if __name__ == "__main__":
    main()
