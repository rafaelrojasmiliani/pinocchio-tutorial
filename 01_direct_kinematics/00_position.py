"""
 Example of pin implementation.
 This example only shows how to create a simple pinoccio model
 from a URDF file and then it compute the forward kinermatics
 REMARK: In this section we use the data model. the data model is a
 pinocchio class that stores relevant information about the kinematics
 and dynamics of the model. This class is used as an argument for much
 of the pinocchio functions in order used it and store its result
"""
from pathlib import Path
# Loads URDF model into pinocchio
from pinocchio import buildModelFromUrdf
# Stores the forward kinematics of the joints into the data argument
from pinocchio import forwardKinematics
# Updates the positions of the frames given the joints positions in data
from pinocchio import updateFramePlacements
from pinocchio import randomConfiguration

# This path refers to Pinocchio source code but you can define your own
# directory here.


def main():
    '''
        Main procedure
        1 ) Build the model from an URDF file
        2 ) compute forwardKinematics
        3 ) compute forwardKinematics of the frames
        4 ) explore data
    '''
    model_file = Path(__file__).absolute(
    ).parents[1].joinpath('urdf', 'twolinks.urdf')
    model = buildModelFromUrdf(str(model_file))
    # Create data required by the algorithms
    data = model.createData()
    # Sample a random configuration
    numpy_vector_joint_pos = randomConfiguration(model)
    # Perform the forward kinematics over the kinematic tree
    forwardKinematics(model, data, numpy_vector_joint_pos)
    # CAUTION updateFramePlacements must be called to update frame's positions
    # Remark: in pinocchio frames, joints and bodies are different things
    updateFramePlacements(model, data)
    # Print out the placement of each joint of the kinematic tree
    joint_number = model.njoints
    for i in range(joint_number):
        joint = model.joints[i]
        joint_placement = data.oMi[i]

    frame_number = model.nframes
    for i in range(frame_number):
        frame = model.frames[i]
        frame_placement = data.oMf[i]


if __name__ == '__main__':
    main()
