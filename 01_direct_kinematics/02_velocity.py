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
from pinocchio import getVelocity
from pinocchio import getFrameVelocity
from pinocchio import computeJointJacobians
from pinocchio import getJointJacobian
from pinocchio import getFrameJacobian
# Updates the positions of the frames given the joints positions in data
from pinocchio import updateFramePlacements
from pinocchio import randomConfiguration
from pinocchio import ReferenceFrame
import numpy as np

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
    numpy_vector_joint_vel = np.random.rand(model.njoints-1)
    # Perform the forward kinematics over the kinematic tree
    forwardKinematics(model, data, numpy_vector_joint_pos,
                      numpy_vector_joint_vel)
    computeJointJacobians(model, data, numpy_vector_joint_pos)

    joint_number = model.njoints
    for i in range(joint_number):
        joint = model.joints[i]
        joint_placement = data.oMi[i]
        joint_velocity = getVelocity(
            model, data, i, ReferenceFrame.LOCAL_WORLD_ALIGNED)

        joint_jacobian = getJointJacobian(
            model, data, i, ReferenceFrame.LOCAL_WORLD_ALIGNED)

        joint_linear_vel = joint_velocity.linear
        joint_angular_vel = joint_velocity.angular
        joint_6v_vel = joint_velocity.vector

        err = joint_6v_vel - joint_jacobian.dot(numpy_vector_joint_vel)
        assert np.linalg.norm(err, ord=np.inf) < 1.0e-10, err

    # CAUTION updateFramePlacements must be called to update frame's positions
    # Remark: in pinocchio frames, joints and bodies are different things
    updateFramePlacements(model, data)
    frame_number = model.nframes
    for i in range(frame_number):
        frame = model.frames[i]
        frame_placement = data.oMf[i]
        frame_velocity = getFrameVelocity(
            model, data, i, ReferenceFrame.LOCAL_WORLD_ALIGNED)

        frame_jacobian = getFrameJacobian(
            model, data, i, ReferenceFrame.LOCAL_WORLD_ALIGNED)

        frame_linear_vel = frame_velocity.linear
        frame_angular_vel = frame_velocity.angular
        frame_6v_vel = frame_velocity.vector

        err = frame_6v_vel - frame_jacobian.dot(numpy_vector_joint_vel)
        assert np.linalg.norm(err, ord=np.inf) < 1.0e-10, err


if __name__ == '__main__':
    main()
