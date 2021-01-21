"""
 Example of pinoccio implementation.
 Here we load a model
"""
from pathlib import Path
from pinocchio import buildModelFromUrdf

# This path refers to Pinocchio source code but you can define your own
# directory here.


def main():
    """
        Main procedure
        1 ) Get the path of the urdf model
        2 ) Build the pinocchio model
        2 ) Print some infor of the model
    """
    model_file = Path(__file__).absolute(
    ).parents[1].joinpath('urdf', 'twolinks.urdf')
    # Load the urdf model
    model = buildModelFromUrdf(str(model_file))
    model_name = model.name
    number_of_joints = model.njoints
    for i in range(number_of_joints):
        joint = model.joints[i]
        joint_name = model.names[i]
        jid = joint.idx_q
        joint_placement = model.jointPlacements[i]

        numpy_translation_vector = joint_placement.translation
        numpy_rotation_matrix = joint_placement.rotation

        if jid >= 0:
            damping = model.damping[jid]
            effortLimit = model.effortLimit[jid]
            friction = model.friction[jid]
            lowerPositionLimit = model.lowerPositionLimit[jid]
            upperPositionLimit = model.upperPositionLimit[jid]
            velocityLimit = model.velocityLimit[jid]

    number_of_frames = model.nframes
    for i in range(number_of_frames):
        frame = model.frames[i]
        frame_name = frame.name
        frame_placement = frame.placement
        numpy_translation_vector = frame_placement.translation
        numpy_rotation_matrix = frame_placement.rotation

    for inertia in model.inertias:
        print(inertia)


if __name__ == '__main__':
    main()
