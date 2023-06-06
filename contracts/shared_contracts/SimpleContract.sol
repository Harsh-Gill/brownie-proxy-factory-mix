pragma solidity ^0.8.0;

contract SimpleContract {
    uint256 public value;

    function initialize(uint256 _value) public {
        value = _value;
    }

    function getValue() public returns (uint256) {
        return value;
    }
}
