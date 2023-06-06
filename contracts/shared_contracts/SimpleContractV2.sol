pragma solidity ^0.8.0;

contract SimpleContractV2 {
    uint256 public value;

    function initialize(uint256 _value) public {
        value = _value;
    }

    // Updated the function to increment the value
    function getValue() public returns (uint256) {
        value = value + 1;
        return value;
    }

    // Added a new function to set the value
    function setValue(uint256 _value) public {
        value = _value;
    }
}
