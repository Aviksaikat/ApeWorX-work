// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// 0x73d00519B15B74D88369cA5111eaF5c4Ad1c73F9
interface Building {
    function isLastFloor(uint256) external returns (bool);
}

contract Elevator {
    bool public top;
    uint256 public floor;

    function goTo(uint256 _floor) public {
        Building building = Building(msg.sender);

        if (!building.isLastFloor(_floor)) {
            floor = _floor;
            top = building.isLastFloor(floor);
        }
    }
}