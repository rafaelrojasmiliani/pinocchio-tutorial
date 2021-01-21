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
from pinocchio import rnea
from pinocchio import computeRNEADerivatives
from pinocchio import randomConfiguration
import numpy as np


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
    numpy_vector_joint_acc = np.random.rand(model.njoints-1)
    # Calls Reverese Newton-Euler algorithm
    numpy_vector_joint_torques = rnea(model, data, numpy_vector_joint_pos,
                                      numpy_vector_joint_vel, numpy_vector_joint_acc)
    computeRNEADerivatives(model, data, numpy_vector_joint_pos,
                           numpy_vector_joint_vel, numpy_vector_joint_acc)
    dtorques_dq = data.dtau_dq
    dtorques_dqd = data.dtau_dv
    dtorques_dqdd = data.M


if __name__ == '__main__':
    main()
