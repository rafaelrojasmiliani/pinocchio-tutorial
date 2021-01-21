## Pinocchio Tutorial

This is a tutorial which containts the basic operations that can be done with [pinocchio](https://stack-of-tasks.github.io/pinocchio/) robot dynamic engine.

## Structure

| Folder             | Description                               |
| ----------------------- | ----------------------------------------- |
| `urdf` | URDF models of the robots |
| `docker`  | Docker files: scripts to build and image with pinocchio a run its container (Windows and Linux) | 
| `00_load_model`         | Example to load a model from an URDF file and basic model properties: joints and frames|
| `01_forward_kinematics` | Examples to compute the forward and differential kinematics: How to get joint/frames positions, velocities and Jacobian |
| `02_inverse_dynamics`   | Example to compute the inverse dynamics and the derivatives of the torque with respect to the joints positions, velocities and accelerations |
