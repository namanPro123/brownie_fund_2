//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract fundme {
    //AggregatorV3Interface internal pricedFeed;
    address public owner;
    address[] public funders;
    AggregatorV3Interface public priceFeed;

    constructor(address _pricefeed) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_pricefeed);
    }

    mapping(address => uint256) adress_to_amount;

    function fund() public payable {
        //$2
        require(convert(msg.value) >= 2 * 10**18, "fund with more ether");
        adress_to_amount[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function get_value_paid(address the_adress) public view returns (uint256) {
        return adress_to_amount[the_adress];
    }

    function valueofEthintermsofUsd() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price * 10**10);
    }

    function convert(uint256 eth_amount) public view returns (uint256) {
        uint256 ethprice = valueofEthintermsofUsd();
        uint256 usd_value = (ethprice * eth_amount) / 10**18;
        return usd_value;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "you are not the admin");
        _;
    }

    function withdraw() public payable onlyOwner {
        // address payable msg_sender=payable(msg.sender);
        //address payable wallet = address(uint160(addr));
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 index = 0; index < funders.length; index++) {
            adress_to_amount[funders[index]] = 0;
        }
        funders = new address[](0);
    }
}
