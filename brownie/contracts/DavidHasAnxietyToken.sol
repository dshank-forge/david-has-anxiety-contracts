// SPDX-License-Identifier: MIT

// How much energy does one tx on this contract use?

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract DavidHasAnxietyToken is ERC721 {
    uint256 public tokenCounter;

    constructor () public ERC721("DavidHasAnxiety", "DHA"){
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newTokenId;
    }
}