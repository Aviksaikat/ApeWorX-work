// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;


contract KingForever {
    address owner;
    uint256 prize;


    constructor() payable {
        owner = msg.sender;
        prize = msg.value;
    }

    function overthrowKing(address payable _addr) external payable{
        (bool tx, ) = _addr.call{value: prize}("");

        require(tx, "Error sending ETH!!");
    }

    receive() external payable {
        revert("Ahhhhhhahha You didn't said the magic word!");
    }

}